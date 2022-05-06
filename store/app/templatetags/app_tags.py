from app.models import *
from django import template

register = template.Library()


@register.inclusion_tag('app/categories.html', name='show_cats')
def show_categories(sort=None):
    if sort:
        cats = Category.objects.order_by(sort)
    else:
        cats = Category.objects.all()
    return {'cats': cats}
