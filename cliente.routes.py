from flask import request
from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import jsonify

#obtener todos los trabajadores
@app.route('/clientes', methods = ["GET"])
def get_clientes():
    if request.method == 'GET':
        clientes = Cliente.objects()
        output = []
        for cliente in clientes:
            output.append({'RUT' : cliente['rut']
                        , 'NOMBRE' : cliente['nombre']
                        , 'EMAIL' : cliente['email']
                        , 'DIRECCION' : cliente['direccion']
                        , 'ESTADO' : cliente['estado']})
    return jsonify({'result' : output})

#agregar un nuevo cliente
@app.route('/clientes/add', methods = ["POST"])
def add_cliente():
    if request.method == 'POST':
        cliente = Cliente()

        _json = request.json # obtenemos el json desde del cliente

        _rut = _json['rut']
        _nombre = _json['nombre']
        _email = _json['email']
        _direccion = _json['direccion']

        cliente.rut = _rut
        cliente.nombre = _nombre
        cliente.email = _email
        cliente.direccion = _direccion
        cliente.estado = 'DISPONIBLE'

        cliente.save()

        resp = jsonify('CLIENTE ADDED SUCCEFULLY')
        resp.status_code = 200
        return resp
    else:
        return not_found()

#obtener un solo cliente por el rut
@app.route('/clientes/<string:_rut>', methods = ["GET"])
def get_one_maquinaria(_rut):
    if request.method == 'GET':
        cliente = Cliente.objects(rut = _rut).get()

        return jsonify({'rut' : cliente.rut
                        ,'nombre' : cliente.nobre
                        ,'email' : cliente.email
                        ,'direccion' : cliente.direccion
                        ,'estado' : cliente.estado})
    else:
        return not_found()

#actualizar un cliente
@app.route('/clientes/<string:_rut>/edit', methods = ["POST"])
def update_maquinaria(_patente):
    if request.method == 'POST':

        _json = request.json.

        _nombre = _json['nombre']
        _email = _json['email']
        _direccion = _json['direccion']

        maquinaria = Maquinaria.objects(patente = _patente).update(
            set__nombre = _nombre,
            set__email = _email,
            set__direccion = _direccion
        )
        resp = jsonify('CLIENTE UPDATE SUCCEFULLY')
        resp.status_code = 200
        return resp
    
#dar de baja a un cliente, no se elimina de la base de datos, solo se cambia el estado
@app.route('/clientes/<string:_rut>/delete', methods = ["get"])
def delete_maquinaria(_rut):
    if request.method == 'GET':
        cliente = Cliente.objects(rut = _rut).update(
            set__estado = "NO DISPONIBLE"
        )

        resp = jsonify('CLIENTE DELETE SUCCEFULLY')
        resp.status_code = 200
        return resp