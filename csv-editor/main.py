from flask import Flask, session
from flask_session import Session  # Importieren der Session-Klasse
from flask import Flask, render_template, request, send_file, session, redirect
import pandas as pd
import csv
import io

app = Flask(__name__)

# Temporärer Speicher für Daten und Secret Key
temp_data = None
temp_secret = None

# Konfiguration
app.config['SESSION_TYPE'] = 'filesystem'  # Verwende das Dateisystem für die Speicherung der Session
Session(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    global temp_data  # Verwende globale Variable
    global columns 
    columns = []  # Stelle sicher, dass 'columns' definiert ist
    selected_columns = session.get('selected_columns', [])  # Lese ausgewählte Spalten aus der Session
    if request.method == 'POST':
        uploaded_file = request.files['file']
        if uploaded_file.filename != '':
            df = pd.read_csv(uploaded_file, delimiter='\t', encoding='utf-8-sig')  # Tabulator als Delimiter
            columns = list(df.columns)
            temp_data = df.to_dict(orient='records')  # Speichere die Daten temporär
            # Speichere ausgewählte Spalten in der Session
            return render_template('index.html', columns=columns, data=temp_data, selected_columns=selected_columns)
    return render_template('index.html', columns=columns, selected_columns=selected_columns)


@app.route('/set_secret', methods=['POST'])
def set_secret():
    global temp_secret  # Verwende globale Variable
    secret = request.form['secret']
    if secret:
        app.secret_key = secret  # Setze den geheimen Schlüssel
        temp_secret = secret  # Speichere den Schlüssel temporär
        Session(app)  # Initialize Session here
        selected_columns = session.get('selected_columns', [])
        session['selected_columns'] = selected_columns  
        session['csv_data'] = temp_data
        return redirect('/download')
    else:
        return 'Kein Geheimnis angegeben', 400

@app.route('/download', methods=['GET'])
def download():
    csv_data = session.get('csv_data')
    selected_columns = session.get('selected_columns', [])  # Lese ausgewählte Spalten aus der Session
    if csv_data:
        csv_output = io.StringIO()
        # Berücksichtige nur ausgewählte Spalten, falls vorhanden
        writer = csv.DictWriter(csv_output, fieldnames=selected_columns if selected_columns else csv_data[0].keys())  
        writer.writeheader()
        for row in csv_data:
            writer.writerow({key: row[key] for key in (selected_columns if selected_columns else row.keys())})  # Berücksichtige nur ausgewählte Spalten, falls vorhanden
        csv_output.seek(0)
        return send_file(io.BytesIO((u'\ufeff' + csv_output.getvalue()).encode('utf-8')), as_attachment=True, download_name='download.csv')
    else:
        return 'Keine Daten zum Download verfügbar', 400

@app.route('/update_csv', methods=['POST'])
def update_csv():
    selected_columns = request.json.get('selected_columns', [])
    session['selected_columns'] = selected_columns
    return 'OK', 200


if __name__ == '__main__':
    app.run(debug=True)


