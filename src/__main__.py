"""
Esta es una forma alternativa de iniciar la aplicación, con el comando:
   
    python -m src

Estando en la carpeta raiz (donde esta .env, config.py, run.py, requeriments.txt)
"""

from . import app

if __name__ == "__main__":
    app.run()  # No añadir parámetros, modificar directamente en Config