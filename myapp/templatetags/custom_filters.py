from django import template

register = template.Library()

@register.filter
def slugify(value):
    return value.replace(" ", "-").replace("/", "-").replace(".", "-")