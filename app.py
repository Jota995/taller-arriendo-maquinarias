from flask import Flask
from flask import request
from flask_pymongo import pymongo
from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import jsonify


app = Flask(__name__)
app.secret_key = "my_secret_key"
CONNECTION_STRING = "mongodb+srv://admin:123@tallers-eqakx.gcp.mongodb.net/test?retryWrites=true&w=majority"
client = pymongo.MongoClient(CONNECTION_STRING)

db = client.get_database('arriendo_maquinarias')
user = pymongo.collection.Collection(db, 'user')

@app.route("/test")
def test():
    db.user.insert_one({"name": "John"})
    return "Connected to the data base!"

if __name__ == '__main__':
    app.run(port = 3000,debug = True)