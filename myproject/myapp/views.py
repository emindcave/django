# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
import datetime
from models import *
# Create your views here.

# hello 视图，向网页返回一句话
def hello (request):
    return HttpResponse("django says helloworld")


# current_time视图，在网页上显示当前时间
def current_time (request):
    now = datetime.datetime.now()
    html = "<html><body><h1>The Current Time</h1><p>It is now %s.</p></body></html>" %now

    return HttpResponse(html)


def index (request):
    return render(request, "index.html")


def contact (request):
    contacts =  WorkMate.objects.all()
    context_dist = {'contacts':contacts}

    return render(request,"temp.html",context_dist)
