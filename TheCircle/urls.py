"""TheCircle URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from portal import views
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from portal.models import Developer, Resources, Mentor, Executive, Camps, ForumTopics, ForumThreads
import os
from django.conf import settings
from django.conf.urls.static import static
from api import CampSerializer, CampViewSet, DeveloperSerializer, DeveloperViewSet, ForumThreadsSerializer, \
    ForumThreadsViewSet, UserSerializer, UserViewSet, ForumTopicsSerializer, ForumTopicsViewSet, ResourceViewSet, \
    ResourceSerializer, ResourceCategorySerializer, ResourceCategoryViewSet

router = routers.DefaultRouter()
router.register(r'User', UserViewSet)
router.register(r'Developer', DeveloperViewSet)
router.register(r'Resource', ResourceViewSet)
router.register(r'Camps', CampViewSet)
router.register(r'ForumThreads', ForumThreadsViewSet)
router.register(r'ForumTopics', ForumTopicsViewSet)
# router.register(r'Posts', PostViewSet)
router.register(r'ResourceCategory', ResourceCategoryViewSet)
app_name = 'portal'
urlpatterns = [
                  url(r'^admin/', admin.site.urls),
                  url(r'^', include('portal.urls')),
                  url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
                  url(r'^api', include(router.urls)),

                  # url('^uploads',r'E:/uploads/uploads')
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL,
                                                                                         document_root=settings.STATIC_ROOT)
