# coding:utf-8
from flask import Flask,redirect

#初始化
app = Flask(__name__)

#路由和视图
@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

#响应
@app.route('/a')
def index2():
    return '<h1>你要找的网页不见了</h1>', 400

#重定向
@app.route('/aa')
def index3():
    return redirect('http://www.baidu.com')

#动态参数
@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s!</h1>' % name
    # return '<h1>Hello, '+ name +'!</h1>'

# @app.route('/user/<int:id>')
# def userId(id):
#     return '<h1>Hello, '+ str(id) +'!</h1>'

if __name__ == '__main__':
    app.run(debug=True)