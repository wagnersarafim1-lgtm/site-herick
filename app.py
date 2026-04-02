from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    # O Flask procura automaticamente na pasta 'templates'
    return render_template('index.html')

if __name__ == '__main__':
    # rodando em modo debug para você ver o erro real no terminal
    app.run(debug=True)
