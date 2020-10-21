from django import template
from blog.models import Category
register = template.Library()


@register.inclusion_tag('partials/categories.html')
def show_categories():
    categories = Category.objects.order_by('name')[:2]
    return {'categories': categories}
