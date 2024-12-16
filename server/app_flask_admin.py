from flask import Flask
from flask import render_template
from flask import redirect 
from flask import url_for
from flask import request
import modelo.repositorio_tienda
import os

from __main__ import app
ruta_admin = "/admin"

@app.route(f"{ruta_admin}/")
def inicio_admin():
    return render_template("index-admin.html")

@app.route(f"{ruta_admin}/listar-videojuegos")
def listar_videojuegos():    
    return render_template("listar-videojuegos.html", videojuegos=modelo.repositorio_tienda.obtener_videojuegos())

@app.route(f"{ruta_admin}/borrar-videojuego/<int:id>")
def borrar_videojuego(id):
    print(f"id borrar: {id}")
    modelo.repositorio_tienda.borrar_videojuego(id)
    return redirect(url_for("listar_videojuegos"))

@app.route(f"{ruta_admin}/registrar-videojuego")
def registrar_videojuego():
    return render_template("registrar-videojuego.html")

@app.route(f"{ruta_admin}/guardar-nuevo-videojuego", methods=["POST"])
def guardar_nuevo_videojuego():
    titulo = request.form["titulo"]
    precio = request.form["precio"]
    estado = request.form["estado"]
    compania = request.form["compania"]
    anio_lanzamiento = request.form["anio_lanzamiento"]
    categoria = request.form["categoria"]
    
    # Registrar el videojuego primero
    id_generada = modelo.repositorio_tienda.registrar_videojuego(titulo, precio, estado, compania, anio_lanzamiento, categoria)
    
    # Guardar la imagen si se proporcionó una
    if 'imagen' in request.files and request.files['imagen'].filename != '':
        imagen = request.files['imagen']
        ruta_actual = os.path.dirname(__file__)
        ruta_imagen = os.path.join(ruta_actual, 'static', 'imagenes', f"{id_generada}.jpg")
        imagen.save(ruta_imagen)
    
    return redirect(url_for("listar_videojuegos"))

@app.route(f"{ruta_admin}/editar-videojuego/<int:id>")
def editar_videojuego(id):
    videojuego_a_editar = modelo.repositorio_tienda.obtener_videojuego_por_id(id)
    return render_template("editar-videojuego.html", videojuego=videojuego_a_editar)

@app.post(f"{ruta_admin}/guardar-cambios-videojuego")
def guardar_cambios_videojuego():
    titulo = request.form["titulo"]
    precio = request.form["precio"]
    estado = request.form["estado"]
    compania = request.form["compania"]
    anio_lanzamiento = request.form["anio_lanzamiento"]
    categoria = request.form["categoria"]
    id = request.form["id"]
    
    # Primero actualizamos los datos del videojuego
    modelo.repositorio_tienda.actualizar_videojuego(titulo, precio, estado, compania, anio_lanzamiento, categoria, id)
    
    # Luego manejamos la imagen si se proporcionó una nueva
    if 'imagen' in request.files and request.files['imagen'].filename != '':
        imagen = request.files['imagen']
        ruta_actual = os.path.dirname(__file__)
        ruta_imagen = os.path.join(ruta_actual, 'static', 'imagenes', f"{id}.jpg")
        if os.path.exists(ruta_imagen):
            os.remove(ruta_imagen)
        imagen.save(ruta_imagen)
    
    return redirect(url_for("listar_videojuegos"))

@app.route(f"{ruta_admin}/listar-pedidos")
def listar_pedidos():    
    return render_template("listar-pedidos.html", pedidos=modelo.repositorio_tienda.obtener_pedidos())

@app.route(f"{ruta_admin}/borrar-pedido/<int:id>")
def borrar_pedido(id):
    modelo.repositorio_tienda.borrar_pedido(id)
    return redirect(url_for("listar_pedidos"))
