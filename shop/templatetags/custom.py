from django import template

register = template.Library()


@register.simple_tag
def multiply(value1, value2):
    return value1 * value2


@register.simple_tag
def hello_user(user):
    return f"Привет {user}! Добро пожаловать на сайт)"


@register.filter(name='underscore')
def underscore(value):
    return value.replace(' ', '_')


@register.filter(name='reverse')
def reverse(value):
    return value[::-1]
