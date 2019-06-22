from django.urls import path
from meeting import views

urlpatterns = [
    path('view_room/', views.view_room),


]