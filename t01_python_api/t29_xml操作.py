#coding:utf-8
# 操作作 XML 有两种方法：DOM 和 SAX。
# DOM 会把整个 XML 读入内存，解析为树，因此占用内存大，解析慢，优点是可以任意遍历树的节点。
# SAX 是流模式，边读边解析，占用内存小，解析快，缺点是我们需要自己处理事件。
from xml.dom.minidom import parse

file_path = 't29.xml'
dom = parse(file_path)
# 获取文档元素对象
data = dom.documentElement
# 获取 property
content = data.getElementsByTagName('content')
print(content)
for item in content:
    print(item.childNodes[0].nodeValue)