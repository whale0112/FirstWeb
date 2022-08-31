from flask import Flask, request, redirect
import random

app = Flask(__name__)

words = [
    {'id': 1, 'english': 'whale', 'korean': '고래'},
    {'id': 2, 'english': 'coding', 'korean': '코딩'}
]

@app.route('/')
def index():
    return f'''<!doctype html>
    <html>
        <body>
            <h1><a href="/">단어장</a></h1>
            <ol>
                <li><a href="/random/">random</a></li>
                <li><a href="/reads/">list</a></li>
                <li><a href="/create/">create</a></li>
            </ol>
            <h2>Whalecoding 단어장</h2>
            <pre>환영합니다.</pre>
        </body>
    </html>
    '''


app.run(debug=True)
