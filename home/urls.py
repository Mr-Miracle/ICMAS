from django.urls import path
from home import views

urlpatterns = [
    path('calendar/', views.calendar),
    path('mailbox/', views.mailbox),

]
