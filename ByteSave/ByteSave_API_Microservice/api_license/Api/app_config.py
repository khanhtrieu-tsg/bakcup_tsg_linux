from flask import Flask
from flask_pymongo import PyMongo

name_db = 'ByteSave_Licenses'
link_api_agent=''
link_api_mac=''

app = Flask(__name__)
app.config['MONGO_DBNAME'] = name_db
app.config['MONGO_URI'] = 'mongodb://localhost:27017/' + str(name_db)
mongo = PyMongo(app)


def get_mongo_db(name_db):
    app.config['MONGO_DBNAME'] = name_db
    app.config['MONGO_URI'] = 'mongodb://localhost:27017/' + str(name_db)
    mongo = PyMongo(app)
    return mongo
