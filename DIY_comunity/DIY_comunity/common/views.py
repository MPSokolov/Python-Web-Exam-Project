from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic as views

from DIY_comunity.common.forms import CommentForm
from DIY_comunity.common.models import LikeModel, BookmarkModel
from DIY_comunity.projects.models import ProjectModel


# Create your views here.

class IndexView(views.ListView):
    model = ProjectModel
    template_name = 'common/index.html'
    context_object_name = 'projects'
    paginate_by = 8

    def get_queryset(self):
        return super().get_queryset().order_by('-created_at')


@login_required
def like_functionality(request, project_id):
    project = ProjectModel.objects.get(pk=project_id)

    kwargs = {
        'project': project,
        'user': request.user
    }

    like_object = LikeModel.objects.filter(**kwargs).first()

    if like_object:
        like_object.delete()
    else:
        new_like_object = LikeModel(**kwargs)
        new_like_object.save()

    return redirect(request.META['HTTP_REFERER'] + f"#{project_id}")


@login_required
def bookmark_functionality(request, project_id):
    project = ProjectModel.objects.get(pk=project_id)

    kwargs = {
        'project': project,
        'user': request.user
    }

    bookmark_object = BookmarkModel.objects.filter(**kwargs).first()

    if bookmark_object:
        bookmark_object.delete()
    else:
        bookmark_object = BookmarkModel(**kwargs)
        bookmark_object.save()

    return redirect(request.META['HTTP_REFERER'] + f"#{project_id}")


@login_required
def comment_functionality(request, project_id):
    project = ProjectModel.objects.get(pk=project_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment_instance = form.save(commit=False)
            new_comment_instance.project = project
            new_comment_instance.user = request.user
            new_comment_instance.save()

        return redirect(request.META['HTTP_REFERER'] + f"#{project_id}")


class BookmarkedProjects(LoginRequiredMixin, views.ListView):
    model = BookmarkModel
    template_name = 'common/bookmarked-projects-page.html'
    context_object_name = 'projects'

    def get_queryset(self):
        user_bookmarks = BookmarkModel.objects.filter(user=self.request.user)
        projects = [bookmark.project for bookmark in user_bookmarks]
        return projects
