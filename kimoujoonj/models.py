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



class Thought(models.Model):
    """
    김어준 생각
    """
    userKey = models.ForeignKey(User, default=1)
    date = models.DateField()

    mediaKey = models.ForeignKey(Media, default=1)
    title_kr = models.CharField(max_length=256, blank=True, null=True)
    title_en = models.CharField(max_length=256, blank=True, null=True)
    
    abstract_kr = models.TextField(blank=True, null=True)
    abstract_en = models.TextField(blank=True, null=True)
    
    content_kr = models.TextField()
    content_en = models.TextField(blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Thought'
        verbose_name_plural = 'Thought'
        ordering = ['mediaKey__id', '-date', ]

    def __str__(self):
        return u'%s | %s | %s | %s | %s' % ( 
            self.userKey.username,
            self.date,
            self.mediaKey.title_kr,
            self.title_kr,
            self.abstract_kr,
        )  



class Press(models.Model):
    """
    신문사들
    """
    url = models.CharField(max_length=256)
    title_kr = models.CharField(max_length=256)
    title_en = models.CharField(max_length=256, blank=True, null=True)
    
    content_kr = models.TextField(blank=True, null=True)
    content_en = models.TextField(blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Press'
        verbose_name_plural = 'Press'
        ordering = ['title_kr', ]

    def __str__(self):
        return u'%s | %s | %s' % ( 
            self.id,
            self.title_kr,
            self.url,
        )  



class NewsArticle(models.Model):
    """
    해당 날짜 김어준 생각과 관련있는 신문기사.
    """
    userKey = models.ForeignKey(User, default=1)
    pressKey = models.ForeignKey(Press, default=1)
    thoughtKey = models.ForeignKey(Thought)
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
        verbose_name = 'NewsArticle'
        verbose_name_plural = 'NewsArticle'
        ordering = ['-date', '-id', ]

    def __str__(self):
        return u'%s | %s | %s | %s | %s | %s' % ( 
            self.userKey.username,
            self.date,
            self.language,
            self.pressKey.title_kr,
            self.title,
            self.commentary,
        )  
