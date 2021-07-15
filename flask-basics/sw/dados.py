import pymongo

cliente = pymongo.MongoClient()

cabecalhos = {"Content-Type": "application/json"}

def setup():
    naves = [
        {"nome": "X-Wing"},
        {"nome": "Y-Wing"}
    ]

    personagens = [
        {"nome": "Lucas Andarilho dos Céus"},
        {"nome": "Léia dos Órgãos"}
    ]

    db = cliente["sw"]

    if db.naves.count() > 0:
        return
    
    db.naves.insert_many(naves)
    db.personagens.insert_many(personagens)

def naves():
    db = cliente.sw
    return db.naves.find()

def criar_nave(nave):
    db = cliente.sw
    return db.naves.insert_one(nave)

def modificar_nave(oid, nave):
    return cliente.sw.naves.update_one(
        oid,
        {"$set": nave}
    )
