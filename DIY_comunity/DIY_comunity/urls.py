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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.defaults import permission_denied

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('DIY_comunity.common.urls')),
    path('accounts/', include('DIY_comunity.accounts.urls')),
    path('categories/', include('DIY_comunity.categories.urls')),
    path('photos/', include('DIY_comunity.photos.urls')),
    path('projects/', include('DIY_comunity.projects.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# handler403 = permission_denied
