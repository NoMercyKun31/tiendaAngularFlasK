from flask import Flask
from flask import render_template
from flask import redirect 
from flask import url_for
from flask import request
import modelo.repositorio_tienda
import os

app = Flask(__name__)

import app_flask_admin
import app_flask_rest

@app.route("/")
def inicio():
    return render_template("index.html")

# Configuración para desarrollo
app.config['DEBUG'] = True
app.run()
