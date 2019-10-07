from wsgiref.simple_server import make_server

def application(env, startResponse):
    startResponse('200 OK', [('Content-Type', 'text/html')])
    return [b'<h1>Hello, web!</h1>']

# 创建一个服务器，IP地址为空，端口是9999，处理函数是application
httpd = make_server('127.0.0.1', 9999, application)
print('http开始监听端口...')
# 开始监听 HTTP 请求:
httpd.serve_forever()