# -*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from . import d


class Media(models.Model):
    """
    김어준 생각이 어느 매체에 있나?
    """
    userKey = models.ForeignKey(User)
    
    title_kr = models.CharField(max_length=256)
    title_en = models.CharField(max_length=256, blank=True, null=True)
    
    content_kr = models.TextField(blank=True, null=True)
    content_en = models.TextField(blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Media'
        verbose_name_plural = 'Media'
        ordering = ['title_kr', ]

    def __str__(self):
        return u'%s | %s | %s' % ( 
            self.id,
            self.userKey.username,
            self.title_kr,
        )  



class Tmonth(models.Model):
    """
    김어준 생각이 있는 달. 각각 갯수를 파악하기 위해서임.
    """
    year = models.IntegerField(default=0)
    month = models.IntegerField(default=0)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Tmonth'
        verbose_name_plural = 'Tmonth'
        ordering = ['-year', '-month', ]

    def __str__(self):
        return u'%s | %s . %s' % ( 
            self.id,
            self.year,
            self.month,
        )  



class Tdate(models.Model):
    """
    김어준 생각이 있는 날짜. 여기에 Thought 를 채워넣어야 함.
    """
    date = models.DateField()
    tmonthKey = models.ForeignKey(Tmonth) 
    mediaKey = models.ForeignKey(Media, default=1)
    is_in_korean = models.BooleanField(default=False)
    is_in_english = models.BooleanField(default=False)
    is_in_french = models.BooleanField(default=False)
    is_in_japanese = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Tdate'
        verbose_name_plural = 'Tdate'
        ordering = ['mediaKey__id', '-date', ]

    def __str__(self):
        return u'%s | %s | %s | %s | %s | %s' % ( 
            self.date,
            self.mediaKey.title_kr,
            self.is_in_korean,
            self.is_in_english,
            self.is_in_french,
            self.is_in_japanese,
        )  
