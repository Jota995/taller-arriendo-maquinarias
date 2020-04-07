from flask import Flask
from flask import request
from flask_pymongo import pymongo
from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
app.secret_key = "my_secret_key"

#clase padre que contiene los datos de conexion
class Conexion():
    def __init__(self):
        self.CONNECTION_STRING = "mongodb+srv://admin:123@tallers-eqakx.gcp.mongodb.net/test?retryWrites=true&w=majority"
        self.client = pymongo.MongoClient(self.CONNECTION_STRING)
        self.db = self.client.get_database('arriendo_maquinarias')
        
class Maquinaria(Conexion):
    def __init__(self):
        Conexion.__init__(self) # inicializa el constructor del padre para obtener los datos de la conexion
        self.collection_name = pymongo.collection.Collection(self.db, __class__.__name__.lower()) # obtenemos la coleccion haciendo referencia al nombre de la clase
        self.collection_name.create_index([("patente", pymongo.ASCENDING)], unique=True) # declaramos PATENTE como clave unica
    
    def findAll(self):
        maquinarias = self.collection_name.find()
        output = []
        for maquinaria in maquinarias:
            output.append({ 'MARCA' : maquinaria['marca'],
                            'MODELO' : maquinaria['modelo'],
                            'TIPO' : maquinaria['tipo'],
                            'PRECIO' : maquinaria['precio'],
                            'ESTADO' : maquinaria['estado'],
                            'PATENTE' : maquinaria['patente']})

        return jsonify({'result' : output})
    
    def findOne(self, _patente):
        maquinaria = self.collection_name.find_one({'patente' : _patente})

        return jsonify({'MARCA' : maquinaria['marca'],
                        'MODELO' : maquinaria['modelo'],
                        'TIPO' : maquinaria['tipo'],
                        'PRECIO' : maquinaria['precio'],
                        'ESTADO' : maquinaria['estado'],
                        'PATENTE' : maquinaria['patente']})

    def create_one(self,request):
        patente = request['patente']
        marca = request['marca']
        modelo = request['modelo']
        tipo = request['tipo']
        precio = request['precio']

        return self.collection_name.insert_one({'patente' : patente
                                                ,'marca' : marca
                                                ,'modelo' : modelo
                                                ,'tipo' : tipo
                                                ,'precio' : precio
                                                ,'estado' : 'DISPONIBLE'})
    
    def update_one(self,patente,request):
        marca = request['marca']
        modelo = request['modelo']
        tipo = request['tipo']
        precio = request['precio']
        return self.collection_name.update_one(
            {'patente' : patente},
            {
                '$set':{
                    'marca' : marca,
                    'modelo' : modelo,
                    'tipo' : tipo,
                    'precio' : precio
                }
            }
        )
    
    def update_en_arriendo(self,patente):
        return self.collection_name.update_one(
            {'patente' : patente},
            {
                '$set':{
                    'estado' : 'EN ARRIENDO',
                }
            }
        )

    def delete(self,patente):
        return self.collection_name.update_one(
            {'patente' : patente},
            {
                '$set':{
                    'estado' : 'NO DISPONIBLE',
                }
            }
        )

class Operador(Conexion):
    def __init__(self):
        Conexion.__init__(self) # inicializa el constructor del padre para obtener los datos de la conexion
        self.collection_name = pymongo.collection.Collection(self.db, __class__.__name__.lower()) # obtenemos la coleccion haciendo referencia al nombre de la clase
        self.collection_name.create_index([("rut", pymongo.ASCENDING)], unique=True) # declaramos RUT como clave unica
    
    def findAll(self):
        operadores = self.collection_name.find()
        output = []
        for operador in operadores:
            output.append({'RUT' : operador['rut'],
                            'NOMBRE' : operador['nombre'],
                            'EMAIL' : operador['email'],
                            'PRECIO' : operador['precio'],
                            'ESTADO' : operador['estado']})

        return jsonify({'result' : output})
    
    def findOne(self, _rut):
        operador = self.collection_name.find_one({'rut' : _rut})

        return jsonify({'RUT' : operador['rut'],
                        'NOMBRE' : operador['nombre'],
                        'EMAIL' : operador['email'],
                        'PRECIO' : operador['precio'],
                        'ESTADO' : operador['estado']})

    def create_one(self,request):
        rut = request['rut']
        nombre = request['nombre']
        email = request['email']
        precio = request['precio']

        return self.collection_name.insert_one({'rut' : rut
                                                ,'nombre' : nombre
                                                ,'email' : email
                                                ,'precio' : precio
                                                ,'estado' : 'DISPONIBLE'})
    
    def update_one(self,rut,request):
        nombre = request['nombre']
        email = request['email']
        precio = request['precio']
        return self.collection_name.update_one(
            {'rut' : rut},
            {
                '$set':{
                    'nombre' : nombre,
                    'email' : email,
                    'precio' : precio
                }
            }
        )
    
    def update_en_arriendo(self,rut):
        return self.collection_name.update_one(
            {'rut' : rut},
            {
                '$set':{
                    'estado' : 'EN ARRIENDO',
                }
            }
        )

    def delete(self,rut):
        return self.collection_name.update_one(
            {'rut' : rut},
            {
                '$set':{
                    'estado' : 'NO DISPONIBLE',
                }
            }
        )

