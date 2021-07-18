from django import template

from ..models import Menu, MenuSet

register = template.Library()


@register.inclusion_tag('hairsalon/components/menu_card.html')
def get_set_menus():
    return {'menus': MenuSet.objects.all()}


@register.inclusion_tag('hairsalon/components/menu_card.html')
def get_menus_filtered_by_category(category):
    return {'menus': Menu.objects.all().filter(category=category)}