from flask import request, jsonify, Response
from flask_restful import Resource
import bcrypt
from bson import json_util
from mongo import mycolUser
from flask_jwt_extended import create_access_token
from common.decorators import token_check
import uuid
import re  



# from bson.objectid import ObjectId

class Loginn(Resource):
    def post(self):
        email = request.json.get("email", None)
        password = request.json.get("password", None)
        user = mycolUser.find_one({'email': email})

        # bcrypt.checkpw(passwd, hashed)
        if (user is None) or (  bcrypt.checkpw(password.encode('utf-8'), user['password'].encode('utf-8')) == False  ):
            return {"message" : "Wrong email or password"} , 401
        else:
            if ( (user['role'] == 'admin') or (user['role'] == 'superadmin') ):
                access_token = create_access_token(identity=user['id'])
                return {"access_token" : access_token}, 200
            else:
                return {"message" : "You are not authorized"} , 401


class ListUser(Resource):
    @token_check
    def get(self):
        users = mycolUser.find(  {'role': { '$in': ['boss', 'manager']}} ,{'_id': 0, 'id':1, 'email': 1, 'status' : 1 , 'boxNumber' : 1, 'role': 1}) 
        response = json_util.dumps(users) 
        return Response(response, mimetype='application/json')

class AddUser(Resource):
    @token_check
    def post(slef):
        id = str(uuid.uuid4())
        name = request.json['name']
        email = request.json['email']
        password = request.json['password']
        phoneNumber = request.json['phoneNumber']
        apiURL = request.json['apiURL']
        role = request.json['role']
 
        if (mycolUser.find({"email" : request.json['email']}).count() == 1) :
            return { "message" : "User already in use, Email exists"}, 400
        else:
            #Check Email
            regexEmail = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$' 
            if( re.search(regexEmail,email) is None ):   
                return { "message" : "Email invalid"}
            
            #Encrypt password.
            salt = bcrypt.gensalt()
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')

            #Check phoneNumber

            phoneNumber = phoneNumber.replace(" ", "")
            regexPhone = '^[0-9]{0,11}$' #Từ 0-11 chữ số
            if( re.search(regexPhone, phoneNumber) is None ):   
                return { "message" : "phoneNumber invalid"}
            

            #Check role
            if (role != "boss" and role != "manager") :
                return { "message" : "Role can only be boss or manager."}


            mycolUser.insert_one({
                'id' : id,
                'name': name,
                'email': email,
                'password': hashed_password,
                'verify': True,
                'product': 'fr,pc,hm,at,fd,lp',
                'phoneNumber': phoneNumber ,
                'boxNumber': 100,
                'mobileToken': '',
                'apiURL': apiURL,
                'role': role,
                'status': True, 
            })
            userNew = mycolUser.find_one({"email" : email},{"_id":0}) #Kiểu dict
            return userNew,201



class User(Resource):
    @token_check
    def get(self,id):
        user = mycolUser.find_one({"id" : id},{"_id":0})
        if (user is None):
            return {"message": "User not found"}
        return user,200

    def put(self,id):
        
        userUpdate = mycolUser.find_one({"id" : id},{"_id":0})
        if (userUpdate is None):
            return {"message": "User not found"}

        name = request.json['name']
        email = request.json['email']
        password = request.json['password']
        phoneNumber = request.json['phoneNumber']
        apiURL = request.json['apiURL']
        role = request.json['role']


        userCheckEmail = mycolUser.find_one({"email" : request.json['email']})

        if ((userCheckEmail is None) or (userCheckEmail['email']  ==  userUpdate['email'])):
            #Nếu Email không có, hoặc có nhưng trùng với email đang chỉnh sửa thì tiếp tục
            #Check Email
            # /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
            regexEmail = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$' 
            if( re.search(regexEmail,email) is None ):   
                return { "message" : "Email invalid"}
            
            #Encrypt password.
            salt = bcrypt.gensalt()
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')

            #Check phoneNumber
            phoneNumber = phoneNumber.replace(" ", "")
            regexPhone = '^[0-9]{0,11}$' #Từ 0-11 chữ số
            if( re.search(regexPhone, phoneNumber) is None ):   
                return { "message" : "phoneNumber invalid"}
            

            #Check role
            if (role != "boss" and role != "manager") :
                return { "message" : "Role can only be boss or manager "}

            mycolUser.update_one({"id" : id}, {"$set" : {
                'name': name,
                'email': email,
                'password': hashed_password,
                'phoneNumber': phoneNumber ,
                'apiURL': apiURL,
                'role': role,
            }})
            userNew = mycolUser.find_one({"email" : email},{"_id":0}) #Kiểu dict
            return userNew,201
        else:
            return {"message" : "Admin already in use, Email exists"}, 400 

    @token_check     
    def delete(self,id):
        user = mycolUser.find_one({"id" : id},{"_id":0})
        if (user is None):
            return {"message": "User not found"}
        mycolUser.delete_one({"id" : id})
        return {"message": "Admin deleted"}, 200




