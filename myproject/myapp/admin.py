# -*- coding:utf-8 -*-
from django.contrib import admin
from models import *
# Register your models here.

# showmate用于显示在admin显示模型数据列表
class ShowMate(admin.ModelAdmin):
	list_display = ("name","hiredate","gender","dept","tel","email")

# 注册模型
admin.site.register(WorkMate,ShowMate)