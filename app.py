import os
from flask import Flask,request
from flask_restful import Resource,Api,abort,reqparse
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from secure_check import authenticate,identity
from flask_jwt import JWT, jwt_required
from datetime import datetime
import json


app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

api = Api(app)
jwt = JWT(app,authenticate,identity)

# db configurations
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/testingdb'
app.config['SQLACHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)
###########################################################
class Todo(db.Model):
    id            = db.Column(db.Integer, primary_key=True)
    todo          = db.Column(db.String(600))
    date          = db.Column(db.DateTime,nullable=False,default=datetime.utcnow())

    def __init__(self,todo):
        self.todo = todo
    
    def json(self):
        return {'todo' : self.todo}
############################################################



parser = reqparse.RequestParser()

class Testin(Resource):
    def get(self):
        todos = Todo.query.all()
        if todos == []:
            return "No Todo in the List"
        return [ todo.json() for todo in todos ]

    def post(self):
        parser.add_argument("todo", type=str)                 #This expects a request from the user: creates field
        args = parser.parse_args()                            #Accepts user input as Dict value and the above as key: Name space
        if all([args.get(field, False) for field in ["todo"]]):#Handles wrong inputs by user
            todo = args['todo']
            newtodo = Todo(todo=todo)                          # saves to model class
            db.session.add(newtodo)                            # add to db
            db.session.commit()                                # saves to db
            return newtodo.json()
        return {"status": "Bad Request" }, 400

class Testing(Resource):
    @jwt_required()
    def get(self,id):        
        todo = Todo.query.get_or_404(id)
        return { "todo" : todo.json()},200
    
    @jwt_required()
    def put(self,id):
        todo = Todo.query.get_or_404(id)
        parser.add_argument("todo", type=str)                
        args = parser.parse_args()
        if all([args.get(field, False) for field in ["todo"]]):
            todo.todo = args.get("todo", todo.todo)
            db.session.add(todo)
            db.session.commit()
            return {"status" : "Todo Updated", "todo" : todo.json()},200
        return "Bad Request"

    @jwt_required()
    def delete(self,id):
        todo = Todo.query.get_or_404(id)
        if todo is None:
            abort(404, message ="No todo task here")
        db.session.delete(todo)
        db.session.commit()
        return {"delete":"success"},200

# @app.errorhandler(werkseug.exception.BadRequest)


api.add_resource(Testin, '/todos')
api.add_resource(Testing,'/todos/<int:id>')

if __name__ == "__main__":
    app.run(debug=True)