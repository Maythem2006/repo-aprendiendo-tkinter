# DEBES DE INSTALAR FLASK CON: "pip install flask" DESDE LA TERMINAL
from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return "<h1>Inicio</1>"

@app.route("/youtube")
def youtube():
    return '<>'

app.run(debug=True)