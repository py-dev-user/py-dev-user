from django import template

register = template.Library()


@register.simple_tag
def get_current_time():
    from datetime import datetime
    return datetime.now().strftime('%H:%M:%S %d-%m-%Y')
