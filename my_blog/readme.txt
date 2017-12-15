1.cd f:/pythonwork      先切换到对应的目录下
2.django-admin startproject my_blog     创建一个项目
3.cd my_blog    切换到对应的项目下
4.python manage.py startapp article     创建一个app
    article是一个app，一个app就是一个功能模块
5.在my_blog/my_blog/settings.py下添加新建app，article
6.python manage.py runserver localhost:9000     部署

一、Models
    1.Django Model
        a）每一个Django Model都继承自django.db.models.Model
        b）在Model当中每一个属性attribute都代表一个database field
        c）通过Django Model API可以执行数据库的增删改查, 而不需要写一些数据库的查询语句
    2.设置数据库
        my_blog/my_blog/settings.py中可以查看和修改数据库设置
    3.创建models
        在my_blog/article/models.py下编写程序
        a）CharField 用于存储字符串, max_length设置最大长度
        b）TextField 用于存储大量文本
        c）DateTimeField 用于存储时间, auto_now_add设置True表示自动设置对象增加时间
    4.同步数据库
        python manage.py makemigrations
        python manage.py migrate

二、Admin
    1.设置url
        在my_blog/my_blog/urls.py中设置 url(r'^admin/', admin.site.urls)
    2.创建超级用户
        python manage.py createsuperuser
        账号:admin
        密码:admin123

三、Views和URL
    1.网页程序的逻辑
    request进来->从服务器获取数据->处理数据->把网页呈现出来
        url设置相当于客户端向服务器发出request请求的入口, 并用来指明要调用的程序逻辑
        views用来处理程序逻辑, 然后呈现到template(一般为GET方法, POST方法略有不同)
        template一般为html+CSS的形式, 主要是呈现给用户的表现形式

    2.url()函数有四个参数, 两个是必须的:regex和view, 两个可选的:kwargs和name
        regex是regular expression的简写,这是字符串中的模式匹配的一种语法, Django 将请求的URL从上至下依次匹配列表中的正则表达式，直到匹配到一个为止。
        view当Django匹配了一个正则表达式就会调用指定的view逻辑, 上面代码中会调用article/views.py中的home函数
        kwargs任意关键字参数可传一个字典至目标view
        name命名你的 URL, 使url在 Django 的其他地方使用, 特别是在模板中