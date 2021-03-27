from django import template

register = template.Library()


@register.filter(name='rev_str')
def revers_string(value):
    return value[::-1]
