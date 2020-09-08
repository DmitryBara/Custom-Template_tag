# TemplateTag which save context into variables
# Use in django templates ( for example menu_template.html) when
# you need to save some data outside of iteration cycles

from django import template

register = template.Library()

@register.simple_tag
def define(val=None):
  return val