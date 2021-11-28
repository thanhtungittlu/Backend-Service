from flask import request, jsonify, Response
from flask_restful import Resource
import bcrypt,re,json
from bson import json_util
from mongo import mycolBoxai, mycolCamera, mycolZone, mycolRoute,mycolUser,mycolGroup
from common.decorators import token_check
from common.common import checkEmpty, checkNumber0to1
import uuid
import datetime



# from bson.objectid import ObjectId

class Boxai(Resource):
    @token_check
    def get(self):
        id = request.args.get('id')
        box = mycolBoxai.find_one({'id':id},{'_id':0}) 
        return box,200
    @token_check    
    def post(self):
        try:
            boxai = request.json['boxai'] #insert boxai
            cameras = request.json['cameras'] #Chuỗi các camara của box
        except:
            return {"message": "Bad request, filed empty"},400

        
    #Validate cho Box AI
        idBoxai = str(uuid.uuid4())

        #Validate name
        if checkEmpty(boxai["name"]) == True: #Tên không rỗng
            return {
                "code": 400,
                "message": "Bad Request, Name boxai empty"
            },400


        #Validate Group
        if mycolGroup.find( {"id": boxai["group"] }).count() == 0: #Nếu không tìm thấy trong db group thì trả về lỗi
            return {
                "code": 400,
                "message": "Bad Request, Group not exist"
            },400

        #Validate module
        product = ["hm","rm","pc","fr","att"]
        # set(A).issubset(set(B)): Kiểm tra xem A có phải tập con của B hay không
        if set(boxai["module"]).issubset(set(product)) == False: 
            return {
                "code": 400,
                "message": "Bad Request, Module not satisfied."
            },400

        #Validate User
        if mycolUser.find( {"id": boxai["userID"] }).count() == 0: #Nếu không tìm thấy trong db user thì trả về lỗi
            return {
                "code": 400,
                "message": "Bad Request, User not exist"
            },400
        
        objDate= datetime.date.today() #Lấy ngày hiện tại
        registedDate = str(objDate.month) + "-" + str(objDate.day) + "-" + str(objDate.year) # Chuyển sang kiểu string
    

        #Validate status

        if (boxai["status"] != "Module installed" and boxai["status"] != "Module is not installed") :
            return {
                "code": 400,
                "message": "Bad Request, Status: Module installed or Module is not installed"
            },400

        try:
            mycolBoxai.insert_one({
                    'id' : idBoxai,
                    'name': boxai["name"],
                    'group': boxai["group"],
                    'module': boxai["module"],
                    'userID': boxai["userID"],
                    'registedDate' : registedDate,
                    'status' : boxai["status"],
                    'ip' : boxai["ip"],
                    'ipVPN' : boxai["ipVPN"],
                })
        except:
            return {"message": "Error!!! Insert Box failed."},400


        for camera in cameras: # Lặp các camara trong 1 boxai
            idCamara = str(uuid.uuid4())
        # Validate camera.

            #Validate name
            if checkEmpty(camera["name"]) == True: #Tên không rỗng
                return {
                    "code": 400,
                    "message": "Bad Request, Name camera empty"
                },400

            #Validate link_stream
            if checkEmpty(camera["link_stream"]) == True: #Tên không rỗng
                return {
                    "code": 400,
                    "message": "Bad Request, Link_stream empty"
                },400
            

            # Validate module 
            if set(camera["module"]).issubset(set(boxai["module"])) == False: 
                return {
                    "code": 400,
                    "message": "Bad Request, Module camera is must belong to Module Box"
                },400

            #Validate status
            if (camera["status"] != True and camera["status"] != False) :
                return {
                    "code": 400,
                    "message": "Bad Request, Status is boolean"
                },400
            try:
                mycolCamera.insert_one({
                    "id": idCamara,
                    "status": camera["status"],
                    "link_stream": camera["link_stream"],
                    "userID": boxai["userID"],
                    "boxID": idBoxai,
                    "module": camera["module"],
                    "name": camera["name"]
                })
            except:
                return {"message": "Error!!! Insert camera failed."},400            
    

            if set(["pc"]).issubset(set(camera["module"])): # Nếu module camera có pc thì thêm zone
                zones = camera['zones'] #Chuỗi các zones
                for zone in zones: # Lặp các zone trong 1 camera
                #Validate zone
                    #Validate Name
                    if checkEmpty(zone["name"]) == True: #Tên không rỗng
                        return {
                            "code": 400,
                            "message": "Bad Request, Name zone empty"
                        },400 
                    #Validate location
                    if (zone["location"] != "gate" and zone["location"] != "shop" and zone["location"] != "way") :
                        return {
                            "code": 400,
                            "message": "Bad Request, Location: gate or shop or way"
                        },400

                    #Validate offset
                    for x in zone["offset"]:
                        if checkNumber0to1(x) == False:
                            return {
                                "code": 400,
                                "message": "Bad Request, offset is array from 0 to 1, Error: {}".format(zone["offset"])
                            },400
                    try:
                        mycolZone.insert_one({
                            "id": str(uuid.uuid4()),
                            "name": zone["name"],
                            "offset": zone["offset"],
                            "boxID": idBoxai,
                            "location": zone["location"],
                            "camID" : idCamara,
                            "groupID": boxai["group"],
                        })
                    except:
                        return {"message": "Error!!! Insert Zone failed."},400    

            if set(["rm"]).issubset(set(camera["module"])): # Nếu module camera có rm thì thêm route
                routes = camera["routes"]
                for route in routes: # Lặp các zone trong 1 camera
                #Validate route
                    #Validate cluster
                    if checkEmpty(route["cluster"]) == True: #Tên không rỗng
                        return {
                            "code": 400,
                            "message": "Bad Request, Cluster empty"
                        },400  

                    #Validate start, có 2 phần tử, mỗi phần từ từ 0 tới 1
                    if len(route["start"]) != 2:
                        return {
                            "code": 400,
                            "message": "Bad Request, Start length is 2,  Error: {}".format(route["start"])
                        },400

                    for x in route["start"]:
                        if checkNumber0to1(x) == False:
                            return {
                                "code": 400,
                                "message": "Bad Request, start is array from 0 to 1, Error: {}".format(route["start"])
                            },400

                    #Validate end, có 2 phần tử, mỗi phần từ từ 0 tới 1
                    if len(route["end"]) != 2:
                        return {
                            "code": 400,
                            "message": "Bad Request, end length is 2,  Error: {}".format(route["end"])
                        },400

                    for x in route["end"]:
                        if checkNumber0to1(x) == False:
                            return {
                                "code": 400,
                                "message": "Bad Request, end is array from 0 to 1, Error: {}".format(route["end"])
                            },400

                    #Validate mid, có 2 phần tử, hoặc 0 phần tử, mỗi phần từ từ 0 tới 1
                    if len(route["mid"]) != 2 and len(route["mid"]) != 0:
                        return {
                            "code": 400,
                            "message": "Bad Request, mid length is 2,  Error: {}".format(route["mid"])
                        },400

                    for x in route["mid"]:
                        if checkNumber0to1(x) == False:
                            return {
                                "code": 400,
                                "message": "Bad Request, mid is array from 0 to 1, Error: {}".format(route["mid"])
                            },400

                    try:
                        mycolRoute.insert_one({
                            "id": str(uuid.uuid4()),
                            "boxID": idBoxai,
                            "camID" : idCamara,
                            "start": route["start"],
                            "end": route["end"],
                            "mid": route["mid"],
                            "cluster": route["cluster"],
                        })
                    except:
                        return {"message": "Error!!! Insert route failed."},400    
            
                 
        return {
                "code": 200,
                "message": "Operation success"
        },200





