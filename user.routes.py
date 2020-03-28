from flask import request
from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import jsonify

@app.route('/user/login', methods = ["GET"])
def login():

@app.route('/user/registrar', methods = ["POST"])
def registrar_usuario():
    if request.method == 'POST':
        user = User()

        _json = request.json
        _username = _json['username']
        _email = _json['email']
        _password = _json['password']

        maquinaria.username = _username
        maquinaria.email = _email
        maquinaria.password = _password

        user.save()

        resp = jsonify('USER ADDED SUCCEFULLY')
        resp.status_code = 200
        return resp
    else:
        return not_found()

@app.route('/user/<string:_username>/delete', methods = ["GET"])
def delete_usuario(_username):
    if request.method == 'GET':

        user = User.objects(username = _username).delete()

        resp = jsonify('USER DELETE SUCCEFULLY')
        resp.status_code = 200
        return resp