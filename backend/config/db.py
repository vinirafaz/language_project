from pymongo import MongoClient
import redis

# MongoDB
connection = MongoClient("mongodb://172.17.0.2:27017/")

# Redis
redis_client = redis.Redis(host='172.17.0.3', port=6379, db=0)
