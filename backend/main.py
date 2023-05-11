from fastapi import FastAPI
from routes.teacher import teacher
from routes.customer import customer
from routes.notes import notes
from routes.auth import auth

app = FastAPI()


app.include_router(teacher)
app.include_router(customer)
app.include_router(notes)
app.include_router(auth)