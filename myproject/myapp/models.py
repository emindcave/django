# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

# 模型和数据库，创建通讯录模型
class WorkMate (models.Model):

	GENDER_CHOICES = (
        (u'M', u'Male'),
        (u'F', u'Female'),
    )

	name = models.CharField(max_length=30)
	hiredate = models.DateTimeField()
	gender = models.CharField(max_length=2,choices=GENDER_CHOICES)
	dept = models.CharField(max_length=50)
	tel = models.CharField(max_length=30)
	email = models.EmailField()