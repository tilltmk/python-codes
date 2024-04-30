import requests
import re

inputter = input("Path to Markdown file:" )

# Pfad zur Markdown-Datei
file_path = inputter

# Lese die Inhalte der Markdown-Datei
with open(file_path, 'r') as file:
    content = file.read()

# Regex, um GitHub-Links zu finden
pattern = r'https://github\.com/([a-zA-Z0-9_-]+)/([a-zA-Z0-9_-]+)'

# Finde alle Vorkommen im Text
matches = re.finditer(pattern, content)

# Für jeden Link die GitHub API aufrufen und Beschreibung holen
for match in matches:
    user, repo = match.groups()
    api_url = f'https://api.github.com/repos/{user}/{repo}'
    response = requests.get(api_url)
    repo_data = response.json()
    description = repo_data.get('description', 'Keine Beschreibung verfügbar')

    # Füge die Beschreibung in den Text ein
    insert_position = match.end()
    content = content[:insert_position] + '\n> ' + description + '\n' + content[insert_position:] + '\n' + '\n'

# Speichere die modifizierte Markdown-Datei
with open(file_path, 'w') as file:
    file.write(content)
