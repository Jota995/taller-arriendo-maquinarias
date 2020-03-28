from flask import request
from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import jsonify

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

#agregar una nueva maquinaria
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
        
        resp = jsonify('MAQUINARIA ADDED SUCCEFULLY')
        resp.status_code = 200
        return resp
    else:
        return not_found()

#obtener una sola maquinaria por la patente
@app.route('/maquinarias/<string:_patente>', methods = ["GET"])
def get_one_maquinaria(_patente):
    if request.method == 'GET':
        maquinaria = Maquinaria.objects(patente = _patente).get()

        return jsonify({'patente' : maquinaria.patente
                        ,'marca' : maquinaria.marca
                        ,'modelo' : maquinaria.modelo
                        ,'tipo' : maquinaria.tipo
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

#dar de baja una maquinaria, no se elimina de la base de datos, solo se cambia el estado
@app.route('/maquinarias/<string:_patente>/delete', methods = ["get"])
def delete_maquinaria(_patente):
    if request.method == 'GET':
        maquinaria = Maquinaria.objects(patente = _patente).update(
            set__estado = "NO DISPONIBLE"
        )
        resp = jsonify('MAQUINARIA DELETE SUCCEFULLY')
        resp.status_code = 200
        return resp
        