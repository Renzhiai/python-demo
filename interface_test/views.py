# coding:utf-8
import warnings
from flask import Flask,request,render_template
from model import *

warnings.filterwarnings('ignore')

app=Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_door_28',methods=['GET','POST'])
def app_add_door_28():
    return render_template('add_door_28.html',name1=add_door_28())

@app.route('/open_door_voice_28',methods=['GET','POST'])
def app_open_door_voice_28():
    return render_template('open_door_voice_28.html',name1=open_door_voice_28())

@app.route('/add_door_engineer_28',methods=['GET','POST'])
def app_add_door_engineer_28():
    return render_template('add_door_engineer_28.html',name1=add_door_engineer_28())

@app.route('/add_visible_device_28',methods=['GET','POST'])
def app_add_visible_device_28():
    return render_template('add_visible_device_28.html',name1=add_visible_device_28())

@app.route('/all_28',methods=['GET','POST'])
def app_all_28():
    return render_template('all_28.html',name1=add_door_28(),name2=open_door_voice_28(),name3=add_door_engineer_28(),name4=add_visible_device_28())

if __name__=='__main__':
    app.run(debug=True)

