from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import api
from dotenv import load_dotenv

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=['*']
)

load_dotenv()

app.include_router(api.router)
