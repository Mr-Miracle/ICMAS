from django.urls import path
from home import views

urlpatterns = [
    path('calendar/', views.calendar),
    path('mailbox/mailbox', views.mailbox),
    path('mailbox/compose', views.compose),
    path('mailbox/read_mail', views.read_mail),

]
