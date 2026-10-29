from blueprints.alumnos.routes import alumnos_bp
from blueprints.maestros.routes import maestros_bp
from config import config
from flask import Blueprint, Flask, jsonify, request
from flask_cors import CORS
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config.from_object(config['development'])

CORS(app)
con = MySQL(app)

app.register_blueprint(alumnos_bp)
app.register_blueprint(maestros_bp)


def pagina_no_encontrada(error):
    return "<h1>Pagina_no_encontrada</h1>", 404


# Registrar el manejador de errores a nivel global
app.register_error_handler(404, pagina_no_encontrada)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)