# Proyecto API Python - FastAPI

Aplicativo API desarrollado por kevin-sys para la gestión de operaciones con FastAPI, Docker y pruebas unitarias.

<p align="center">
<br>
<label><b>Sígueme en</b></label>
<br>
<a href="https://www.facebook.com/tu_perfil"><img src="https://icon-library.com/images/facebook-icon-25x25/facebook-icon-25x25-18.jpg" alt="Facebook" height=50></a>
<label><b></b></label>
<a href="https://www.instagram.com/tu_perfil"><img src="https://assets.stickpng.com/images/580b57fcd9996e24bc43c521.png" alt="Instagram" height=50></a>
<label><b></b></label>
<a href="https://www.linkedin.com/in/tu-perfil"><img src="https://1000logos.net/wp-content/uploads/2017/03/Linkedin-Logo.png" alt="LinkedIn" height=50></a>
<label><b></b></label>
<a href="https://api.whatsapp.com/send?phone=tu_numero"><img src="https://pngimg.com/uploads/whatsapp/whatsapp_PNG95147.png" alt="WhatsApp" height=50></a>
<h4>Invítame un café</h4>
<a href="https://paypal.me/tu_usuario?locale.x=es_XC"><img src="https://assets.stickpng.com/images/580b57fcd9996e24bc43c530.png" alt="PayPal" height=50></a>
</p>

## Descripción

Este es un proyecto de API desarrollado con FastAPI para la gestión de una pequeña biblioteca

## Estructura del Proyecto

La estructura básica del proyecto es la siguiente:

📁 proyecto
│
├── 📁 app               # Código principal de la aplicación
│   ├── __init__.py
│   ├── models.py        # Definición de modelos
│   ├── schemas.py        # Esquemas de Pydantic para serialización
│   └── database.py      # Configuración de la base de datos
|── 📁 routers
|   ├── __init__.py
|   |────books.py
├── 📁 tests             # Pruebas del proyecto
├── main.py              # Punto de entrada principal de la aplicación
├── requirements.txt     # Dependencias del proyecto
├── Dockerfile           # Configuración para Docker
└── README.md            # Documentación

