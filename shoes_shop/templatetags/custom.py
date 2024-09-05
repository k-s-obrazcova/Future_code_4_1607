from django import template
from django.conf import settings

register = template.Library()


@register.simple_tag(name='company')
def company():
    return settings.NAME_COMPANY
