from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Isso vai carregar o seu HTML que corrigimos abaixo
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
