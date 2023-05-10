from fastapi import APIRouter
from bson import ObjectId
import bcrypt
from models.customers import Customer
from schemas.customer import userEntity, userEntityList
from config.db import connection


customer = APIRouter()


@customer.get("/api/v1/customers")
def get_all_customers():
    return userEntityList(connection.teste.student.find())

@customer.get("/api/v1/customers/{customer_id}")
def get_customer_by_id(customer_id: str):
    return userEntity(connection.teste.student.find_one({"_id": ObjectId(customer_id)}))


@customer.post("/api/v1/customers")
def create_customer(customer: Customer):
    
    new_user = dict(customer)
    

    if user_validations(new_user["username"].strip()):
        return 


    else:
        del new_user["id"]
        new_user["password"] = bcrypt.hashpw(new_user["password"].strip().encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

        return str(connection.teste.student.insert_one(new_user).inserted_id)



# Auxiliar functions
# -----------User Validations----------------
def user_validations(user: str):
    if connection.teste.student.find_one({"username": user}):
        return {"error": "User already exists"}
    if len(user) >= 4:
        return {"error": "User must have at least 4 characters"}

# -----------Password Validations----------------
#regex de password


# -----------Email Validations----------------
#regex de email

