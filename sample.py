import sqlalchemy
from pydantic import BaseModel
from typing import List

# class Human(BaseModel):
#     first_name: str
#     last_name: str
#     age: int
#     height: float # cm
#     weight: float # kg

# def CreateHuman():
#     return Human(first_name="John", last_name="Tom", age=21, height=178.6, weight=72.9)

# human: Human = CreateHuman()
# print(human)

# def return_result(num: int):
#     return 'even' if num % 2 == 0 else 'odd'

# print(return_result(2))
# print(return_result(1))

# def return_result(num: int):
#     task = None
#     if num % 2 == 0:
#         task = ['value']
#     return task[0] if task is not None else None

# print(return_result(1))

# tmp = None
# print(tmp is None)
# print(tmp is not None)

# from api.config.config import DBConfig

# config = DBConfig()
# print(config.__str__())
# print("mysql+pymysql://root:test-passwd@localhost:33306/demo?charset=utf8")
# print("mysql+aiomysql://root:test-passwd@localhost:33306/demo?charset=utf8")