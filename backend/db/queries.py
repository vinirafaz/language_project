from config.db import connection

def find_one(query):
    return connection['test']['users'].find_one(query)