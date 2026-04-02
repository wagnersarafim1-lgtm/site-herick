from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    # Usar a porta 5001 caso a 5000 esteja ocupada, isso evita conflitos
    app.run(debug=True, port=5001)
