from django import template

register = template.Library()


@register.filter
def makemoney(value):
    try:
        value = int(value)
        return "{:,}".format(value)
    except (ValueError, TypeError):
        return value
