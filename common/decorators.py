from functools import wraps
from flask import request, g, jsonify
from loguru import logger 
from jwt import decode
# from src import config
import datetime
from mongo import mycolUser
from dotenv import load_dotenv
load_dotenv()
import os



def token_check(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        # lấy token từ header ra
        try:
            token = request.headers.get('Authorization') 
            print("-------- Token ---------:", token)
            try:
                resp = decode(token, os.environ.get('SECRET_KEY'), verify=False, algorithms=["HS256"])
            except Exception as e:
                logger.error("Wrong token format header")
                return {
                        "code": 401,
                        "message": "Unauthorized"
                    },401

            if float(resp["exp"]) < datetime.datetime.now().timestamp():
                logger.error("token expired")
                return {"error": "token expired"}, 401
            g.id = resp["sub"]
            user = mycolUser.find_one({'id': g.id})
            if ( (user['role'] == 'admin') or (user['role'] == 'superadmin') ):
                return fn(*args, **kwargs)

            return {
                        "code": 401,
                        "message": "Unauthorized"
                },401
        except Exception as e:
            print("--------Lỗi---------",  e)
            return {"Error": "Bad request" }, 400

    return wrapper