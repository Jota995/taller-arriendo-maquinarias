from flask import request
from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import jsonify

#obtener todas las maquinarias
@app.route('/arriendos', methods = ["GET"])
def get_maquinarias():
    if request.method == 'GET':
        arriendos = ArriendoMaquinaria.objects()
        output = []
        for arriendo in arriendos:
            output.append({'cliente' : maquinaria['cliente']
                        , 'fecha inicio' : maquinaria['fecha_inicio']
                        , 'fecha termino' : maquinaria['fecha_termino']
                        , 'estado' : maquinaria['estado']
                        , 'operadores' : maquinaria['operadores']
                        , 'maquinarias' : maquinaria['maquinarias']
                        ,'otros' : maquinaria['otros']})
    return jsonify({'result' : output})