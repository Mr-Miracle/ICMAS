from django.shortcuts import render, redirect
from meeting.models import *
# Create your views here.


def view_room(req):
    if req.session.get('user'):
        return render(req, 'view_room.html')
    return redirect('/login/')


def add(req):
    pass


def modify(req):
    pass


def delete(req):
    pass

