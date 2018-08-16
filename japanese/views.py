# -*- coding:utf-8 -*-
from django.contrib.auth.models import User
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
import datetime
import json

from .models import ThoughtJp as Thought



def home(request):
    thought = Thought.objects.all().order_by('-date')[0]
    context = { 
        'thought': thought,
    }
    return render(request, 'jp/home.html', context)



def newsfactory(request, year_month):
    year_month = year_month.replace('/', '')
    year = int(year_month.split('_')[0])
    month = int(year_month.split('_')[1])

    thoughts = Thought.objects.filter(date__year=year, date__month=month, is_valid=True).order_by('-date')
    context = { 
        'thoughts': thoughts,
    }
    return render(request, 'jp/newsfactory.html', context)



def thought(request, yy_mm_dd):
    yy_mm_dd = yy_mm_dd.replace('/', '')
    yy_mm_dd = datetime.datetime.strptime(yy_mm_dd, "%Y-%m-%d")
    
    thoughts = Thought.objects.filter(date=yy_mm_dd).order_by('mediaKey__id')
    context = { 
        'thoughts': thoughts,
    }
    return render(request, 'jp/thought.html', context)



def search(request):
    if request.method == 'GET':
        keyword = request.GET.get('search')
        thoughts = Thought.objects.filter(content__icontains=keyword).order_by('-date')

    context = { 
        'thoughts': thoughts,
        'keyword': keyword,
    }
    return render(request, 'jp/search_result.html', context)



def contributors(request):
    users = User.objects.all().order_by('first_name')
    context = { 
        'users': users,
    }
    return render(request, 'jp/contributors.html', context)



def contributor(request, user_id):
    user_id = user_id.replace('/', '')
    user = User.objects.get(id=user_id)
    thoughts = user.thoughtjp_set.filter(is_valid=True).order_by('-date')
    context = { 
        'thoughts': thoughts,
    }
    return render(request, 'jp/newsfactory.html', context)
