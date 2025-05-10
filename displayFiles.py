import os
from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    # Get the current directory
    current_directory = os.getcwd()
    md_files_content = []

    # Loop through all files in the current directory
    for filename in os.listdir(current_directory):
        # Check if the file has a .md extension
        if filename.endswith('.md'):
            # Construct the full file path
            file_path = os.path.join(current_directory, filename)
            
            # Open and read the file
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                md_files_content.append((filename, content))

    # Render the content in a simple HTML template
    html_template = '''
    <!doctype html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Markdown Files</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; }
            h2 { color: #333; }
            pre { background: #f4f4f4; padding: 10px; border-radius: 5px; }
        </style>
    </head>
    <body>
        <h1>Contents of Markdown Files</h1>
        {% for filename, content in md_files_content %}
            <h2>{{ filename }}</h2>
            <pre>{{ content }}</pre>
        {% endfor %}
    </body>
    </html>
    '''

    return render_template_string(html_template, md_files_content=md_files_content)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

