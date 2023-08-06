from django.shortcuts import render
from django.views import generic as views


class ListUserProjects(views.ListView):
    pass


class AddProject(views.CreateView):
    pass


class ProjectDetails(views.DetailView):
    pass


class ProjectEdit(views.UpdateView):
    pass


class ProjectDelete(views.DeleteView):
    pass