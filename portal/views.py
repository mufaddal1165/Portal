from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.contrib.auth.models import User, Group, GroupManager
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.core.urlresolvers import reverse
from .models import FACULTY_CHOICES, DeveloperForm, Developer, Camps


# Create your views here.

def authentication(function):
    def wrapper(request):
        if not request.user.is_authenticated():
            return redirect("/")
        return function(request)

    return wrapper


@authentication
def home(request):
    is_developer = request.user.groups.filter(name="Developers").exists()
    pageTitle = "Home"
    return render(request, 'portal/home.html', {'is_developer': is_developer, 'title': pageTitle})


def root(request):
    if request.user.is_authenticated():
        return redirect("/home")
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('portal:home', args=""))
            else:
                return HttpResponse("User is not active")
        else:
            return HttpResponse("User not present")
    loginForm = LoginForm()

    return render(request, 'portal/root.html', {'login': loginForm,})


@authentication
def TheCamp(request):
    return HttpResponse("Welcome to the Camp")


def Logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('portal:root', args=''))


@authentication
def Resources(request):
    pagetitle = 'Resources'

    return render(request, 'portal/resources.html', {'title': pagetitle})


def SignUp(request):
    if request.method == "POST":
        user_new = User.objects.create_user(username=request.POST['username'],
                                            password=request.POST['password'],
                                            email=request.POST['email'])
        user_new.groups.add(Group.objects.get(name="Developers"))
        # user_new.groups.
        user_new.save()
        # user_new.groups.add(User.groups.get(name="Developers"))
        Developer.objects.create(regNo=request.POST['regNo'],
                                 name=request.POST['name'],
                                 faculty=request.POST['faculty'],
                                 camp=Camps.objects.get(pk=request.POST['camp']),
                                 previousExperience=request.POST['previousExperience'],
                                 whyjoin=request.POST['whyjoin'],
                                 languagesKnown=request.POST['languagesKnown'],
                                 user=user_new

                                 )
        return HttpResponse("Success")
    form = DeveloperForm()
    pageTitle = 'Signup'
    return render(request, 'portal/signup.html', {'form': form, 'title': pageTitle})


class LoginForm(forms.Form):
    username = forms.CharField(max_length=30, label='User Name')
    password = forms.CharField(max_length=20, label='Password', widget=forms.PasswordInput)
