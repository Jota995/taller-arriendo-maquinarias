from flask import request
from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import jsonify

#obtener todas las ordenes de compra
@app.route('/ordencompras', methods = ["GET"])
def get_ordencompra():
    if request.method == 'GET':
        ordencompras = OrdenCompra.objects()
        output = []
        for ordencompra in ordencompras:
            output.append({'CLIENTE' : ordencompra['cliente']
                        , 'FECHA PEDIDO' : ordencompra['fecha_pedido']
                        , 'FECHA REQUERIDO' : ordencompra['fecha_requerido']
                        , 'TOTAL NETO' : ordencompra['total_neto']
                        , 'TOTAL' : ordencompra['total']
                        , 'OBSERVACION' : ordencompra['observacion']
                        , 'OPERADORES' : ordencompra['operadores']
                        , 'MAQUINARIAS' : ordencompra['maquinarias']
                        , 'OTROS' : ordencompra['otros']})
    return jsonify({'result' : output})


#agregar una nueva orden de compra
@app.route('/ordencompras/add', methods = ["POST"])
def add_ordencompra():
    if request.method == 'POST':
        ordencompra = OrdenCompra()

        _json = request.json # obtenemos el json desde del cliente

        _cliente = _json['cliente']
        _fecha_pedido = _json['fecha_pedido']
        _fecha_requerido = _json['fecha_requerido']
        _total_neto = _json['total_neto']
        _total= _json['total']
        _observacion = _json['observacion']
        _operadores = _json['operadores']
        _maquinarias = _json['maquinarias']
        _otros = _json['otros']


        ordencompra.cliente = _cliente
        ordencompra.fecha_pedido = _fecha_pedido
        ordencompra.fecha_requerido = _fecha_requerido
        ordencompra.total_neto = _total_neto
        ordencompra.total = _total
        ordencompra.observacion = _observacion
        ordencompra.operadores = _operadores
        ordencompra.maquinarias = _maquinarias
        ordencompra.otros = _otros
        ordencompra.estado = "sin procesar"

        ordencompra.save()

        resp = jsonify('ORDEN COMPRA ADDED SUCCEFULLY')
        resp.status_code = 200
        return resp
    else:
        return not_found()