# coding:utf-8
import json
import jsonpath

# dumps 把 dict转成json string
# loads 把 json string转成dict

# dict转换成json字符串
d = dict(name="Bob", age=20, score=100)
j = json.dumps(d)
# print(j)

# json字符串转换成dict
j = '{"name":"Bob","age":20,"score":100}'
d = json.loads(j)


# print(d)


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


# def student_dict(std):
#     return {
#         "name": std.name,
#         "age": std.age,
#         "score": std.score
#     }


s = Student("Bob", 20, 100)

# 把对象转换成json string
# print(json.dumps(s, default=student_dict))
# 不需要自己写函数，直接把对象转换成dict
# print(json.dumps(s,default=lambda obj:obj.__dict__))
# class的属性，可以把obj转换成dict
print(s.__dict__)

# 通过jsonpath获取对应值
res = jsonpath.jsonpath(s.__dict__, '$..age')[0]
print(res)

ctx = {
    "code": "200",
    "data": {
        "appTime": "2022-09-28 11:30:07",
        "checkStatus": 1,
        "children": [
            {
                "addTime": "2022-09-28 11:30:07",
                "appTime": "2022-09-28 11:30:07",
                "checkStatus": "1",
            },
            {
                "addTime": "2022-09-29 11:30:07",
                "appTime": "2022-09-29 11:30:07",
                "checkStatus": "2",
            }
        ],
        "id": "2bdc0dbc-d3d0-4c9b-9f10-180ba842f6cb",
        "informationCheck": "通过",
    },
    "message": "成功",
    "success": True,
    "time": "1664359782018"
}

'''
$.store.book[*].author                  获取json中store下book下的所有author值
$..author                               获取所有json中所有author的值
$.store.*                               所有的东西，书籍和自行车
$.store..price                          获取json中store下所有price的值
$..book[2]                              获取json中book数组的第3个值
$..book[-2]                             倒数的第二本书
$..book[0,1]                            前两本书
$..book[:2]                             从索引0（包括）到索引2（排除）的所有图书
$..book[1:2]                            从索引1（包括）到索引2（排除）的所有图书
$..book[-2:]                            获取json中book数组的最后两个值
$..book[2:]                             获取json中book数组的第3个到最后一个的区间值
$..book[?(@.isbn)]                      获取json中book数组中包含isbn的所有值
$.store.book[?(@.price < 10)]           获取json中book数组中price<10的所有值
$..book[?(@.price <= $['expensive'])]   获取json中book数组中price<=expensive的所有值
$..book[?(@.author =~ /.*REES/i)]       获取json中book数组中的作者以REES结尾的所有值（REES不区分大小写）
$..*                                    逐层列出json中的所有值，层级由外到内
$..book.length()                        获取json中book数组的长度
'''

# 查询checkStatus为2的child
result = jsonpath.jsonpath(ctx, '$..children[?(@.checkStatus=="2")]')
print(result)