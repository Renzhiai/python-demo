# coding:utf-8
from flask import Flask

app=Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world!'

@app.route('/home')
def home():
    return 'Home'

#变量
@app.route('/welcome/<username>')
def welcome(username):
    return 'Hello, %s' % username

@app.route('/number/<int:number>')
def hello_number(number):
    return 'Hello, %s' % number

#/和不带/
@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'


if __name__=='__main__':
    app.run(debug=True)


