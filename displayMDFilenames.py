from flask import Flask, render_template_string
import requests

app = Flask(__name__)

# Replace these with the repo owner and name
GITHUB_OWNER = "exploreGi"
GITHUB_REPO = "basics"

@app.route('/')
def list_md_files():
    # GitHub API URL to fetch the repository contents (root directory)
    url = f"https://api.github.com/repos/{GITHUB_OWNER}/{GITHUB_REPO}/contents/"
    
    response = requests.get(url)
    
    if response.status_code != 200:
        return f"Failed to fetch repository contents. Status code: {response.status_code}"
    
    data = response.json()

    # Filter Markdown (.md) files
    md_files = [item['name'] for item in data if item['name'].endswith('.md')]

    # Simple HTML rendering
    html = """
    <h1>Markdown Files in {{ repo }}</h1>
    <ul>
    {% for file in files %}
        <li>{{ file }}</li>
    {% endfor %}
    </ul>
    """
    
    return render_template_string(html, files=md_files, repo=GITHUB_REPO)


if __name__ == '__main__':
    app.run(debug=True)