class Cliente(Conexion):
    def __init__(self):
        Conexion.__init__(self) # inicializa el constructor del padre para obtener los datos de la conexion
        self.collection_name = pymongo.collection.Collection(self.db, __class__.__name__.lower()) # obtenemos la coleccion haciendo referencia al nombre de la clase
        self.collection_name.create_index([("rut", pymongo.ASCENDING)], unique=True) # declaramos RUT como clave unica
    
    def findAll(self):
        clientes = self.collection_name.find()
        output = []
        for cliente in clientes:
            output.append({'RUT' : cliente['rut'],
                            'NOMBRE' : cliente['nombre'],
                            'EMAIL' : cliente['email'],
                            'DIRECCION' : cliente['direccion'],
                            'ESTADO' : cliente['estado']})

        return jsonify({'result' : output})
    
    def findOne(self, _rut):
        operador = self.collection_name.find_one({'rut' : _rut})

        return jsonify({'RUT' : cliente['rut'],
                        'NOMBRE' : cliente['nombre'],
                        'EMAIL' : cliente['email'],
                        'DIRECCION' : cliente['direccion'],
                        'ESTADO' : cliente['estado']})

    def create_one(self,request):
        rut = request['rut']
        nombre = request['nombre']
        email = request['email']
        direccion = request['direccion']

        return self.collection_name.insert_one({'rut' : rut
                                                ,'nombre' : nombre
                                                ,'email' : email
                                                ,'direccion' : direccion
                                                ,'estado' : 'DISPONIBLE'})
    
    def update_one(self,rut,request):
        nombre = request['nombre']
        email = request['email']
        direccion = request['direccion']

        return self.collection_name.update_one(
            {'rut' : rut},
            {
                '$set':{
                    'nombre' : nombre,
                    'email' : email,
                    'direccion' : direccion
                }
            }
        )
    
    def delete(self,rut):
        return self.collection_name.update_one(
            {'rut' : rut},
            {
                '$set':{
                    'estado' : 'NO DISPONIBLE',
                }
            }
        )

class Arriendo(Conexion):
    def __init__(self):
        Conexion.__init__(self) # inicializa el constructor del padre para obtener los datos de la conexion
        self.collection_name = pymongo.collection.Collection(self.db, __class__.__name__.lower()) # obtenemos la coleccion haciendo referencia al nombre de la clase
    
    def findAll(self):
        arriendos = self.collection_name.find()
        output = []
        for arriendo in arriendos:
            output.append({'FECHAINICIO' : arriendo['fecha inicio'],
                            'FECHATERMINO' : arriendo['fecha termino'],
                            'CLIENTE' : arriendo['cliente'],
                            'ESTADO' : arriendo['estado'],
                            'OPERADORES' : arriendo['operadores'],
                            'MAQUINARIAS' : arriendo['maquinarias'],
                            'ID' : str(arriendo['_id'])})

        return jsonify({'result' : output})

    def findOne(self, id):
        arriendo = self.collection_name.find_one({'_id': ObjectId(id)})

        return jsonify({'FECHAINICIO' : arriendo['fecha inicio'],
                        'FECHATERMINO' : arriendo['fecha termino'],
                        'CLIENTE' : arriendo['cliente'],
                        'MAQUINARIAS' : arriendo['maquinarias'],
                        'OPERADORES' : arriendo['operadores'],
                        'ESTADO' : arriendo['estado'],
                        'ID' : str(arriendo['_id'])})
    
    def create_one(self,request):
        fecha_inicio = request['fecha inicio']
        fecha_termino = request['fecha termino']
        cliente = request['cliente']
        maquinarias = request['maquinarias']
        operadores = request['operadores']

        return self.collection_name.insert_one({'fecha inicio' : fecha_inicio
                                                ,'fecha termino' : fecha_termino
                                                ,'cliente' : cliente
                                                ,'maquinarias' : maquinarias
                                                ,'operadores' : operadores
                                                ,'estado' : 'EN ARRIENDO'})

