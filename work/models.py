# -*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from kimoujoonj.models import Media



class Stage(models.Model):
    """
    지금 이 작업이 어디에 있나.
    """
    num = models.IntegerField()
    title = models.CharField(default='', max_length=256)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Stage"
        ordering = ['num', 'id']

    def __str__(self):
        return u'%s | %s | %s' % (
            self.id,
            self.num,
            self.title,
        )



class TempThought(models.Model):
    """
    김어준 생각 임시. 여기서 승인이 되면 진짜 김어준 생각으로 옮긴다.
    """
    userKey = models.ForeignKey(User)
    date = models.DateField()
    stageKey = models.ForeignKey(Stage)

    mediaKey = models.ForeignKey(Media)
    reply = models.ManyToManyField('self', through='TempThoughtRelationship', symmetrical=False, related_name='replied_by')
    title_kr = models.CharField(max_length=256, blank=True, null=True)
    title_en = models.CharField(max_length=256, blank=True, null=True)
    
    abstract_kr = models.TextField(blank=True, null=True)
    abstract_en = models.TextField(blank=True, null=True)
    
    content_kr = models.TextField()
    content_en = models.TextField(blank=True, null=True)

    count = models.IntegerField(default=0)
    repliy_to = models.IntegerField(default=0)

    is_reply = models.BooleanField(default=False)
    is_valid = models.BooleanField(default=False)
    is_finished = models.BooleanField(default=False)
    is_moved = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Thought'
        verbose_name_plural = 'Thought'
        ordering = ['mediaKey__id', 'date', ]

    def __str__(self):
        return u'%s | %s | %s | %s | %s (%s / %s / %s)' % ( 
            self.userKey.username,
            self.date,
            self.mediaKey.title,
            self.title_kr,
            self.abstract_kr,
            self.is_valid,
            self.is_finished,
            self.is_moved,
        )  

    def reply(self, tt):
        relationship, created = TempThoughtRelationship.objects.get_or_create(
            from_tt=self,
            to_tt=tt,
        )
        tt.count = tt.count + 1
        tt.save()

    def get_reply(self):
        "이 글의 답글을 찾는다"
        return list(
            map(
                lambda x: x.from_tt,
                TempThoughtRelationship.objects.filter(
                    to_tt=self,
                ).order_by('from_tt__id')
            )
        )

    def get_host_tt(self):
        "이 글이 답글 단 원 문장을 찾는다"
        return list(
            map(
                lambda x: x.to_tt,
                TempThoughtRelationship.objects.filter(
                    from_tt=self,
                ).order_by('to_tt__id')
            )
        )
        
    def unreply(self, tt):
        TempThoughtRelationship.objects.get(from_tt=self, to_tt=tt).delete()
        tt.count = tt.count - 1
        tt.save()



class TempThoughtRelationship(models.Model):
    from_tt = models.ForeignKey(TempThought, related_name='from_tt')
    to_tt = models.ForeignKey(TempThought, related_name='to_tt')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
