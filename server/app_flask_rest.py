from flask import jsonify, request, session 
import modelo.repositorio_tienda
from __main__ import app

ruta_servicio_rest = "/rest/"

@app.route(ruta_servicio_rest)
def inicio_rest():
    return "Servicio rest operativos"

@app.route(ruta_servicio_rest + "obtener_videojuegos")
def obtener_videojuegos():
    videojuegos = modelo.repositorio_tienda.obtener_videojuegos()
    return jsonify(videojuegos)

@app.route(ruta_servicio_rest + "obtener_videojuegos_nuevos")
def obtener_videojuegos_nuevos():
    videojuegos = modelo.repositorio_tienda.obtener_videojuegos_nuevos()
    return jsonify(videojuegos)

@app.route(ruta_servicio_rest + "obtener_videojuego_por_id")
def obtener_videojuego_por_id():
    id = request.args.get("id")
    videojuego = modelo.repositorio_tienda.obtener_videojuego_por_id(id)
    return jsonify(videojuego)

@app.route(ruta_servicio_rest + "obtener_categorias")
def obtener_categorias():
    categorias = modelo.repositorio_tienda.obtener_categorias()
    return jsonify(categorias)

@app.route(ruta_servicio_rest + "obtener_videojuegos_paginados")
def obtener_videojuegos_paginados():
    pagina = int(request.args.get("pagina", 1))
    elementos_por_pagina = int(request.args.get("elementos_por_pagina", 9))
    
    videojuegos = modelo.repositorio_tienda.obtener_videojuegos_paginados(pagina, elementos_por_pagina)
    total_videojuegos = modelo.repositorio_tienda.obtener_numero_videojuegos()
    
    respuesta = {
        "videojuegos": videojuegos,
        "total": total_videojuegos,
        "paginas_totales": (total_videojuegos + elementos_por_pagina - 1) // elementos_por_pagina
    }
    
    return jsonify(respuesta)

# Endpoints del carrito de compras
@app.route(ruta_servicio_rest + "carrito/agregar", methods=['POST'])
def agregar_al_carrito():
    datos = request.get_json()
    id_videojuego = datos.get('id_videojuego')
    cantidad = datos.get('cantidad', 1)
    id_usuario = 1  # Por ahora usaremos un ID de usuario fijo hasta implementar autenticación
    
    try:
        modelo.repositorio_tienda.agregar_al_carrito(id_usuario, id_videojuego, cantidad)
        items_carrito = modelo.repositorio_tienda.obtener_carrito(id_usuario)
        return jsonify({'mensaje': 'Producto agregado al carrito', 'carrito': items_carrito})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route(ruta_servicio_rest + "carrito/obtener", methods=['GET'])
def obtener_carrito():
    id_usuario = 1  # Por ahora usaremos un ID de usuario fijo hasta implementar autenticación
    try:
        items_carrito = modelo.repositorio_tienda.obtener_carrito(id_usuario)
        return jsonify(items_carrito)
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route(ruta_servicio_rest + "carrito/actualizar", methods=['PUT'])
def actualizar_carrito():
    datos = request.get_json()
    id_videojuego = datos.get('id_videojuego')
    cantidad = datos.get('cantidad')
    id_usuario = 1  # Por ahora usaremos un ID de usuario fijo hasta implementar autenticación
    
    try:
        modelo.repositorio_tienda.actualizar_cantidad_carrito(id_usuario, id_videojuego, cantidad)
        items_carrito = modelo.repositorio_tienda.obtener_carrito(id_usuario)
        return jsonify({'mensaje': 'Carrito actualizado', 'carrito': items_carrito})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route(ruta_servicio_rest + "carrito/eliminar/<int:id_videojuego>", methods=['DELETE'])
def eliminar_del_carrito(id_videojuego):
    id_usuario = 1  # Por ahora usaremos un ID de usuario fijo hasta implementar autenticación
    try:
        modelo.repositorio_tienda.eliminar_del_carrito(id_usuario, id_videojuego)
        items_carrito = modelo.repositorio_tienda.obtener_carrito(id_usuario)
        return jsonify({'mensaje': 'Producto eliminado del carrito', 'carrito': items_carrito})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route(ruta_servicio_rest + "carrito/vaciar", methods=['DELETE'])
