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
        print("ID: ", id)

        box = mycolBoxai.find_one({'id':id},{'_id':0}) 
        if box:
            cameras = mycolCamera.find({'boxID':id},{'_id':0})
            responseCam = json_util.dumps( { "cameras" : cameras})
            resultCam = json.loads(responseCam)

            for x in resultCam["cameras"]:
                #Lấy zones từ Cam
                zones = mycolZone.find({'camID':x['id']},{'_id':0, "boxID" : 0 , "camID": 0, "groupID" : 0})
                responseZones = json_util.dumps( { "zones" : zones} )
                resultZones = json.loads(responseZones)
                x["zones"] = resultZones["zones"]

                #Lấy route từ Cam
                routes = mycolRoute.find({'camID':x['id']},{'_id':0, "boxID" : 0 , "camID": 0})
                responseRoutes = json_util.dumps( { "routes" : routes})
                resultRoutes = json.loads(responseRoutes)
                x["routes"] = resultRoutes["routes"]


            box["cameras"] = resultCam["cameras"]
            return box,200
        else:
            return {
                "code": 400,
                "message": "Bad Request, Box not found."
            },400

    @token_check   
    def post(self):
        try:
            boxai = request.json['boxai'] #insert boxai
            cameras = request.json['cameras'] #Chuỗi các camara của box
        except:
            return {
                "code": 400,
                "message": "Bad request, filed empty."
            },400
        
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
            return {
                "code": 500,
                "message": "Error!!! Insert Box failed."
            },500
            


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
                    "message": "Bad Request, Module camera (name: {}) is must belong to Module Box".format(camera["name"])
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
                return {
                    "code": 500,
                    "message": "Error!!! Insert camera failed."
                },500   

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
                        return {
                            "code": 500,
                            "message": "Error!!! Insert Zone failed."
                        },500  
                            

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
                            "message": "Bad Request, mid length is 2 or 0,  Error: {}".format(route["mid"])
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
                        return {
                            "code": 500,
                            "message": "Error!!! Insert route failed."   
                        },500 
                                         
        return {
                "code": 200,
                "message": "Operation success"
        },200

    @token_check 
    def put(self):
        id = request.args.get('id') 
        if (mycolBoxai.find({'id':id},{'_id':0}).count() == 0):
            return {
                "code": 404,
                "message": "Bad Request, BoxAi not found"
            },404
        
        try:
            boxai = request.json['boxai'] #insert boxai
            cameras = request.json['cameras'] #Chuỗi các camara của box
        except:
            return {"message": "Bad request, filed empty"},400

        
        #Validate cho Box AI
        
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
            mycolBoxai.update_one({"id" : id}, {"$set" :
                {
                    'name': boxai["name"],
                    'group': boxai["group"],
                    'module': boxai["module"],
                    'userID': boxai["userID"],
                    'registedDate' : registedDate,
                    'status' : boxai["status"],
                    'ip' : boxai["ip"],
                    'ipVPN' : boxai["ipVPN"],
                }})
        except:
            return {"message": "Error!!! Update Box failed."},400



        for camera in cameras: # Lặp các camara trong 1 boxai
            if camera["remove"] == True:
                mycolCamera.delete_one({"id": camera["id"]})
                mycolZone.delete_many({"camID": camera["id"]})  
                mycolRoute.delete_many({"camID": camera["id"]})  
                continue 
                
            # Validate camera.
            #Validate name
            if checkEmpty(camera["name"]) == True: #Tên không rỗng
                return {
                    "code": 400,
                    "message": "Bad Request, Name camera empty"
                },400

            #Validate link_stream
            if checkEmpty(camera["link_stream"]) == True: #Stream không rỗng
                return {
                    "code": 400,
                    "message": "Bad Request, Link_stream empty"
                },400
            

            # Validate module 
            if set(camera["module"]).issubset(set(boxai["module"])) == False: 
                return {
                    "code": 400,
                    "message": "Bad Request, Module camera (name: {}) is must belong to Module Box".format(camera["name"])
                },400

            #Validate status
            if (camera["status"] != True and camera["status"] != False) :
                return {
                    "code": 400,
                    "message": "Bad Request, Status is boolean"
                },400
            
            if camera["id"] != "": #Nếu khác rỗng thì chỉnh sửa camera đó
                if  mycolCamera.find({"id": camera["id"] }).count() == 0: #Nếu không tìm thấy trong db
                    return {"message": "Error!!! Camera not found. idCamera: {}".format(camera["id"])},404  
                try:
                    mycolCamera.update_one({"id": camera["id"] },{"$set" : 
                        {
                            "status": camera["status"],
                            "link_stream": camera["link_stream"],
                            "userID": boxai["userID"],
                            "module": camera["module"],
                            "name": camera["name"]
                        }})
                except:
                    return {"message": "Error!!! Update camera failed."},400    
            else:  # Nếu bằng rỗng thì thêm mới camera
                idCamera = str(uuid.uuid4())
                camera["id"] = idCamera
                try:
                    mycolCamera.insert_one({
                        "id": idCamera,
                        "status": camera["status"],
                        "link_stream": camera["link_stream"],
                        "userID": boxai["userID"],
                        "boxID": id,
                        "module": camera["module"],
                        "name": camera["name"]
                    })
                except:
                    return {"message": "Error!!! Insert camera failed."},400      
            
            if set(["pc"]).issubset(set(camera["module"])): # Nếu module camera có pc thì thêm zone
                zones = camera['zones'] #Chuỗi các zones
                for zone in zones: # Lặp các zone trong 1 camera
                    if zone["remove"] == True:
                        mycolZone.delete_one({"id": zone["id"]})
                        continue
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

                    if zone["id"] != "": #Nếu khác rỗng thì chỉnh sửa Zone đó
                        if  mycolZone.find({"id": zone["id"] }).count() == 0: #Nếu không tìm thấy trong db
                            return {"message": "Error!!! Zone not found."},404 
                        else:
                            try:
                                mycolZone.update_one({"id": zone["id"] },{"$set" : 
                                    {
                                        "name": zone["name"],
                                        "location": zone["location"],
                                        "offset": zone["offset"],
                                    }})
                            except:
                                return {"message": "Error!!! Update Zone failed."},400    
                    else:  # Nếu bằng rỗng thì thêm mới Zone
                        try:
                            mycolZone.insert_one({
                                "id": str(uuid.uuid4()),
                                "name": zone["name"],
                                "offset": zone["offset"],
                                "boxID": id,
                                "location": zone["location"],
                                "camID" : camera["id"],
                                "groupID": boxai["group"],
                            })
                        except:
                            return {"message": "Error!!! Insert zone failed."},400  

            if set(["rm"]).issubset(set(camera["module"])): # Nếu module camera có rm thì thêm route
                routes = camera["routes"]
                for route in routes: # Lặp các zone trong 1 camera
                    if route["remove"] == True:
                        mycolRoute.delete_one({"id": route["id"]})
                        continue
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

                    if route["id"] != "": #Nếu khác rỗng thì chỉnh sửa route đó
                        
                        if  mycolRoute.find({"id": route["id"] }).count() == 0: #Nếu không tìm thấy trong db
                            return {"message": "Error!!! route not found."},404 
                        else:
                            try:
                                mycolRoute.update_one({"id": route["id"] },{"$set" : 
                                    {
                                        "start": route["start"],
                                        "end": route["end"],
                                        "mid": route["mid"],
                                        "cluster": route["cluster"],
                                    }})
                            except:
                                return {"message": "Error!!! Update Route failed."},400    
                    else:  # Nếu bằng rỗng thì thêm mới Zone
                        
                        try:
                            mycolRoute.insert_one({
                                "id": str(uuid.uuid4()),
                                "boxID": id,
                                "camID" : camera["id"],
                                "start": route["start"],
                                "end": route["end"],
                                "mid": route["mid"],
                                "cluster": route["cluster"],
                            })
                        except:
                            return {"message": "Error!!! Insert Route failed."},400  


        return {
                "code": 200,
                "message": "Operation success"
        },200

class ListBox(Resource):
    @token_check
    def get(self):
        boxs = mycolBoxai.find({},{'_id':0, "group" : 0 , "boxToken" : 0 }) 
        response = json_util.dumps(boxs) 
        return Response(response, mimetype='application/json')


