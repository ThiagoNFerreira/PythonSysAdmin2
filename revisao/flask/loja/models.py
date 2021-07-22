from bson.objectid import ObjectId
from config.db import db

def list_produtos():
    return list(db.produtos.find())

def get_produto(id):
    if isinstance(id, str):
        id = {"_id": ObjectId(id)}
    
    return db.produtos.find_one(id)