from config.db import db

def get_naves():
    return db.naves.find()

def criar_nave(nave):
    return db.naves.insert_one(nave)

def modificar_nave(oid, nave):
    return db.naves.update_one(
        oid,
        {"$set": nave}
    )