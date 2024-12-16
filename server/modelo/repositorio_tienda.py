import modelo.conexion

# Operaciones con la base de datos de videojuegos retro

def obtener_videojuegos():
    conexion = modelo.conexion.conectar()
    sql = "SELECT * FROM videojuegos_retro ORDER BY id DESC"
    cur = conexion.cursor(dictionary=True)
    cur.execute(sql)
    videojuegos = cur.fetchall()
    cur.close()
    conexion.close()
    return videojuegos

def obtener_videojuegos_nuevos():
    conexion = modelo.conexion.conectar()
    sql = "SELECT * FROM videojuegos_retro WHERE estado = 'Nuevo Lanzamiento' ORDER BY id DESC"
    cur = conexion.cursor(dictionary=True)
    cur.execute(sql)
    videojuegos = cur.fetchall()
    cur.close()
    conexion.close()
    return videojuegos

def obtener_categorias():
    conexion = modelo.conexion.conectar()
    sql = "SELECT DISTINCT categoria FROM videojuegos_retro"
    cur = conexion.cursor(dictionary=True)
    cur.execute(sql)
    categorias = cur.fetchall()
    cur.close()
    conexion.close()
    return categorias

def borrar_videojuego(id):
    conexion = modelo.conexion.conectar()
    sql = "DELETE FROM videojuegos_retro WHERE id = %s"
    cur = conexion.cursor()
    cur.execute(sql, (id,))
    conexion.commit()
    cur.close()
    conexion.close()

