from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views import generic as views


# Create your views here.

class IndexView(views.ListView):
    pass


@login_required
def like_functionality(request, project_id):
    pass


@login_required
def bookmark_functionality(request, project_id):
    pass


@login_required
def comment_functionality(request, project_id):
    pass
