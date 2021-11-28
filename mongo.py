import pymongo
from dotenv import load_dotenv
load_dotenv()
import os


mongo_uri = 'mongodb://' + os.environ.get('USERNAME_MONGO') + ':' + os.environ.get('PASSWORD_MONGO') + '@' + os.environ.get('IP') + ':' + os.environ.get('PORT') + '/' + os.environ.get('AUTHENTICATION')

mongo = pymongo.MongoClient(mongo_uri)

mydb = mongo[os.environ.get('DB')] #Truy cập vào db iviewstaging
mycolUser = mydb[os.environ.get('COLLECTION_USER')]  #Truy cập vào collection user
mycolGroup = mydb[os.environ.get('COLLECTION_GROUP')]  #Truy cập vào collection group

mycolBoxai = mydb[os.environ.get('COLLECTION_BOXAI')]  #Truy cập vào collection group
mycolCamera = mydb[os.environ.get('COLLECTION_CAMERA')]  #Truy cập vào collection group
mycolZone = mydb[os.environ.get('COLLECTION_ZONE')]  #Truy cập vào collection group
mycolRoute = mydb[os.environ.get('COLLECTION_ROUTE')]  #Truy cập vào collection group





