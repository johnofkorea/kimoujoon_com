# -*- coding:utf-8 -*-
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render, redirect
import json
import datetime

from seoulbestj.models import Info, Person
from english.models import Category, Chapter
from pad.models import WnoteAnswerLog
from .models import BookPersonLog, BookChapterPage, Wnote, WnoteVisitLog



def home(request):

    if not request.user.is_authenticated():
        return redirect('/accounts/login/')

    person = Person.objects.get(user=request.user) 
    person.calculate_score()

    picture = Info.objects.get(title='english_picture').content
    title = ''
    categories = Category.objects.filter(is_menu_shown=True).order_by('order')

    context = {
        'picture': picture,
        'categories': categories,
        'score': person.score,
    }
    return render(request, 'smath/home.html', context)



def journal(request):

    if not request.user.is_authenticated():
        return redirect('/accounts/login/')

    person = Person.objects.get(user=request.user) 
    person.calculate_score()

    picture = Info.objects.get(title='english_picture').content
    title = ''
    categories = Category.objects.filter(is_menu_shown=True).order_by('order')

    context = {
        'picture': picture,
        'categories': categories,
        'score': person.score,
    }
    return render(request, 'smath/home.html', context)



def wnotebook(request):

    if not request.user.is_authenticated():
        #return redirect('/smath/a_wnote/')
        return redirect('/accounts/login/')

    person = Person.objects.get(user=request.user) 
    #person.calculate_score()

    picture = Info.objects.get(title='english_picture').content
    title = ''

    context = {
        'picture': picture,
        'score': person.score,
        'books': BookPersonLog.objects.filter(personKey=request.user.person).order_by('-id'),
    }
    return render(request, 'smath/wnotebook.html', context)



def wnote(request, chapter_id):

    if not request.user.is_authenticated():
        return redirect('/accounts/login/')

    person = Person.objects.get(user=request.user) 
    #person.calculate_score()
    chapter = BookChapterPage.objects.get(id=chapter_id)
    picture = Info.objects.get(title='english_picture').content
    title = ''
    a_week_ago = datetime.datetime.today() - datetime.timedelta(days=7)

    context = {
        'picture': picture,
        'score': person.score,
        'wnotes': Wnote.objects.filter(userKey=request.user, chapterKey=chapter, created__lt=a_week_ago).order_by('-priority', 'date', 'page', 'updated', )
    }
    return render(request, 'smath/wnote.html', context)




def wrecord(request):

    
    context = {
    }
    return render(request, 'smath/wrecord.html', context)



def wnoteq(request, order):

    if not request.user.is_authenticated():
        return redirect('/accounts/login/')

    order = int(order.replace('/', ''))
    person = Person.objects.get(user=request.user) 
    #person.calculate_score()

    picture = Info.objects.get(title='english_picture').content
    title = ''
    categories = Category.objects.filter(is_menu_shown=True).order_by('order')
    wnotes = Wnote.objects.filter(userKey=request.user).order_by('-priority', 'date', 'page', 'updated', )
    wnote = wnotes[order - 1]
    answers = WnoteAnswerLog.objects.filter(userKey=request.user, wnoteKey=wnote).order_by('-id')
    WnoteVisitLog.objects.create(userKey=request.user, wnoteKey=wnote, date=datetime.datetime.today()) 
    
    
    if order > 1:
        prev_order = order - 1
    else: 
        prev_order = order

    if order < wnotes.count():
        next_order = order + 1
    else:
        next_order = order
    
    
    context = {
        'picture': picture,
        'categories': categories,
        'score': person.score,
        'wnote': wnote,
        'prev_order': prev_order,
        'next_order': next_order,
        'order': order,
        'answers': answers,
    }
    return render(request, 'smath/wnoteq.html', context)

