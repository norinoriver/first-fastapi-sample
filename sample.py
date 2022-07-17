# import sqlalchemy
# from pydantic import BaseModel
# from typing import List

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

# import redis
# redis = redis.Redis(host='localhost', port=26379, db=0, password='test-passwd')

# redis.set('hoge', 'hoge')

# hoge = redis.get('hoge')

# print(hoge.decode())

# import aioredis
# import asyncio

# async def main():
#     redis = aioredis.from_url("redis://default:test-passwd@localhost:26379/0")
#     await redis.set("my-key", "value")
#     value = await redis.get("my-key")
#     print(value)

# if __name__ == "__main__":
#     asyncio.run(main())

# import datetime

# d = datetime.datetime.now()
# print(d)
# print(d + datetime.timedelta(days=3))

# dict = {"first_name": "John"}
# dict_copy = dict.copy()
# dict2 = dict

# dict2.update({"last_name": "Doe"})
# dict_copy.update({"last_name": "Doe"})

# print(dict)
# print(dict2)
# print(dict_copy)

# from deprecated import deprecated
# from passlib.context import CryptContext
# pwd_ctx = CryptContext(schemes=["bcrypt"], deprecated="auto")
# pwd_ctx2 = CryptContext(schemes=["bycrypt", "sha256_crypt"], deprecated="auto")
# class Hash():
#     def get_password_hash(password: str):
#         return pwd_ctx.hash(password)

#     def verify_password(hashed_password, plain_password):
#         return pwd_ctx.verify(plain_password, hashed_password)

# password = "secret"
# password = "a"*100
# hashed_password = pwd_ctx.hash(password)

# $2b $12 $EixZaYVK1fsbw1ZfbX3OXe. PaWxn96p36WQoeG6Lruj3vjPGga31lW

# hashed_password2 = "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW"
# print(isinstance(hashed_password, str))

# print(pwd_ctx.hash(password, scheme="bcrypt")) # less than 72bytes
# print(len(hashed_password))
# print(hashed_password)
# print(Hash.verify_password(hashed_password, "secret"))
# print(Hash.verify_password(hashed_password2, "secret"))

# import string

# password = "p@ssw0rd;"
# password = "パスワード"

# allowed = string.ascii_letters + string.digits + string.punctuation
# print(allowed)
# try:
#     assert all(char in allowed for char in password)
# except AssertionError:
#     print("error")

# print(len("$2b$12$A/kzt7aCdWKQFpwDCo7XC.DO9dGoz0ppPlFF69u9m4BGSBbYsZr3S"))

# import fire
# def greet(msg="HELLO WORLD!"):
#     print(msg)

# fire.Fire(greet)
# import uuid
# print(uuid.uuid4().hex)

# from  passlib.context import CryptContext

# pwd_ctx = CryptContext(schemes=["sha256_crypt"], deprecated="auto")
# password = "password"
# hashed_password = pwd_ctx.hash(password)
# print(hashed_password)