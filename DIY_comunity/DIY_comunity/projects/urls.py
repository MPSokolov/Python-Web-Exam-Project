"""
URL configuration for DIY_comunity project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from DIY_comunity.projects.views import ListUserProjects, AddProject, ProjectDetails, ProjectEdit, ProjectDelete

urlpatterns = [
    path('<str:username>/', ListUserProjects.as_view(), name='list user projects'),
    path('add/', AddProject.as_view(), name="add project"),
    path('<slug:slug>/', include([
        path('', ProjectDetails.as_view(), name="project details"),
        path('edit/', ProjectEdit.as_view(), name="project edit"),
        path('delete/', ProjectDelete.as_view(), name="project delete"),
    ]))
]