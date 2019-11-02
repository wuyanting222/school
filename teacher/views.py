# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

from teacher.models import Teacher


class TeacherCreate(View):
    def get(self, request):
        d = 'helloworld'

        teachers = Teacher.objects(id=1)[0:5]  #Teacher.objects.filter(deleted=0)[page * pagesize: pagesize * (page + 1)]

        json_data = serializers.serialize('json', teachers) #第二个参数就是 teachers
        json_data = json.loads(json_data)

        response = JsonResponse(json_data, safe=False) #第一个参数就是 返回个前端的字符串
        return response



