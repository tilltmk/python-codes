# metadaten werden beibehalten 
# versionierung wenn dateien ungleich 
# keine gui wegen performance 
# verbose mode 
# progressbar

import os
import shutil
import hashlib
from tqdm import tqdm
import time

def calculate_md5(file_path, block_size=65536):
    """Berechnet den MD5-Hash einer Datei."""
    md5 = hashlib.md5()
    with open(file_path, 'rb') as f:
        for block in iter(lambda: f.read(block_size), b''):
            md5.update(block)
    return md5.hexdigest()

def copy_with_metadata(source, dest):
    """Kopiert eine Datei und behält dabei die Metadaten wie Zeitstempel bei."""
    shutil.copy2(source, dest)

def move_files(source_dir, dest_dir, verbose=False):
    """Verschiebt Dateien von einem Verzeichnis in ein anderes, mit Fortschrittsanzeige und optionalem Verbose-Modus."""
    files = os.listdir(source_dir)
    
    with tqdm(total=len(files), desc="Verschiebe Dateien", unit="dateien") as pbar:
        for filename in files:
            source_file = os.path.join(source_dir, filename)
            dest_file = os.path.join(dest_dir, filename)

            if os.path.isfile(source_file):
                if os.path.exists(dest_file):
                    if os.path.getsize(source_file) == os.path.getsize(dest_file):
                        source_md5 = calculate_md5(source_file)
                        dest_md5 = calculate_md5(dest_file)

                        if source_md5 == dest_md5:
                            if verbose:
                                print(f"Überspringe {source_file}, da es bereits im Zielverzeichnis existiert und identisch ist.")
                            pbar.update(1)
                            continue
                        else:
                            base, ext = os.path.splitext(filename)
                            version = 2
                            new_filename = f"{base}_{version}{ext}"
                            new_dest_file = os.path.join(dest_dir, new_filename)

                            while os.path.exists(new_dest_file):
                                version += 1
                                new_filename = f"{base}_{version}{ext}"
                                new_dest_file = os.path.join(dest_dir, new_filename)

                            dest_file = new_dest_file

                # Datei kopieren und Metadaten beibehalten
                copy_with_metadata(source_file, dest_file)
                # Originaldatei löschen
                os.remove(source_file)
                
                if verbose:
                    print(f"Verschoben {source_file} nach {dest_file}")
            pbar.update(1)

if __name__ == "__main__":
    source_directory = input("Geben Sie den Quellordner an: ")
    destination_directory = input("Geben Sie den Zielordner an: ")
    verbose_mode = input("Soll der Verbose-Modus aktiviert werden? (ja/nein): ").strip().lower() == 'ja'

    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)

    move_files(source_directory, destination_directory, verbose=verbose_mode)
