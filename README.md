# 🚀 **BIBLIOTECA FAST-API** 🚀

¡API REST utilizando FastAPI para gestionar una pequeña biblioteca. !

## 🛠 **TECNOLOGIAS**
- Python
-FastAPI
- Uvicorn (servidor ASGI)
- Docker
- SQLAlchemy (base de datos relacional)
---
## 🛠 **Instalación de herramientas necesarias**

- **Instalar Docker**
- **Instalar Python**
- **Clona el repositorio https://github.com/kevin-sys/biblioteca_api.git**


1. **Construye la imagen Docker**

   ```bash
   docker build -t biblioteca-api .

2. **Ejecuta el contenedor**

   ```bash
   docker run -p 8000:8000 biblioteca-api


3. **Accede a Swagger para cononocer los Endpoint**

   ```bash
   http://localhost:8000/docs

4. **Para ejecutar pruebas, asegúrate de tener pytest instalado. Luego, puedes ejecutar**

   ```bash
   pytest

