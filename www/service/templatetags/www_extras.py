from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(name='link')
def link(value):
    return mark_safe(value.replace('{click}',' <a href="#contact-form" class="contact-action">Click here</a>'))
