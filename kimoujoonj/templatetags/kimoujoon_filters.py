# -*- coding:utf-8 -*-
from django import template
from django.http import QueryDict
from django.utils.safestring import mark_safe
from django.db.models import Count, Min, Sum, Avg
from django.contrib.auth.models import User
import datetime


register = template.Library()


@register.filter(name='agent_name')
def agent_name(request):
    "agent 의 이름이 무엇인지 반환한다."
    if 'Android' in request.META['HTTP_USER_AGENT']:
        return 'Android'
    elif 'Apple' in request.META['HTTP_USER_AGENT']:
        return 'iPhone'
    else:
        return ''
