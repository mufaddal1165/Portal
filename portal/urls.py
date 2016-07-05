from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls import static
from django.contrib.auth.models import User

app_name = 'portal'
urlpatterns = [url(r'^home', views.home, name='home'),
               url('^$', views.root, name='root'),
               url(r'^logout', views.Logout, name='logout'),
               url(r'^camps/', views.camps, name='camps'),
               url(r'^camp/(?P<num>\d+)', views.TheCamp, name='camp'),
               url(r'^resources/$', views.Resources, name='resources'),
               url(r'^signup', views.SignUp, name='signup'),
               url(r'resourcesR/$', views.ResourcesSearch, name="resourcesearch"),
               url(r'^posts/$', views.CampView.as_view()),
               url(r'deleteresources/(?P<resource_id>\d)', views.deleteresources, name="deleteresources")
               ]
