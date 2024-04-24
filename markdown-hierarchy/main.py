from flask import Flask, request, render_template_string, jsonify, redirect, url_for
import sqlite3

app = Flask(__name__)
DATABASE = 'hierarchy.db'

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <title>Hierarchie-Editor</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <div class="container mt-4">
        <h1>Hierarchie-Editor</h1>
        <form method="post">
            <select name="level" class="form-control mb-3" onchange="this.form.submit()">
                <option value="">Wähle eine Hierarchieebene</option>
                {% for level in levels %}
                <option value="{{ level[0] }}" {% if selected_level == level[0] %}selected{% endif %}>Ebene {{ level[0] }}</option>
                {% endfor %}
            </select>
            <table class="table" id="editableTable">
                <thead>
                    <tr>
                        <th>Inhalt</th>
                        <th>Aktion</th>
                    </tr>
                </thead>
                <tbody>
                    {% for row in rows %}
                    <tr id="{{ row[0] }}">
                        <td><input type="text" class="form-control" name="content[]" value="{{ row[2] }}"></td>
                        <td>
                            <button type="button" class="btn btn-danger" onclick="deleteRow('{{ row[0] }}')">Löschen</button>
                        </td>
                    </tr>
                    {% endfor %}
                </tbody>
            </table>
            <button type="button" class="btn btn-primary" onclick="addNewRow()">Neue Zeile hinzufügen</button>
            <button type="submit" class="btn btn-success">Änderungen speichern</button>
        </form>
    </div>

    <script>
    function addNewRow() {
        var table = document.getElementById("editableTable").getElementsByTagName('tbody')[0];
        var newRow = table.insertRow();
        var cell1 = newRow.insertCell(0);
        cell1.innerHTML = '<input type="text" class="form-control" name="content[]">';
        var cell2 = newRow.insertCell(1);
        cell2.innerHTML = '<button type="button" class="btn btn-danger" onclick="deleteRow(this.parentNode.parentNode.id)">Löschen</button>';
    }

    function deleteRow(rowId) {
        if (rowId) {
            fetch('/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                },
                body: 'row_id=' + rowId
            }).then(response => response.json())
            .then(data => {
                if(data.success) {
                    var row = document.getElementById(rowId);
                    if (row) {
                        row.parentNode.removeChild(row);
                    }
                }
            });
        }
    }
    </script>
</body>
</html>
"""

def init_db():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS hierarchy (
                id INTEGER PRIMARY KEY,
                level INTEGER,
                content TEXT
            )
        """)
        conn.commit()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        level = request.form.get('level')
        if 'content[]' in request.form:
            contents = request.form.getlist('content[]')
            with sqlite3.connect(DATABASE) as conn:
                cursor = conn.cursor()
                cursor.executemany("INSERT INTO hierarchy (level, content) VALUES (?, ?)",
                                   [(level, content) for content in contents if content.strip()])
                conn.commit()
        elif 'row_id' in request.form:
            row_id = request.form.get('row_id')
            with sqlite3.connect(DATABASE) as conn:
                cursor = conn.cursor()
                cursor.execute("DELETE FROM hierarchy WHERE id = ?", (row_id,))
                conn.commit()
            return jsonify(success=True)
        return redirect(url_for('index', selected_level=level))

    selected_level = request.args.get('level')
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT DISTINCT level FROM hierarchy ORDER BY level")
        levels = cursor.fetchall()
        if selected_level:
            cursor.execute("SELECT id, level, content FROM hierarchy WHERE level = ? ORDER BY id", (selected_level,))
        else:
            cursor.execute("SELECT id, level, content FROM hierarchy ORDER BY id")
        rows = cursor.fetchall()

    return render_template_string(HTML_TEMPLATE, levels=levels, rows=rows, selected_level=selected_level)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
