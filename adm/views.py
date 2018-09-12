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



def input(request):

    import datetime
    from kimoujoonj.models import Media, Tdate
    from english.models import TmonthEn, ThoughtEn
    from french.models import TmonthFr, ThoughtFr
    from japanese.models import TmonthJp, ThoughtJp
    from korean.models import TmonthKr, ThoughtKr

    if not request.user.is_authenticated():
        return redirect('/accounts/login/')

    if request.user.username != 'john':
        return redirect('/')
    
    if request.method == 'POST':
        if request.POST.get('content'):
            user_id = request.POST.get('user_id')
            year = request.POST.get('year')
            month = request.POST.get('month')
            day = request.POST.get('day')
            language = request.POST.get('language')
            title = request.POST.get('title')
            content = request.POST.get('content')

            user = User.objects.get(id=user_id)
            date = datetime.datetime.strptime(year + month + day, "%Y%m%d").date()
            tdate, created = Tdate.objects.get_or_create(date=date)
            
            if language == 'kr':
                tmonth, created = TmonthKr.objects.get_or_create(year=int(year), month=int(month))
                tdate.is_in_korean = True
                tdate.save()
                try:
                    t = ThoughtKr.objects.get(date=date)
                except:
                    t = ThoughtKr.objects.create(
                        userKey=user,
                        date=date,
                        mediaKey=Media.objects.get(id=1),
                        title=title,
                        content=content,
                        tmonthKey=tmonth,
                        tdateKey=tdate,
                        is_valid=True,
                        priority=99,
                    )
            elif language == 'en':
                tmonth, created = TmonthEn.objects.get_or_create(year=int(year), month=int(month))
                tdate.is_in_english = True
                tdate.save()
                try:
                    t = ThoughtEn.objects.get(date=date)
                except:
                    t = ThoughtEn.objects.create(
                        userKey=user,
                        date=date,
                        mediaKey=Media.objects.get(id=1),
                        title=title,
                        content=content,
                        tmonthKey=tmonth,
                        tdateKey=tdate,
                        is_valid=True,
                        priority=99,
                    )    
            elif language == 'fr':
                tmonth, created = TmonthFr.objects.get_or_create(year=int(year), month=int(month))
                tdate.is_in_french = True
                tdate.save()
                try:
                    t = ThoughtFr.objects.get(date=date)
                except:
                    t = ThoughtFr.objects.create(
                        userKey=user,
                        date=date,
                        mediaKey=Media.objects.get(id=1),
                        title=title,
                        content=content,
                        tmonthKey=tmonth,
                        tdateKey=tdate,
                        is_valid=True,
                        priority=99,
                    ) 
            elif language == 'jp':
                tmonth, created = TmonthJp.objects.get_or_create(year=int(year), month=int(month))
                tdate.is_in_japanese = True
                tdate.save()
                try:
                    t = ThoughtJp.objects.get(date=date)
                except:
                    t = ThoughtJp.objects.create(
                        userKey=user,
                        date=date,
                        mediaKey=Media.objects.get(id=1),
                        title=title,
                        content=content,
                        tmonthKey=tmonth,
                        tdateKey=tdate,
                        is_valid=True,
                        priority=99,
                    )       

    context = {
        'users': User.objects.all(),
    }
    return render(request, 'adm/input.html', context)
