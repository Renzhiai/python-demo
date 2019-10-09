#coding:utf-8
#1.位置参数：调用函数时，传入的两个值按照位置顺序依次赋给参数 x 和 n
def power(x):
    return x*x

def power(x,n):
    s=1
    while n>0:
        n=n-1
        s=s*x
    return s

#2.默认参数：必选参数在前，默认参数在后
#函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数
def power(x,n=2):
    s=1
    while n>0:
        n=n-1
        s=s*x
    return s

#3.可变参数允许你传入 0 个或任意个参数，这些可变参数在函数调用时自动组装为一个 tuple
#计算a*a+ b*b +c*c + ……。
#numbers只能是list或者tuple
def calc(numbers):
    sum=0
    for n in numbers:
        sum=sum+n*n
    return sum
#传入参数如下
calc([1,3,7])
calc((3,5,6))
#使用可变参数，参数 numbers 接收到的是一个 tuple
def calc(*numbers):
    sum=0
    for n in numbers:
        sum=sum+n*n
    return sum

calc(1,2)
calc()

#4.关键字参数允许你传入 0 个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个 dict
def person(name,age,**kw):
    print("name:",name,"age:",age,"99.other:",kw)

person("Xiaoming",30)
person("Xiaoh",18,city="Shenzhen",job="Test")
keyword={"city":"Shenzhen","job":"Test"}
person("Xiaoshuai",24,**keyword)

#5.命名关键字参数
def person(name,age,**kw):
    if "city" in kw:
        #有city参数
        pass
    if "job" in kw:
        #有job参数
        pass
    print("name:",name,"age:",age,"99.other:",kw)

#如果要限制关键字参数的名字，就可以用命名关键字参数
#如，只接收 city 和 job 作为关键字参数，name，age是位置参数，*是特殊分隔符
def person(name,age,city,job):
    print(name,age,city,job)

# *不是参数，而是特殊分隔符
def person(name, age, *, city='Beijing', job):
    print(name, age, city, job)

#命名关键字参数必须传入参数名
person("Xiaoai",24,city="Shenzhen",job="Test")