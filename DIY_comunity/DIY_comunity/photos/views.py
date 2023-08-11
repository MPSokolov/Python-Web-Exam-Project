from django.contrib.auth.mixins import PermissionRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views import generic as views

from DIY_comunity.photos.forms import PhotoForm
from DIY_comunity.photos.models import PhotoModel
from DIY_comunity.projects.models import ProjectModel


def user_can_add_or_delete(user, project):
    return user == project.creator


class PhotoAdd(UserPassesTestMixin, views.CreateView):
    model = PhotoModel
    template_name = 'photos/photo-add-page.html'
    form_class = PhotoForm

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        project_slug = self.kwargs['slug']
        form.instance.project = get_object_or_404(ProjectModel, slug=project_slug)
        form.instance.creator = self.request.user
        return form

    def get_success_url(self):
        project_slug = self.kwargs['slug']
        return reverse('project details', kwargs={'slug': project_slug})

    def test_func(self):
        project_slug = self.kwargs['slug']
        project = get_object_or_404(ProjectModel, slug=project_slug)

        return user_can_add_or_delete(self.request.user, project)


class PhotoDelete(UserPassesTestMixin, views.DeleteView):
    model = PhotoModel
    template_name = 'photos/photo-delete-page.html'
    context_object_name = 'photo'

    def get_success_url(self):
        return reverse_lazy('project details', kwargs={'slug': self.object.project.slug})

    def test_func(self):
        project_slug = self.get_object().project.slug
        project = get_object_or_404(ProjectModel, slug=project_slug)

        return user_can_add_or_delete(self.request.user, project)