@app.route('/arriendos/add', methods = ["POST"])
def add_arriendos():
    if request.method == 'POST':
        _json = request.json

        _arriendo = Arriendo()
        _maquinaria = Maquinaria()
        _operador = Operador()

        maquinarias = _json['maquinarias']
        operadores = _json['operadores']

        for maquinaria in maquinarias :
            _maquinaria.update_en_arriendo(maquinaria)
        
        for operador in operadores:
            _operador.update_en_arriendo(operador)

        _arriendo.create_one(_json)

        resp = jsonify('ARRIENDO ADDED SUCCEFULLY')
        resp.status_code = 200
        return resp

@app.route('/arriendos/<string:id>', methods = ["GET"])
def findOne_arriendo(id):
    if request.method == 'GET':
        return Arriendo().findOne(id)

@app.route('/arriendos', methods = ["GET"])
def findAll_arriendos():
    if request.method == 'GET':
        return Arriendo().findAll()

@app.route('/maquinarias', methods = ["GET"])
def findAll_maquinarias():
    if request.method == 'GET':
        return Maquinaria().findAll()

@app.route('/maquinarias/<string:_patente>', methods = ["GET"])
def findOne_maquinaria(_patente):
    if request.method == 'GET':
        return Maquinaria().findOne(_patente)

@app.route('/maquinarias/create', methods = ["POST"])
def add_maquinaria():
    if request.method == 'POST':
        _json = request.json

        Maquinaria().create_one(_json)
        
        resp = jsonify('MAQUINARIA ADDED SUCCEFULLY')
        resp.status_code = 200
        return resp

@app.route('/maquinarias/<string:patente>/update', methods = ["POST"])
def update_maquinaria(patente):
    if request.method == 'POST':
        _json = request.json

        maquinaria = Maquinaria().update_one(patente,_json)
        
        resp = jsonify('MAQUINARIA UPDATE SUCCEFULLY')
        resp.status_code = 200
        return resp

@app.route('/maquinarias/<string:patente>/delete', methods = ["GET"])
def delete_maquinaria(patente):
    if request.method == 'GET':

        maquinaria = Maquinaria().delete(patente)
        
        resp = jsonify('MAQUINARIA DELETE SUCCEFULLY')
        resp.status_code = 200
        return resp

@app.route('/clientes/create', methods = ["POST"])
def add_cliente():
    if request.method == 'POST':
        _json = request.json

        Cliente().create_one(_json)
        
        resp = jsonify('CLIENTE ADDED SUCCEFULLY')
        resp.status_code = 200
        return resp

@app.route('/clientes', methods = ["GET"])
def findAll_cliente():
    if request.method == 'GET':
        return Cliente().findAll()

@app.route('/operadores/create', methods = ["POST"])
def add_operador():
    if request.method == 'POST':
        _json = request.json

        Operador().create_one(_json)
        
        resp = jsonify('OPERADOR ADDED SUCCEFULLY')
        resp.status_code = 200
        return resp

@app.route('/operadores', methods = ["GET"])
def findAll_operadores():
    if request.method == 'GET':
        return Operador().findAll()

@app.route('/operadores/<string:_rut>/update', methods = ["POST"])
def update_operadores(_rut):
    if request.method == 'POST':
        _json = request.json

        operador = Operador().update_one(_rut,_json)
        
        resp = jsonify('OPERADOR UPDATE SUCCEFULLY')
        resp.status_code = 200
        return resp

@app.route('/operadores/<string:_rut>/delete', methods = ["GET"])
def delete_operador(_rut):
    if request.method == 'GET':

        operador = Operador().delete(_rut)
        
        resp = jsonify('OPERADOR DELETE SUCCEFULLY')
        resp.status_code = 200
        return resp

if __name__ == '__main__':
    app.run(port = 3000,debug = True)