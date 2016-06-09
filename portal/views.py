from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.core.urlresolvers import reverse
from .models import FACULTY_CHOICES, DeveloperForm, Developer, Camps


# Create your views here.



def home(request):
    if not request.user.is_authenticated():
        return redirect("/")
    return render(request, 'portal/home.html', {})


def root(request):
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
    return render(request, 'portal/root.html', {'login': loginForm})


def TheCamp(request):
    if not request.user.is_authenticated():
        return HttpResponse("Login first please")
    else:
        return HttpResponse("Welcome to the Camp")


def Logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('portal:root', args=''))


def Resources(request):
    if not request.user.is_authenticated():
        return redirect("/")
    return HttpResponse("Welcome to resources section")


def SignUp(request):
    if request.method == "POST":
        user_new = User.objects.create_user(username=request.POST['username'],
                                            password=request.POST['password'],
                                            email=request.POST['email'])
        user_new.save()
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

    return render(request, 'portal/signup.html', {'form': form})


class LoginForm(forms.Form):
    username = forms.CharField(max_length=30, label='User Name')
    password = forms.CharField(max_length=20, label='Password', widget=forms.PasswordInput)
