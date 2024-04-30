# GitHub Markdown Link Describer 📝

## Überblick 🌐

Dieses Python-Script automatisiert die Anreicherung von Markdown-Dateien mit Beschreibungen von GitHub Repositories. Es sucht nach GitHub-URLs in einer Markdown-Datei, ruft die entsprechenden Repository-Informationen über die GitHub API ab und fügt die Beschreibungen direkt in die Markdown-Datei ein. 🚀

## Funktionsweise 🔍

- Das Script liest eine Markdown-Datei und sucht nach allen GitHub Repository URLs.
- Für jede gefundene URL ruft das Script die GitHub API an, um die Repository-Beschreibung zu erhalten.
- Die Beschreibungen werden direkt nach dem entsprechenden Link in der Markdown-Datei eingefügt.

## Voraussetzungen 📋

Bevor Sie das Script verwenden, stellen Sie sicher, dass Sie die `requests` Bibliothek installiert haben. Diese kann mit folgendem Befehl installiert werden:

```bash
pip install requests
´´´

## Beispiel 📖

Angenommen, Ihre Markdown-Datei enthält den folgenden Link:

https://github.com/octocat/Hello-World

Nach der Ausführung des Scripts wird die Datei aktualisiert und sieht wie folgt aus:

```
https://github.com/octocat/Hello-World
> Das ist eine Beschreibung des octocat/Hello-World Repositories.
```

## Lizenz 📄

Dieses Projekt ist unter der MIT Lizenz lizenziert.

## Unterstützung 🤝

Falls Sie Unterstützung benötigen oder Verbesserungen vorschlagen möchten, eröffnen Sie bitte ein Issue in diesem Repository.
