import sys

legal_files = [
    "privacy-cashflowm.html", 
    "terms-cashflowm.html", 
    "privacy-tripease.html", 
    "terms-tripease.html", 
    "disclosure-tripease.html"
]

for file in legal_files:
    try:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if '<body class="legal-document-body">' not in content:
            content = content.replace('<body>', '<body class="legal-document-body">')
            
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
    except FileNotFoundError:
        pass

print("Added legal-document-body class to legal pages.")
