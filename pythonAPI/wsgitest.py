def application(environ,start_response):
    start_response('200 OK',[('Content-Type','text/html')])
    return ['<h1>你好<h1>'.encode('gb2312')]
