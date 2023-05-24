import os

SECRET = os.getenv('SECRET')
ALGORITHM = os.getenv('ALGORITHM')


GPT_SECRET = os.getenv('GPT_SECRET')


class Config:
    """Base config."""

    SECRET_KEY = SECRET
    ALGORITHM = ALGORITHM
