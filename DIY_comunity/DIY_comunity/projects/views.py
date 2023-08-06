from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import render
from django.views import generic as views


def user_can_edit_or_delete(user, project):
    return user == project.creator


class ListUserProjects(views.ListView):
    pass


class AddProject(views.CreateView):
    pass


class ProjectDetails(views.DetailView):
    pass


class ProjectEdit(UserPassesTestMixin, views.UpdateView):
    pass

    # def test_func(self):
    #     project = self.get_object()
    #     return user_can_edit_or_delete(self.request.user, project)


class ProjectDelete(UserPassesTestMixin, views.DeleteView):
    pass

    # def test_func(self):
    #     project = self.get_object()
    #     return user_can_edit_or_delete(self.request.user, project)
