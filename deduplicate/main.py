import os
import shutil
from datetime import datetime
import hashlib
from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Pfad für den Papierkorb
trash_path = os.path.join(os.getcwd(), 'Papierkorb')
os.makedirs(trash_path, exist_ok=True)

# Funktion zur Berechnung des MD5-Hash einer Datei
def get_hash(file_path):
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

# Funktion zum Durchsuchen des Verzeichnisses und zur Deduplizierung
def deduplicate(directory):
    files_dict = {}
    for root, dirs, files in os.walk(directory):
        for file in files:
            path = os.path.join(root, file)
            file_hash = get_hash(path)
            file_info = os.stat(path)

            if file_hash in files_dict:
                existing_path, existing_size, existing_mtime = files_dict[file_hash]
                if file_info.st_size == existing_size and file_info.st_mtime == existing_mtime:
                    shutil.move(path, trash_path)  # Identische Datei in den Papierkorb
                else:
                    version_count = 0
                    new_path = f"{path}_V{version_count}"
                    while os.path.exists(new_path):
                        version_count += 1
                        new_path = f"{path}_V{version_count}"
                    shutil.move(path, new_path)
            else:
                files_dict[file_hash] = (path, file_info.st_size, file_info.st_mtime)

    return files_dict

# Index der Dateien und Versionen
index = {}

@app.route('/')
def index_page():
    return render_template('index.html', index=index)

@app.route('/update')
def update_index():
    global index
    index = deduplicate('.')
    return jsonify(index)

if __name__ == '__main__':
    app.run(debug=True)
