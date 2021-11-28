from flask import request, jsonify, Response
from flask_restful import Resource
import bcrypt
from bson import json_util
from mongo import mycolGroup
from flask_jwt_extended import create_access_token
from common.decorators import token_check
import uuid
import re  
import json


# from bson.objectid import ObjectId

class Group(Resource):
    @token_check
    def get(self):
        userid = request.args.get('userid')
        group = mycolGroup.find({"userid" : userid},{"_id":0, "id":1 , "name": 1})
        if group.count() == 0: 
            return {
                "code": 400,
                "message": "Bad Request"
            }
        response = json_util.dumps( {"data": group})
        result = json.loads(response)
        return result, 200
    
    @token_check
    def post(self):
        try:
            id = str(uuid.uuid4())
            name = request.json['name'] # Không rỗng
            userid = request.json['userid'] # Đã có trong hệ thống
            status = request.json['status'] # active, deactice
        except:
            return {"message": "name,userid,status"},400

        #Check name
        if name.replace(" ", "") == '':
            return {
                "code": 400,
                "message": "Bad Request"
            },400

        #Check userid
        
        if ((mycolGroup.find({"userid" : userid}).count() == 0) or (userid.replace(" ", "") == '')):
            return {
                "code": 400,
                "message": "Bad Request"
            },400

        #Check status
        if (status != "active" and status != "deactive") :
            return {
                "code": 400,
                "message": "Bad Request"
            },400

        mycolGroup.insert_one({
                'id' : id,
                'name': name,
                'userid': userid,
                'status' : status,
                'listBox' : []
            })
        return {
                "code": 200,
                "message": "Operation success"
        },200
    
    @token_check
    def put(self):
        id = request.args.get('id')
        
        if (mycolGroup.find({"id" : id}).count() == 0):
            return {
                "code": 400,
                "message": "Bad Request"
            },400
        
        try:
            name = request.json['name'] # Không rỗng
            status = request.json['status'] # active, deactice
        except:
            return {"message": "field name,status error"},400
            
        #Check name
        if name.replace(" ", "") == '':
            return {
                "code": 400,
                "message": "Bad Request"
            },400

        #Check role
        if (status != "active" and status != "deactice") :
            return {
                "code": 400,
                "message": "Bad Request"
            },400

        mycolGroup.update_many({"id" : id}, {"$set" : {
                'name': name,
                'status' : status,
            }})

        return {
                "code": 200,
                "message": "Operation success"
        },200

        