def registrar_videojuego(titulo, precio, estado, compania, anio_lanzamiento, categoria):
    conexion = modelo.conexion.conectar()
    sql = """
    INSERT INTO videojuegos_retro (titulo, precio, estado, compania, anio_lanzamiento, categoria)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    cursor = conexion.cursor()
    cursor.execute(sql, (titulo, precio, estado, compania, anio_lanzamiento, categoria))
    conexion.commit()
    cursor.close()
    conexion.close()
    return cursor.lastrowid  # Devuelve el ID del último registro

def obtener_videojuego_por_id(id):
    conexion = modelo.conexion.conectar()
    cursor = conexion.cursor(dictionary=True)
    sql = "SELECT * FROM videojuegos_retro WHERE id = %s"
    cursor.execute(sql, (id,))
    videojuego = cursor.fetchone()
    cursor.close()
    conexion.close()
    return videojuego

def obtener_numero_videojuegos():
    conexion = modelo.conexion.conectar()
    sql = "SELECT COUNT(*) FROM videojuegos_retro"
    cursor = conexion.cursor()
    cursor.execute(sql)
    num_videojuegos = cursor.fetchone()[0]
    cursor.close()
    conexion.close()
    return num_videojuegos

def actualizar_videojuego(titulo, precio, estado, compania, anio_lanzamiento, categoria, id):
    conexion = modelo.conexion.conectar()
    cursor = conexion.cursor()
    sql = """
    UPDATE videojuegos_retro
    SET 
        titulo = %s,
        precio = %s,
        estado = %s,
        compania = %s,
        anio_lanzamiento = %s,
        categoria = %s
    WHERE id = %s
    """
    cursor.execute(sql, (titulo, precio, estado, compania, anio_lanzamiento, categoria, id))
    conexion.commit()
    cursor.close()
    conexion.close()

def obtener_pedidos():
    conexion = modelo.conexion.conectar()
    sql = "SELECT * FROM pedidos ORDER BY fecha_creacion DESC"
    cur = conexion.cursor(dictionary=True)
    cur.execute(sql)
    pedidos = cur.fetchall()
    
    # Obtener los detalles de cada pedido
    for pedido in pedidos:
        pedido['productos'] = obtener_detalles_pedido(pedido['id'])
    
    cur.close()
    conexion.close()
    return pedidos

def borrar_pedido(id):
    conexion = modelo.conexion.conectar()
    sql = "DELETE FROM pedidos WHERE id = %s"
    cur = conexion.cursor()
    cur.execute(sql, (id,))
    conexion.commit()
    cur.close()
    conexion.close()

def obtener_videojuegos_paginados(pagina, elementos_por_pagina):
    conexion = modelo.conexion.conectar()
    offset = (pagina - 1) * elementos_por_pagina
    sql = "SELECT * FROM videojuegos_retro ORDER BY id DESC LIMIT %s OFFSET %s"
    cur = conexion.cursor(dictionary=True)
    cur.execute(sql, (elementos_por_pagina, offset))
    videojuegos = cur.fetchall()
    cur.close()
    conexion.close()
    return videojuegos

# Funciones para el carrito de compras


def agregar_al_carrito(id_usuario, id_videojuego, cantidad):
    conexion = modelo.conexion.conectar()
    cur = conexion.cursor(dictionary=True)
    
    # Verificar si el item ya existe en el carrito
    sql_verificar = "SELECT * FROM carrito WHERE id_usuario = %s AND id_videojuego = %s"
    cur.execute(sql_verificar, (id_usuario, id_videojuego))
    item_existente = cur.fetchone()
    
    if item_existente:
        # Actualizar cantidad si ya existe
        sql_actualizar = "UPDATE carrito SET cantidad = cantidad + %s WHERE id_usuario = %s AND id_videojuego = %s"
        cur.execute(sql_actualizar, (cantidad, id_usuario, id_videojuego))
    else:
        # Insertar nuevo item
        sql_insertar = "INSERT INTO carrito (id_usuario, id_videojuego, cantidad) VALUES (%s, %s, %s)"
        cur.execute(sql_insertar, (id_usuario, id_videojuego, cantidad))
    
    conexion.commit()
    cur.close()
    conexion.close()
    return True

def obtener_carrito(id_usuario):
    conexion = modelo.conexion.conectar()
    cur = conexion.cursor(dictionary=True)
    
    sql = """
    SELECT c.*, v.titulo, v.precio 
    FROM carrito c 
    JOIN videojuegos_retro v ON c.id_videojuego = v.id 
    WHERE c.id_usuario = %s
    """
    cur.execute(sql, (id_usuario,))
    items_carrito = cur.fetchall()
    
    cur.close()
    conexion.close()
    return items_carrito

def actualizar_cantidad_carrito(id_usuario, id_videojuego, cantidad):
    conexion = modelo.conexion.conectar()
    cur = conexion.cursor()
    
    sql = "UPDATE carrito SET cantidad = %s WHERE id_usuario = %s AND id_videojuego = %s"
    cur.execute(sql, (cantidad, id_usuario, id_videojuego))
    
    conexion.commit()
    cur.close()
    conexion.close()
    return True

def eliminar_del_carrito(id_usuario, id_videojuego):
    conexion = modelo.conexion.conectar()
    cur = conexion.cursor()
    
    sql = "DELETE FROM carrito WHERE id_usuario = %s AND id_videojuego = %s"
    cur.execute(sql, (id_usuario, id_videojuego))
    
    conexion.commit()
    cur.close()
    conexion.close()
    return True

def vaciar_carrito(id_usuario):
    conexion = modelo.conexion.conectar()
    cur = conexion.cursor()
    
    sql = "DELETE FROM carrito WHERE id_usuario = %s"
    cur.execute(sql, (id_usuario,))
    
    conexion.commit()
    cur.close()
    conexion.close()
    return True

# Funciones para pedidos
def obtener_detalles_pedido(id_pedido):
    conexion = modelo.conexion.conectar()
    sql = """
        SELECT dp.*, v.titulo 
        FROM detalles_pedido dp
        JOIN videojuegos_retro v ON dp.id_videojuego = v.id
        WHERE dp.id_pedido = %s
    """
    cur = conexion.cursor(dictionary=True)
    cur.execute(sql, (id_pedido,))
    detalles = cur.fetchall()
    cur.close()
    conexion.close()
    return detalles

def crear_pedido(id_usuario, nombre, email, direccion, telefono, numero_tarjeta, total, ip_address=None, user_agent=None):
    conexion = modelo.conexion.conectar()
    try:
        # Iniciar transacción
        conexion.start_transaction()
        
        # Crear el pedido
        sql_pedido = """
        INSERT INTO pedidos (id_usuario, nombre, email, direccion, telefono, numero_tarjeta, total, ip_address, user_agent)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor = conexion.cursor()
        cursor.execute(sql_pedido, (id_usuario, nombre, email, direccion, telefono, numero_tarjeta, total, ip_address, user_agent))
        id_pedido = cursor.lastrowid
        
        # Obtener items del carrito
        sql_carrito = """
        SELECT c.id_videojuego, c.cantidad, v.precio
        FROM carrito c
        JOIN videojuegos_retro v ON c.id_videojuego = v.id
        WHERE c.id_usuario = %s
        """
        cursor.execute(sql_carrito, (id_usuario,))
        items_carrito = cursor.fetchall()
        
        # Insertar detalles del pedido
        sql_detalles = """
        INSERT INTO detalles_pedido (id_pedido, id_videojuego, cantidad, precio_unitario)
        VALUES (%s, %s, %s, %s)
        """
        for item in items_carrito:
            cursor.execute(sql_detalles, (id_pedido, item[0], item[1], item[2]))
        
        # Vaciar el carrito
        sql_vaciar = "DELETE FROM carrito WHERE id_usuario = %s"
        cursor.execute(sql_vaciar, (id_usuario,))
        
        # Confirmar transacción
        conexion.commit()
        return id_pedido
        
    except Exception as e:
        conexion.rollback()
        raise e
    finally:
        cursor.close()
        conexion.close()

def obtener_pedido(id_pedido):
    conexion = modelo.conexion.conectar()
    try:
        cursor = conexion.cursor(dictionary=True)
        
        # Obtener información del pedido
        sql_pedido = "SELECT * FROM pedidos WHERE id = %s"
        cursor.execute(sql_pedido, (id_pedido,))
        pedido = cursor.fetchone()
        
        if not pedido:
            return None
            
        # Obtener detalles del pedido
        sql_detalles = """
        SELECT dp.*, v.titulo, v.categoria 
        FROM detalles_pedido dp
        JOIN videojuegos_retro v ON dp.id_videojuego = v.id
        WHERE dp.id_pedido = %s
        """
        cursor.execute(sql_detalles, (id_pedido,))
        detalles = cursor.fetchall()
        
        pedido['detalles'] = detalles
        return pedido
        
    finally:
        cursor.close()
        conexion.close()

def obtener_pedidos_usuario(id_usuario):
    conexion = modelo.conexion.conectar()
    try:
        cursor = conexion.cursor(dictionary=True)
        sql = "SELECT * FROM pedidos WHERE id_usuario = %s ORDER BY fecha_creacion DESC"
        cursor.execute(sql, (id_usuario,))
        pedidos = cursor.fetchall()
        return pedidos
    finally:
        cursor.close()
        conexion.close()
