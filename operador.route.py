from flask import request
from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import jsonify

#obtener todos los operadores
@app.route('/operadores', methods = ["GET"])
def get_operadores():
    if request.method == 'GET':
        operadores = Operador.objects()
        output = []
        for operador in operadores:
            output.append({'RUT' : operador['rut']
                        , 'NOMBRE' : operador['nombre']
                        , 'EMAIL' : operador['email']
                        , 'PRECIO' : operador['precio']
                        , 'ESTADO' : operador['estado']})
    return jsonify({'result' : output})

#agregar un nuevo operador
@app.route('/operadores/add', methods = ["POST"])
def add_maquinaria():
    if request.method == 'POST':
        operador = Operador()

        _json = request.json # obtenemos el json del cliente

        _rut = _json['rut']
        _nombre = _json['nombre']
        _email = _json['email']
        _precio = _json['precio']

        operador.rut = _rut
        operador.nombre = _nombre
        operador.email = _email
        operador.precio = _precio
        operador.estado = 'DISPONIBLE'

        operador.save()

        resp = jsonify('OPERADOR ADDED SUCCEFULLY')
        resp.status_code = 200
        return resp
    else:
        return not_found()

#obtener un solo operador por el rut
@app.route('/maquinarias/<string:_rut>', methods = ["GET"])
def get_one_maquinaria(_rut):
    if request.method == 'GET':
        operador = Operador.objects(rut = _rut).get()

        return jsonify({'rut' : operador.rut
                        ,'nombre' : operador.nobre
                        ,'email' : operador.email
                        ,'precio' : operador.precio
                        ,'estado' : cliente.estado})
    else:
        return not_found()

#actualizar un operador
@app.route('/maquinarias/<string:_rut>/edit', methods = ["POST"])
def update_maquinaria(_patente):
    if request.method == 'POST':

        _json = request.json.

        _nombre = _json['nombre']
        _email = _json['email']
        _precio = _json['precio']

        maquinaria = Maquinaria.objects(patente = _patente).update(
            set__nombre = _nombre,
            set__email = _email,
            set__precio = _precio
        )
        resp = jsonify('OPERADOR UPDATE SUCCEFULLY')
        resp.status_code = 200
        return resp
    
#dar de baja a un operador, no se elimina de la base de datos, solo se cambia el estado
@app.route('/maquinarias/<string:_rut>/delete', methods = ["get"])
def delete_maquinaria(_rut):
    if request.method == 'GET':
        operador = Operador.objects(rut = _rut).update(
            set__estado = "NO DISPONIBLE"
        )

        resp = jsonify('OPERADOR DELETE SUCCEFULLY')
        resp.status_code = 200
        return resp