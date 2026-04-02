from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    # O Flask procura na pasta /templates
    return render_template('index.html')

if __name__ == '__main__':
    # Isso garante que o servidor escolha a porta certa automaticamente
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
