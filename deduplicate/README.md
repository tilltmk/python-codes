# Datei Deduplizierungs-Tool 🧹🗃️

Dieses Projekt bietet eine effektive Lösung zur Deduplizierung von Dateien in einem Verzeichnis. Es identifiziert Dateien mit gleichen Namen, prüft Größe und Änderungsdatum und führt entsprechende Aktionen durch: Versionierung bei Unterschieden und Verschiebung in den Papierkorb bei identischen Dateien.

## Features 🌟

- **Durchsuchen von Verzeichnissen** 📁: Durchsucht rekursiv alle Unterordner auf der Suche nach doppelten Dateien.
- **Automatische Versionierung** 📑: Erstellt Versionen von Dateien, wenn Größe oder Änderungsdatum variieren.
- **Papierkorb für Duplikate** 🗑️: Verschiebt identische Dateien in einen speziellen Papierkorbordner.
- **Flask-UI** 🌐: Eine einfache Web-Oberfläche zur Anzeige und Aktualisierung des Deduplizierungsstatus.
- **Live-Status** 🔁: Live-Updates über die Web-Oberfläche zur Überwachung der Fortschritte.

## Technologien 💻

- **Python** 🐍: Für das Backend und die Deduplizierungslogik.
- **Flask** 🌶️: Erstellt eine einfache Web-UI.
- **HTML/JavaScript** 📜: Frontend für die Darstellung und Interaktion mit dem Benutzer.

## Installation und Ausführung 🚀

Stellen Sie sicher, dass Sie Python und Flask auf Ihrem System installiert haben. Sie können Flask mit folgendem Befehl installieren:

```bash
pip install flask
```

Klonen Sie dieses Repository auf Ihren lokalen Computer:

```bash
git clone https://github.com/tilltmk/python-codes/deduplicate.git
cd deduplicate
```

Starten Sie die Anwendung mit:

```bash
python app.py
```

Öffnen Sie einen Webbrowser und navigieren Sie zu `http://127.0.0.1:5000/`, um die UI zu sehen.

## Lizenz 📄

Dieses Projekt ist unter der MIT Lizenz lizenziert - siehe die [LICENSE](LICENSE) Datei für Details.

## Beitrag 🤝

Beiträge sind willkommen! Für größere Änderungen, bitte zuerst ein Issue erstellen, um zu diskutieren, was Sie ändern möchten.

## Support 🆘

Bei Fragen oder Problemen, eröffnen Sie bitte ein Issue im [Issue-Tracker](https://github.com/tilltmk/python-codes/issues) dieses Repositories.

