from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import api

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow__origins=["http://localhost:3000"],
    allow_methods=["*"]
)



app.include_router(api.router)
