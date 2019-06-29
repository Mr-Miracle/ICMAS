from django.db import models

# Create your models here.


# 组织信息
class Corp(models.Model):
    code = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    place = models.CharField(max_length=50)
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name


# 用户信息
class Users(models.Model):
    code = models.CharField(max_length=50, primary_key=True)
    email = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=120)
    phone = models.CharField(max_length=30)
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name


# 邮箱收件箱
class Mailbox(models.Model):
    subject = models.CharField(max_length=250)
    sender = models.CharField(max_length=50)
    received = models.DateTimeField(max_length=50)
    create_datetime = models.DateTimeField(auto_now_add=True)
    modify_datetime = models.DateTimeField(auto_now_add=True)
