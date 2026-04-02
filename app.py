import os
from flask import Flask, render_template

# Configuração explícita de pastas para evitar erro no servidor Linux
app = Flask(__name__, 
            template_folder='templates', 
            static_folder='static',
            static_url_path='/static')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    # O Render exige que leiamos a porta da variável de ambiente PORT
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
