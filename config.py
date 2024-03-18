import os
from dotenv import load_dotenv  # Instalar con pip install python-dotenv o pipenv install python-dotenv si se esta usando pipenv para en venv

load_dotenv()  # Carga todo el contenido de .env en variables de entorno (reduntante si usas pipenv)

class Config:
    DEBUG = True

    SECRECT_KEY = os.environ.get('SECRET_KEY') or 'LLAVE_SECRETA_PARA_DEV' # SECRECT_KEY para dar seguridad a formularios contra CSRF

    DATABASE_PATH = os.environ.get("DATABASE_PATH", "")  # Uri de la DB
    DB_TOKEN = os.environ.get("DB_TOKEN", "")  # Para Encriptar la DB
    ENCRYPT_DB = False

    TEMPLATE_FOLDER = "views/templates/"
    STATIC_FOLDER = "views/static/"
