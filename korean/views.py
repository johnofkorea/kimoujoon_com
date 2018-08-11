# -*- coding:utf-8 -*-
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
import datetime
import json

from .models import ThoughtKr as Thought



def home(request):
    thought = Thought.objects.all().order_by('-date')[0]
    context = { 
        'thought': thought,
    }
    return render(request, 'kr/home.html', context)



def newsfactory(request, year_month):
    year_month = year_month.replace('/', '')
    year = int(year_month.split('_')[0])
    month = int(year_month.split('_')[1])

    thoughts = Thought.objects.filter(date__year=year, date__month=month).order_by('-date')
    context = { 
        'thoughts': thoughts,
    }
    return render(request, 'kr/newsfactory.html', context)



def search(request):
    if request.method == 'GET':
        keyword = request.GET.get('search')
        thoughts = Thought.objects.filter(content__icontains=keyword).order_by('-date')

    context = { 
        'thoughts': thoughts,
        'keyword': keyword,
    }
    return render(request, 'kr/search_result.html', context)

