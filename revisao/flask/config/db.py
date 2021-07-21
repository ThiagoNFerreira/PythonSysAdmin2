import random
import pymongo

client = pymongo.MongoClient()
db = client.loja

def setup():
    produtos = [
        {"nome": "Headset", "preco": 279.90},
        {"nome": "RX 6700", "preco": 5899.00},
        {"nome": "Mouse Redragon", "preco": 119.90},
        {"nome": "Xbox S", "preco": 2519.90},
        {"nome": "Galaxy M12", "preco": 1709.05},
        {"nome": "Memoria XPG", "preco": 317.90},
        {"nome": "Monitor Gamer", "preco": 1499.90},
        {"nome": "Notebook Gamer", "preco": 5099.00},
        {"nome": "Teclado Gamer", "preco": 229.90}
    ]

    if db.produtos.count() > 0:
        return
    
    for produto in produtos:
        produto["estoque"] = random.randint(0, 99)

    db.produtos.insert_many(produtos)