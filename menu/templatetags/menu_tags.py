from django import template
from ..models import Menu, MenuElement

register = template.Library()


@register.inclusion_tag('menu_template.html')
def draw_menu(name, context):
	menu_elements = MenuElement.objects.filter(menu__name=name).order_by('path')
	return {'menu_elements': menu_elements, 'context': context}