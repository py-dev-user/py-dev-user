from django import template

register = template.Library()


@register.filter(name='rev_str')
def revers_string(value):
    return value[::-1]


@register.filter(name='trunc_desc')
def truncate_description(value):
    idx = value.find('<hr />')
    if idx < 0:
        short_desc = value
    else:
        short_desc = value[: idx] + '<span class="h3">&#8230;</span>'
    return short_desc
