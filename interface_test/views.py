# coding:utf-8
import warnings
from flask import Flask,request,render_template
from interface_test.model import *
from flask_bootstrap import Bootstrap

warnings.filterwarnings('ignore')
app=Flask(__name__)
bootstrap=Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_door',methods=['GET','POST'])
def app_add_door():
    return render_template('add_door.html',name1=addOfflineDoor())

@app.route('/add_door_engineer',methods=['GET','POST'])
def app_add_door_engineer():
    return render_template('add_door_engineer.html',name1=addOfflineDoor())

@app.route('/all',methods=['GET','POST'])
def app_all():
    return render_template('all.html',name1=addOfflineDoor(),name2=addDoorEngineer())

if __name__=='__main__':
    app.run(debug=False)

