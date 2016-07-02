from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.contrib.auth.models import User, Group, GroupManager
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.core.urlresolvers import reverse
from .models import FACULTY_CHOICES, DeveloperForm, Developer, Camps, FileUploadForm, Resources as ResourceModel, \
    FormModel, ResourceCategory, Posts
from django.conf import settings
from django.db.models import Q


# Create your views here.

def authentication(function):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated():
            return redirect("/")
        return function(request, *args, **kwargs)

    return wrapper


@authentication
def home(request):
    is_developer = request.user.groups.filter(name="Developers").exists()
    pageTitle = "Developers' Cell"
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
    campsBelongto = None
    posts = Posts.objects.all().order_by('-datetime')
    is_developer = request.user.groups.filter(name="Developers").exists()
    is_mentor = request.user.groups.filter(name="Mentors").exists()
    if is_developer:
        title = request.user.developer.camp
    elif is_mentor:
        campsBelongto = request.user.mentor.camp.all()
        title = campsBelongto.first()
    else:
        campsBelongto = Camps.objects.all()
        title = campsBelongto.first()
    if request.method == 'POST':
        Posts.objects.create(
            user = request.user,
            text=request.POST['text'],
            camp=Camps.objects.get(id=request.POST['camp']),
        )
    context = {'title': title, 'posts': posts, "is_developer": is_developer, "is_mentor": is_mentor,
               'campsbelongto': campsBelongto}

    return render(request, 'portal/camp.html', context)


def Logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('portal:root', args=''))


@authentication
def ResourcesSearch(request, searchString):
    return reverse(Resources, args=searchString)


@authentication
def Resources(request):
    resources = ResourceModel
    categories = ResourceCategory.objects.all()
    query = request.GET.get('searchbox')
    if query:
        resourcesObjects = ResourceModel.objects.filter(Q(title__icontains=query)).distinct()
    else:
        resourcesObjects = ResourceModel.objects.all()
    pagetitle = 'Resources'
    listofCamps = Camps.objects.all()
    recent_additions = ResourceModel.objects.all().order_by("-timestamp")[:5]
    is_developer = request.user.groups.filter(name="Developers").exists()

    context = {'title': pagetitle, 'resources': resources, 'is_developer': is_developer,
               'resourcesObjects': resourcesObjects, 'Camps': listofCamps, 'recent': recent_additions,
               'categories': categories}

    if not is_developer:
        if request.method == "POST":
            form = FileUploadForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()

        form = FileUploadForm()
        context['form'] = form
    return render(request, 'portal/resources.html',
                  context)


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


class PostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['text', 'camp']
