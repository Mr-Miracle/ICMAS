from django.db import models

# Create your models here.


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
