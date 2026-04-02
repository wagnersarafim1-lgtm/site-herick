import os
from flask import Flask, render_template

# Forçamos o Flask a reconhecer as pastas de templates e arquivos estáticos
app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    # O Render exige que usemos a porta fornecida pela variável de ambiente PORT
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
