# coding:utf-8
from flask import Flask

#初始化
app = Flask(__name__)

#路由和视图
@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

#动态参数
@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s!</h1>' % name

if __name__ == '__main__':
    app.run(debug=True)