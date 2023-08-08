from django.shortcuts import render
from django.views import generic as views

from DIY_comunity.categories.models import CategoryModel


# Create your views here.

class CategoriesListView(views.ListView):
    model = CategoryModel
    template_name = 'categories/categories-list-page.html'  # Replace with your template name
    context_object_name = 'categories'


class CategoryProjectsListView(views.DetailView):
    model = CategoryModel
    template_name = 'categories/category-projects-list-page.html'  # Replace with your template name
    context_object_name = 'category'
