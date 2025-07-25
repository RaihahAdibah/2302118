from flask import Flask, request, render_template_string

app = Flask(__name__)

# HTML template with search form
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Hello World with Search</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; }
        .search-box { margin: 20px 0; }
        .result { margin-top: 20px; padding: 10px; border: 1px solid #ddd; }
    </style>
</head>
<body>
    <h1>Hello World!</h1>
    
    <div class="search-box">
        <form method="GET" action="/search">
            <input type="text" name="query" placeholder="Search something..." required>
            <button type="submit">Search</button>
        </form>
    </div>

    {% if result %}
    <div class="result">
        <strong>You searched for:</strong> {{ result }}
    </div>
    {% endif %}
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route('/search')
def search():
    query = request.args.get('query', '')
    return render_template_string(HTML_TEMPLATE, result=query)

if __name__ == '__main__':
    app.run(host='127.0.0.0', port=5000)
