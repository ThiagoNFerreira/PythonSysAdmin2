from config.db import db

def list_produtos():
    return list(db.produtos.find())
