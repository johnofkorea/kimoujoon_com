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



@register.simple_tag(takes_context=True)
def num_valid_thoughts(context, lang, tmonth):
    "해당 tmonth 에 속한, is_valid 한 김어준생각이 몇 개 있는지 반환한다."
    if lang == 'kr':
        return tmonth.thoughtkr_set.filter(is_valid=True).count()
    elif lang == 'en':
        return tmonth.thoughten_set.filter(is_valid=True).count()
    elif lang == 'fr':
        return tmonth.thoughtfr_set.filter(is_valid=True).count()
    elif lang == 'jp':
        return tmonth.thoughtjp_set.filter(is_valid=True).count()
    else:
        return -1


