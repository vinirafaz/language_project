from fastapi import APIRouter
from bson import ObjectId
from schemas.teacher import teacherEntity, teacherEntityList
from config.db import connection


teacher = APIRouter()

@teacher.get('/teachers')
def get_teachers():
    return teacherEntityList(connection.teste.teacher.find())


