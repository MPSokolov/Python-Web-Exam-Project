from django import template

from DIY_comunity.categories.models import CategoryModel
from DIY_comunity.projects.models import ProjectModel

register = template.Library()


@register.simple_tag
def get_all_categories():
    return CategoryModel.objects.all()

