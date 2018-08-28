# -*- coding:utf-8 -*-
from django.contrib.auth.models import User
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils import timezone
import datetime
import json

from kimoujoonj.models import Person


def home(request):

    if not request.user.is_authenticated():
        return redirect('/accounts/login/')

    if request.user.username != 'john':
        return redirect('/')

    context = {
    }
    return render(request, 'adm/home.html', context)



def count_contribution(request):

    if not request.user.is_authenticated():
        return redirect('/accounts/login/')

    if request.user.username != 'john':
        return redirect('/')

    persons = Person.objects.all()
    for person in persons:
        person.count_contribution()

    context = {
    }
    return render(request, 'adm/home.html', context)