def vaciar_carrito():
    id_usuario = 1  # Por ahora usaremos un ID de usuario fijo hasta implementar autenticación
    try:
        modelo.repositorio_tienda.vaciar_carrito(id_usuario)
        return jsonify({'mensaje': 'Carrito vaciado'})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route(ruta_servicio_rest + "obtener_numero_videojuegos")
def obtener_numero_videojuegos():
    num_videojuegos = modelo.repositorio_tienda.obtener_numero_videojuegos()
    return jsonify(num_videojuegos)

# Endpoints de pedidos
@app.route(ruta_servicio_rest + "pedidos/crear", methods=['POST'])
def crear_pedido():
    try:
        datos = request.get_json()
        id_usuario = 1  # Por ahora usamos ID fijo hasta implementar autenticación
        
        # Validar datos requeridos
        campos_requeridos = ['nombre', 'email', 'direccion', 'telefono', 'numero_tarjeta']
        for campo in campos_requeridos:
            if campo not in datos:
                return jsonify({'error': f'Falta el campo {campo}'}), 400
        
        # Obtener el total del carrito
        items_carrito = modelo.repositorio_tienda.obtener_carrito(id_usuario)
        total = sum(item['precio'] * item['cantidad'] for item in items_carrito)
        
        if not items_carrito:
            return jsonify({'error': 'El carrito está vacío'}), 400
            
        # Obtener IP y User-Agent
        ip_address = request.remote_addr
        user_agent = request.headers.get('User-Agent')
            
        # Crear el pedido
        id_pedido = modelo.repositorio_tienda.crear_pedido(
            id_usuario=id_usuario,
            nombre=datos['nombre'],
            email=datos['email'],
            direccion=datos['direccion'],
            telefono=datos['telefono'],
            numero_tarjeta=datos['numero_tarjeta'],
            total=total,
            ip_address=ip_address,
            user_agent=user_agent
        )
        
        # Obtener el pedido creado
        pedido = modelo.repositorio_tienda.obtener_pedido(id_pedido)
        return jsonify({
            'mensaje': 'Pedido creado exitosamente',
            'pedido': pedido
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route(ruta_servicio_rest + "pedidos/usuario", methods=['GET'])
def obtener_pedidos_usuario():
    try:
        id_usuario = 1  # Por ahora usamos ID fijo hasta implementar autenticación
        pedidos = modelo.repositorio_tienda.obtener_pedidos_usuario(id_usuario)
        return jsonify(pedidos)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route(ruta_servicio_rest + "pedidos/<int:id_pedido>", methods=['GET'])
def obtener_pedido(id_pedido):
    try:
        pedido = modelo.repositorio_tienda.obtener_pedido(id_pedido)
        if not pedido:
            return jsonify({'error': 'Pedido no encontrado'}), 404
        return jsonify(pedido)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

from flask import Flask, jsonify, request
import modelo  # Tu módulo para manejar la base de datos

app = Flask(__name__)

@app.route('/rest/obtener_videojuegos_paginados', methods=['GET'])
def obtener_videojuegos_paginados():
    page = int(request.args.get('page', 1))  # Página actual
    size = int(request.args.get('size', 9))  # Tamaño de página
    offset = (page - 1) * size  # Calcular el desplazamiento

    conexion = modelo.conexion.conectar()
    cursor = conexion.cursor(dictionary=True)

    # Obtener videojuegos paginados
    sql = "SELECT * FROM videojuegos_retro ORDER BY id DESC LIMIT %s OFFSET %s"
    cursor.execute(sql, (size, offset))
    videojuegos = cursor.fetchall()

    # Obtener el número total de videojuegos
    sql_total = "SELECT COUNT(*) as total FROM videojuegos_retro"
    cursor.execute(sql_total)
    total = cursor.fetchone()['total']

    cursor.close()
    conexion.close()

    return jsonify({
        "videojuegos": videojuegos,
        "totalElements": total,
        "pageSize": size,
        "currentPage": page,
        "totalPages": (total + size - 1) // size 
    })

if __name__ == '__main__':
    app.run(debug=True)