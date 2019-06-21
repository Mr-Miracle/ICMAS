$ python manage.py createsuperuser

$ python manage.py migrate   # 创建表结构
$ python manage.py makemigrations   # 让 Django 知道我们在我们的模型有一些变更


startapp
$ django-admin startapp name [directory]

 startproject
$ django-admin startproject name [directory]


requirements.txt文件是一个项目的依赖文件，可以通过下面的方式自动生成：
$ pip freeze > ./requirements.txt

如果拷贝了我的代码，要安装第三方库依赖的话，只需要：
$ pip install -r requirements.txt
就可以一次性安装好所有的库了。


"""extends继承‘base.html’；
{% load static %}载入静态文件；
{% block title %}资产详细{% endblock %}，定制title;
{% block css %}，载入当前页面的专用CSS文件；
{% block breadcrumb%}定制顶部面包屑导航;
{% block script %}，载入当前页面的专用js文件；
最后在{% block content %}中， 填充页面的主体内容
"""

