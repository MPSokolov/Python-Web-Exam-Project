from django.contrib.auth.mixins import UserPassesTestMixin
from django.forms import inlineformset_factory, modelformset_factory
from django.urls import reverse_lazy
from django.views import generic as views

from DIY_comunity.projects.forms import ProjectForm
from DIY_comunity.projects.models import ProjectModel


def user_can_edit_or_delete(user, project):
    return user == project.creator


class ListUserProjects(views.ListView):
    pass


class AddProject(views.CreateView):
    pass


class ProjectDetails(views.DetailView):
    pass


class ProjectEdit(UserPassesTestMixin, views.UpdateView):
    model = ProjectModel
    form_class = ProjectForm
    template_name = 'projects/project-edit-page.html'  # Replace with your template
    # success_url = reverse_lazy('project_list')

    def test_func(self):
        project = self.get_object()
        return user_can_edit_or_delete(self.request.user, project)


class ProjectDelete(UserPassesTestMixin, views.DeleteView):
    pass

    # def test_func(self):
    #     project = self.get_object()
    #     return user_can_edit_or_delete(self.request.user, project)
