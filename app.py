import datetime
from flask import Flask
from flask_cors import CORS, cross_origin
from flask_restful import  Api
from resources.user import Loginn,ListUser, AddUser, User
from resources.group import Group
from resources.boxai import Boxai




from dotenv import load_dotenv
load_dotenv()
import os



from flask_jwt_extended import JWTManager


app = Flask(__name__) 
CORS(app)
app.secret_key = os.environ.get('SECRET_KEY')
api = Api(app)
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(seconds=36000)
jwt = JWTManager(app)



api.add_resource(Loginn, "/login")
api.add_resource(ListUser, "/users")
api.add_resource(AddUser, "/insert")
api.add_resource(User, "/user/<id>")

api.add_resource(Group, "/group")
api.add_resource(Boxai, "/box")











if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host='0.0.0.0', debug=True)