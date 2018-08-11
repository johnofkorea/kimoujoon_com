# -*- coding:utf-8 -*-
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
import datetime
import json



def home(request):
    context = { 
    }
    return render(request, 'en/home.html', context)

