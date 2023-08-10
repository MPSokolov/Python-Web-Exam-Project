from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.forms import inlineformset_factory, modelformset_factory
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import generic as views

from DIY_comunity.common.forms import CommentForm
from DIY_comunity.projects.forms import ProjectForm
from DIY_comunity.projects.models import ProjectModel

UserModel = get_user_model()


def user_can_edit_or_delete(user, project):
    return user == project.creator


# class ListUserProjects(views.ListView):
#     model = ProjectModel
#     template_name = 'projects/user-projects-page.html'
#     context_object_name = 'projects'
#
#     # paginate_by = 10
#
#     def get_queryset(self):
#         username = self.kwargs['username']
#         user = get_object_or_404(UserModel, username=username)
#         return user.projectmodel_set.order_by('-created_at')


class AddProject(LoginRequiredMixin, views.CreateView):
    model = ProjectModel
    form_class = ProjectForm
    template_name = 'projects/project-add-page.html'

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        form.instance.creator = self.request.user
        return form

    def get_success_url(self):
        return reverse('profile details', kwargs={'username': self.request.user.username})


class ProjectDetails(views.DetailView):
    model = ProjectModel
    template_name = 'projects/project-details-page.html'
    context_object_name = 'project'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        context['comments'] = self.get_object().commentmodel_set.all().order_by('-created_at')
        context['liked_by_user'] = self.get_object().likemodel_set.filter(user=self.request.user).exists()
        context['bookmarked_by_user'] = self.get_object().bookmarkmodel_set.filter(user=self.request.user).exists()
        return context


class ProjectEdit(UserPassesTestMixin, views.UpdateView):
    model = ProjectModel
    form_class = ProjectForm
    template_name = 'projects/project-edit-page.html'
    context_object_name = 'project'

    def test_func(self):
        project = self.get_object()
        return user_can_edit_or_delete(self.request.user, project)

    def get_success_url(self):
        return reverse('project details', kwargs={'slug': self.get_object().slug})


class ProjectDelete(UserPassesTestMixin, views.DeleteView):
    model = ProjectModel
    template_name = 'projects/project-delete-page.html'
    context_object_name = 'project'

    def test_func(self):
        project = self.get_object()
        return user_can_edit_or_delete(self.request.user, project)

    def get_success_url(self):
        username = self.object.creator.username
        return reverse('profile details', kwargs={'username': username})