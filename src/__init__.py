from flask import Flask, render_template, url_for
from config import Config
#from .database.contact_db import reset_table
#from .routes import global_scope, api_scope, errors_scope

app = Flask(__name__, static_folder=Config.STATIC_FOLDER, template_folder=Config.TEMPLATE_FOLDER)
app.config.from_object(Config)

from src import controllers, helpers, models, routes, tests, views

@app.route ('/')
def index():
	return render_template('index.html')

#app.register_blueprint(global_scope, url_prefix="/")
#app.register_blueprint(errors_scope, url_prefix="/")
#app.register_blueprint(api_scope, url_prefix="/api")

#reset_table()