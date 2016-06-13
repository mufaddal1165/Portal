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


class CampSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Camps
        fields = ('name',)


class CampViewSet(viewsets.ModelViewSet):
    queryset = Camps.objects.all()
    serializer_class = CampSerializer


class ForumTopicsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ForumTopics
        fields = ('camp', 'title', 'description', 'user', 'datetime')


class ForumTopicsViewSet(viewsets.ModelViewSet):
    queryset = ForumTopics.objects.all()
    serializer_class = ForumTopicsSerializer


class ForumThreadsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ForumThreads
        fields = ('topic', 'user', 'datetime', 'text', 'images')


class ForumThreadsViewSet(viewsets.ModelViewSet):
    queryset = ForumThreads.objects.all()
    serializer_class = ForumThreadsSerializer


class ResourceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Resources
        fields = ('link', 'title', 'category', 'camp')


class ResourceViewSet(viewsets.ModelViewSet):
    queryset = Resources.objects.all()
    serializer_class = ResourceSerializer


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff',)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class DeveloperSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Developer
        fields = ('user', 'name')


class DeveloperViewSet(viewsets.ModelViewSet):
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer


router = routers.DefaultRouter()
router.register(r'User', UserViewSet)
router.register(r'Developer', DeveloperViewSet)
router.register(r'Resource', ResourceViewSet)
router.register(r'Camps', CampViewSet)
router.register(r'ForumThreads', ForumThreadsViewSet)
router.register(r'ForumTopics', ForumTopicsViewSet)
app_name = 'portal'
urlpatterns = [
                  url(r'^admin/', admin.site.urls),
                  url(r'^', include('portal.urls')),
                  url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
                  url(r'^API', include(router.urls)),
                  # url('^uploads',r'E:/uploads/uploads')
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
