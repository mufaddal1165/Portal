from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls import static
app_name = 'portal'
urlpatterns = [url(r'^home', views.home, name='home'),
               url('^$', views.root, name='root'),
               url(r'^logout', views.Logout, name='logout'),
               url(r'^camp', views.TheCamp, name='camp'),
               url(r'^resources', views.Resources, name='resources'),
               url(r'^signup', views.SignUp, name='signup'), ]
