from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import *
from django.shortcuts import render, redirect
from home.models import *
from exchangelib import *
import datetime
import time
from exchangelib.protocol import BaseProtocol, NoVerifyHTTPAdapter
BaseProtocol.HTTP_ADAPTER_CLS = NoVerifyHTTPAdapter


# 首页
def index(req):
    if req.session.get('user'):
        return render(req, 'index.html')
    return redirect('/login/')


# 注册
def register(req):
    if req.method == 'GET':
        return render(req, 'register.html')
    if req.method == 'POST':
        id_email = req.POST.get("id_Email")
        id_name = req.POST.get("id_Name")
        # 判断用户输入的邮箱和用户名是否存在
        email = Users.objects.filter(email=id_email)
        name = Users.objects.filter(name=id_name)
        if email and name:
            message = '用户名或者邮箱已经被注册，请重新输入！'
            return render(req, 'register.html', {'message': message})
        else:
            id_password = req.POST.get("id_Password")
            id_phone = req.POST.get("id_Phone")
            new_user = Users.objects.create(email=id_email, password=id_password, name=id_name, phone=id_phone)
            new_User = User.objects.create_user(username=id_name, email=id_email, password=id_password)
            new_user.save()
            new_User.save()
            print(new_User)
            message = '用户注册成功,请登录。'
            return redirect(req, 'login.html', {'message': message})


# 登录
def login(req):
    if req.session.get('is_login', None):  # 不允许重复登录
        return redirect('/index/')
    if req.method == 'GET':
        return render(req, 'login.html')
    if req.method == 'POST':
        name = req.POST.get('id_Username')
        password = req.POST.get('id_Password')
        message = '用户名或者密码为空！'
        if name.strip() and password:
            # 用户名字符合法性验证
            # 密码长度验证
            # 更多的其它验证.....
            try:
                user = Users.objects.get(name=name)
            except :
                message = '用户不存在！'
                return render(req, 'login.html', {'message': message})
            if user.password == password:
                req.session['is_login'] = True
                req.session['user'] = name
                Now_time = datetime.datetime.now()
                return render(req, 'index.html', {'user': name, "Now_time": Now_time})
            else:
                message = '密码不正确！'
                return render(req, 'login.html', {'message': message})
        else:
            return render(req, 'login.html', {'message': message})
    return render(req, 'login.html', {'message': '用户不存在或在密码错误，', })


# 退出登录
def logout(req):
    req.session.flush()
    return redirect('/login')


# 日历
def calendar(req):
    if req.session.get('user'):
        return render(req, 'calendar.html')
    return redirect('/login/')


# 收件箱
def mailbox(req):
    if req.session.get('user'):
        return render(req, 'mailbox/mailbox.html')
    return redirect('/login/')


# 发邮件
def compose(req):
    if req.session.get('user'):
        return render(req, 'mailbox/compose.html')
    return redirect('/login/')


# 读取邮件
def read_mail(req):
    if req.session.get('user'):
        return render(req, 'mailbox/read-mail.html')
    return redirect('/login/')


# 同步邮件
def get_mail(req):
    if req.session.get('user'):
        Emailusername = req.session.get('user')
        credentials = Credentials(
            username=req.session.get('user'),
            password='123456@a',  # Users.objects.only('password').get(name=Emailusername),
        )
        account = Account(
            primary_smtp_address='lujihao@inspur.com',  # Users.objects.only('email').get(name=Emailusername),
            credentials=credentials,
            autodiscover=True
        )
        print(account.inbox.all())
        for item in account.inbox.all().order_by('-datetime_received')[0:4]:
            subject = str(item.subject)
            # 用正则表达式获取邮件的发件人名称
            # re.findall(re.compile('name=.{10}'),str(item.sender))
            sender = str(item.last_modified_name)
            # 截取日期的字符串字段
            received = str(item.datetime_received)[0:19]
            maillist = [subject, sender, received]
            # 插入获取的邮箱数据
            boxs = Mailbox.objects.create(subject=subject, sender=sender, received=received, )
            boxs.save()
        return render(req, 'mailbox/mailbox.html')
    return redirect('/login/')

