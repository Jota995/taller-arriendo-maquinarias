from flask import Flask
from flask import request
from flask_mongoengine import MongoEngine
from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import jsonify


app = Flask(__name__)
app.secret_key = "my_secret_key"
app.config['MONGODB_SETTINGS'] = {
    'db': 'arriendo-maquinarias',
    'host': '127.0.0.1',
    'port': 27017
}
db = MongoEngine(app)

class User(db.Document):
    username = db.StringField(unique = True, required = True)
    email = db.EmailField(unique = True)
    password = db.BinaryField()

class Maquinaria(db.Document):
    patente = db.StringField(unique = True, required = True)
    marca = db.StringField()
    modelo = db.StringField()
    estado = db.StringField()
    precio = db.IntField()
    tipo = db.StringField()

class Operador(db.Document):
    rut = db.StringField(unique = True, required = True)
    nombre = db.StringField()
    email = db.EmailField()
    precio = db.IntField()
    estado = db.StringField()

class Cliente(db.Document):
    rut = db.StringField(unique = True, required = True)
    nombre = db.StringField()
    email = db.EmailField()
    direccion = db.StringField
    estado = db.StringField()

class OrdenCompra(db.Document):
    cliente : db.ReferenceField(Cliente)
    fecha_pedido : db.DateTimeField()
    fecha_requerido : db.DateTimeField()
    total_neto : db.FloatField()
    total : db.FloatField()
    observacion : db.StringField()
    operadores : db.ListField()
    maquinarias: db.ListField()
    otros : db.ListField()

class ArriendoMaquinaria(db.Document):
    cliente : db.ReferenceField(Cliente)
    fecha_inicio : db.DateTimeField()
    fecha_termino : db.DateTimeField()
    estado : db.StringField()
    operadores : db.ListField()
    maquinarias: db.ListField()
    otros : db.ListField()

@app.route('/')
def default():
    return "web"

@app.route('/user/add', methods = ["POST"])
def user_create():
    if request.method == 'POST':
        _json = request.json
        _username = _json['username']
        _email = _json['email']
        _password = _json['password']
        
        id = mongo.db.user.insert({'username': _username, 'email': _email, 'password': _password})
        resp = jsonify('USER ADDED SUCCEFULLY')
        resp.status_code = 200
        return resp
    else:
        return not_found()

@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status' : 404,
        'message' : 'not found'
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp

@app.route('/test', methods = ["GET"])
def test():
    if request.method == 'GET':
        users = User.objects()
        output = []
        for user in users:
            output.append({'username' : user['username'], 'email' : user['email'], 'password' : user['password']})
    return jsonify({'result' : output})

#obtener todas las maquinarias
@app.route('/maquinarias', methods = ["GET"])
def get_maquinarias():
    if request.method == 'GET':
        maquinarias = Maquinaria.objects()
        output = []
        for maquinaria in maquinarias:
            output.append({'PATENTE' : maquinaria['patente']
                        , 'MARCA' : maquinaria['marca']
                        , 'MODELO' : maquinaria['modelo']
                        , 'TIPO' : maquinaria['tipo']
                        , 'PRECIO' : maquinaria['precio']
                        , 'ESTADO' : maquinaria['estado']})
        return jsonify({'result' : output})
    else:
        return not_found()

@app.route('/maquinarias/add', methods = ["POST"])
def add_maquinaria():
    if request.method == 'POST':
        maquinaria = Maquinaria()

        _json = request.json
        _patente = _json['patente']
        _marca = _json['marca']
        _modelo = _json['modelo']
        _tipo = _json['tipo']
        _precio = _json['precio']

        maquinaria.patente = _patente
        maquinaria.marca = _marca
        maquinaria.modelo = _modelo
        maquinaria.tipo = _tipo
        maquinaria.precio = _precio
        maquinaria.estado = 'DISPONIBLE'

        maquinaria.save()

        resp = jsonify('USER ADDED SUCCEFULLY')
        resp.status_code = 200
        return resp
    else:
        return not_found()

@app.route('/maquinarias/<string:_patente>', methods = ["GET"])
def get_one_maquinaria(_patente):
    if request.method == 'GET':
        maquinaria = Maquinaria.objects(patente = _patente).get()

        return jsonify({'patente' : maquinaria.patente
                        ,'precio' : maquinaria.precio
                        ,'estado' : maquinaria.estado})
    else:
        return not_found()

#actualizar una maquinaria
@app.route('/maquinarias/<string:_patente>/edit', methods = ["POST"])
def update_maquinaria(_patente):
    if request.method == 'POST':
        _json = request.json
        _marca = _json['marca']
        _modelo = _json['modelo']
        _tipo = _json['tipo']
        _precio = _json['precio']
        maquinaria = Maquinaria.objects(patente = _patente).update(
            set__marca = _marca,
            set__modelo = _modelo,
            set__tipo = _tipo,
            set__precio = _precio

        )
        resp = jsonify('MAQUINARIA UPDATE SUCCEFULLY')
        resp.status_code = 200
        return resp

if __name__ == '__main__':
    app.run(port = 3000,debug = True)