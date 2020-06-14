import os
from flask import Flask,request
from flask_restful import Resource,Api,abort
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime
import json


app = Flask(__name__)
api = Api(app)

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



# parser = reqparse.RequestParser()
# parser.add_argument('work')

class Testin(Resource):
    def get(self):
        todos = Todo.query.all()
        if todos == []:
            return "No Todo in the List"
        return [ todo.json() for todo in todos ]

    def post(self):
        todo = request.get_json()['todo']
        newtodo = Todo(todo=todo)
        db.session.add(newtodo)
        db.session.commit()
        return newtodo.json()

class Testing(Resource):
    def get(self,id):
        todo_id = Todo.query.filter_by(id=id).first()
        if todo_id is None:
            abort(404, message ="No todo task here")
        return { 'todo' : todo_id.json()}
    
    def patch(self,id):
        todo_id = Todo.query.filter_by(id=id).first()
        if todo_id is None:
            abort(404, message ="No todo task here")
        # oldtodo = { "todo" : todo_id.json()}
        if 'todo' in request.get_json():
            todo_id = request.get_json()['todo']
        db.session.commit()
        return "here"

    def delete(self,id):
        todo_id = Todo.query.filter_by(id=id).first()
        if todo_id is None:
            abort(404, message ="No todo task here")
        db.session.delete(todo_id)
        db.session.commit()
        return {"delete":"success"},201


api.add_resource(Testin, '/todos')
api.add_resource(Testing,'/todos/<int:id>')

if __name__ == "__main__":
    app.run(debug=True)