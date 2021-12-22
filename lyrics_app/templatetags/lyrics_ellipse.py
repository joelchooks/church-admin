from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter
def lyrEll(value):
    value = value[0:18]
    secondVal = value.replace("\n", " ").replace("\r", " ")
    
    if secondVal[len(secondVal)-1] == " ":
        newValue = secondVal.strip()
        return newValue + '...'
    else:
        return secondVal[:-1] + '...'