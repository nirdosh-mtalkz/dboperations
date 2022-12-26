from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db=SQLAlchemy(app)

class Employee(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(50),nullable=False,unique=True)
    password = db.Column(db.String(50),nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return f"{self.username} - {self.password}"

@app.route('/')
def Show():
    emp=Employee.query.all()
    res=[]
    for e in emp:
        tmp = {'id':e.id,'username':e.username,'password':e.password}
        res.append(tmp)
    return {'Employee Details':res}

@app.route('/add',methods=['POST'])
def add():
    emp = Employee(request.json['username'],request.json['password'])
    db.create_all()
    db.session.add(emp)
    db.session.commit()
    return "Successfully added %s" %request.json['username']


if __name__ == '__main__':
    app.run(debug=True)