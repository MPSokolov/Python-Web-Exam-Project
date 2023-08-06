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
from .views import IndexView, like_functionality, comment_functionality, bookmark_functionality
from django.urls import path, include

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('like/<int:project_id>/', like_functionality, name='like'),
    path('comment/<int:project_id>/', comment_functionality, name='comment'),
    path('bookmark/<int:project_id>/', bookmark_functionality, name='bookmark'),
]
