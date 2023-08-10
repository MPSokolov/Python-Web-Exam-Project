from django.shortcuts import render, get_object_or_404
from django.views import generic as views

from DIY_comunity.categories.models import CategoryModel
from DIY_comunity.projects.models import ProjectModel


# Create your views here.

class CategoriesListView(views.ListView):
    model = CategoryModel
    template_name = 'categories/categories-list-page.html'
    context_object_name = 'categories'


class CategoryProjectsListView(views.ListView):
    model = ProjectModel
    template_name = 'categories/category-projects-list-page.html'
    context_object_name = 'projects'
    paginate_by = 8

    def get_queryset(self):
        category_slug = self.kwargs['slug']
        return ProjectModel.objects.filter(category__slug=category_slug)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = get_object_or_404(CategoryModel, slug=self.kwargs['slug'])
        return context
