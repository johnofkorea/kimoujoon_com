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



class Tdate(models.Model):
    """
    김어준 생각이 있는 날짜. 여기에 Thought 를 채워넣어야 함.
    """
    date = models.DateField()
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



class Person(models.Model):
    """
    사람.
    """
    user = models.OneToOneField(User)
    following = models.ManyToManyField('self', through='PersonRelationship', symmetrical=False, related_name='followed_by')
    contribution_en = models.IntegerField(default=0, null=True, blank=True)
    contribution_fr = models.IntegerField(default=0, null=True, blank=True)
    contribution_jp = models.IntegerField(default=0, null=True, blank=True)
    contribution_kr = models.IntegerField(default=0, null=True, blank=True)
    level = models.IntegerField(default=10)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Person'
        verbose_name_plural = 'Person'
        ordering = ['-id']

    def __str__(self):
        return u'%s | %s | En %s | Fr %s | Jp %s | Kr %s | %s' % (
            self.id,
            self.user.username,
            self.contribution_en,
            self.contribution_fr,
            self.contribution_jp,
            self.contribution_kr,
            self.level,
        )

    def count_contribution(self):
        self.contribution_en = self.user.thoughten_set.filter(is_valid=True).count()
        self.contribution_fr = self.user.thoughtfr_set.filter(is_valid=True).count() 
        self.contribution_jp = self.user.thoughtjp_set.filter(is_valid=True).count() 
        self.contribution_kr = self.user.thoughtkr_set.filter(is_valid=True).count()
        self.save()


    def follow_person(self, person):
        relationship, created = PersonRelationship.objects.get_or_create(
            from_person=self,
            to_person=person,
        )

    # 사람 얻기. 세 가지 파라미터가 필요하다. 1. 그는 누구냐 2. 내가 따르냐 나를 따르냐 3. 나는 그에게 누구냐.
    def get_person(self, im_following_or_followed_by=d.FOLLOWING):
        "나와 관계있는 사람을 구한다."
        if im_following_or_followed_by == d.FOLLOWING:  # 내가 따라가는 사람이라면,
            return list(
                map(
                    lambda x: x.to_person,
                    PersonRelationship.objects.filter(
                        from_person=self,
                    ).order_by('to_person__id')
                )
            )
        else:  # 나를 따라오는 사람이라면,
            return list(
                map(
                    lambda x: x.from_person,
                    PersonRelationship.objects.filter(
                        to_person=self,
                    ).order_by('from_person__id')
                )
            )

    def unfollow_person(self, person):
        PersonRelationship.objects.get(from_person=self, to_person=person).delete()




class PersonRelationship(models.Model):
    from_person = models.ForeignKey(Person, related_name='from_people')
    to_person = models.ForeignKey(Person, related_name='to_people')
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

