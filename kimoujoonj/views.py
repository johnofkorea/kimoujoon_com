# -*- coding:utf-8 -*-
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
import datetime
import json

from .models import Thought


def home(request):
    thought = Thought.objects.all().order_by('-date')[0]
    context = { 
        'thought': thought,
    }
    return render(request, 'home.html', context)



def newsfactory(request, year_month):
    year_month = year_month.replace('/', '')
    year = int(year_month.split('_')[0])
    month = int(year_month.split('_')[1])

    thoughts = Thought.objects.filter(date__year=year, date__month=month).order_by('-date')
    context = { 
        'thoughts': thoughts,
    }
    return render(request, 'newsfactory.html', context)
