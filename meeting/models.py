from django.db import models
from home.models import Users, Corp
# Create your models here.


# 园区
class Park(models.Model):
    code = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    place = models.CharField(max_length=50)
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# 会议室
class Room(models.Model):
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    parks_id = models.ForeignKey('Park', on_delete=models.CASCADE)
    floor = models.CharField(max_length=20)
    capacity = models.CharField(max_length=20)
    equipment = models.CharField(max_length=20)
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# 会议预定单据
class Order(models.Model):
    theme = models.CharField(max_length=20)
    room_id = models.ForeignKey('Room', on_delete=models.CASCADE)
    creator = models.CharField(max_length=20)
    department = models.CharField(max_length=50)
    corp = models.CharField(max_length=20)
    order_date = models.DateTimeField(max_length=20)
    start_time = models.DateTimeField(max_length=20)
    end_time = models.DateTimeField(max_length=20)
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


