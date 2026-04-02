from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    # O Flask vai carregar o index.html da pasta /templates
    # Certifique-se de que o arquivo se chama index.html
    return render_template('index.html')

if __name__ == '__main__':
    # debug=True permite que você veja os erros no navegador e reinicie o servidor automaticamente ao salvar
    app.run(debug=True)
