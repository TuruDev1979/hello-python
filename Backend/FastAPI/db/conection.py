from pymongo import MongoClient

# BBDD Local
#db_conection = MongoClient().local

# BBDD Remota
db_conection = MongoClient("mongodb+srv://test:test@cluster0.ge6dnvo.mongodb.net/?retryWrites=true&w=majority").test




