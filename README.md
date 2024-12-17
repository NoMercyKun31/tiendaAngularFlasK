# E-commerce Angular + Flask

Este proyecto es una aplicación de comercio electrónico que utiliza Angular para el frontend y Flask para el backend. La aplicación permite a los usuarios navegar por productos, agregarlos al carrito y realizar pedidos.

## Tecnologías Utilizadas

### Frontend
- Angular (última versión)
- TailwindCSS para estilos
- TypeScript
- HTML5/CSS3

### Backend
- Flask (Python)
- SQL Database

## Requisitos Previos

- Node.js y npm
- Python 3.x
- XAMPP (para el servidor local)
- Angular CLI

## Configuración

1. **Frontend (Angular)**
   - El frontend se ejecuta en `http://localhost:4200`
   - Configurar las variables de entorno en `src/environments/`

2. **Backend (Flask)**
   - El backend se ejecuta en `http://localhost:5000`
   - Configurar las variables de entorno necesarias

## Ejecución del Proyecto

1. **Iniciar el backend**
   ```bash
   cd server
   python app_flask.py
   ```

2. **Iniciar el frontend**
   ```bash
   cd cliente
   ng serve 
   ```

## Características

- Catálogo de productos
- Carrito de compras
- Gestión de pedidos
- Sistema de autenticación
- Interfaz de usuario responsive
- Para entrar al Panel de Administración desde el Cliente la Contraseña es admin123
