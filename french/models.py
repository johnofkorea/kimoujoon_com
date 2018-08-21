# -*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from kimoujoonj.models import Media, Tmonth, Tdate
from kimoujoonj import d





class ThoughtFr(models.Model):
    """
    프랑스어 김어준 생각
    """
    userKey = models.ForeignKey(User, default=1)
    date = models.DateField()

    mediaKey = models.ForeignKey(Media, default=1)
    title = models.CharField(max_length=512, blank=True, null=True)
    content = models.TextField()
    
    tmonthKey = models.ForeignKey(Tmonth, blank=True, null=True) 
    tdateKey = models.ForeignKey(Tdate, blank=True, null=True)
    is_valid = models.BooleanField(default=False)
    priority = models.IntegerField(default=0)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Thought'
        verbose_name_plural = 'Thought'
        ordering = ['mediaKey__id', '-date', ]

    def __str__(self):
        return u'%s | %s | %s | %s' % ( 
            self.userKey.username,
            self.date,
            self.mediaKey.title_kr,
            self.title,
        )  



class PressFr(models.Model):
    """
    신문사들
    """
    url = models.CharField(max_length=256)
    title = models.CharField(max_length=512)
    content = models.TextField(blank=True, null=True)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Press'
        verbose_name_plural = 'Press'
        ordering = ['title', ]

    def __str__(self):
        return u'%s | %s | %s' % ( 
            self.id,
            self.title,
            self.url,
        )  



class NewsFr(models.Model):
    """
    해당 날짜 김어준 생각과 관련있는 신문기사.
    """
    userKey = models.ForeignKey(User, default=1)
    pressKey = models.ForeignKey(PressFr, default=1)
    thoughtKey = models.ForeignKey(ThoughtFr)
    date = models.DateField()
    
    language = models.IntegerField(choices=d.LANGUAGES, default=d.KOREAN)
    url = models.CharField(max_length=256)
    picture_url = models.CharField(max_length=256, blank=True, null=True)
    title = models.CharField(max_length=256)
    content = models.TextField(blank=True, null=True)
    commentary = models.TextField(blank=True, null=True)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'
        ordering = ['-date', '-id', ]

    def __str__(self):
        return u'%s | %s | %s | %s | %s | %s' % ( 
            self.userKey.username,
            self.date,
            self.language,
            self.pressKey.title,
            self.title,
            self.commentary,
        )  
