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



@register.simple_tag(takes_context=True)
def color_keyword(context, content, keyword):
    "content 와 keyword 를 받아서, content 속의 keyword 에 노란색 하이라이트를 주도록 한다."
    import re

    content = content.replace('\n', '<br />')
    insensitive_keyword = re.compile(re.escape(keyword), re.IGNORECASE) 
    content = insensitive_keyword.sub('<span style="background-color:yellow">' + keyword + '</span>', content)
    return mark_safe(content)

