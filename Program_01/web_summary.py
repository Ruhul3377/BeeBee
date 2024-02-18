from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def get_page_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for any request errors

        soup = BeautifulSoup(response.text, 'html.parser')
        paragraphs = soup.find_all('p')  # Extract paragraphs

        # Summarize content (you can customize this part)
        summary = "\n".join([p.get_text() for p in paragraphs[:3]])

        return summary
    except requests.exceptions.RequestException as e:
        return f"Error fetching content: {e}"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        summary = get_page_content(url)
        return render_template('index.html', url=url, summary=summary)
    return render_template('index.html', url='', summary='')

if __name__ == '__main__':
    app.run(debug=True)
