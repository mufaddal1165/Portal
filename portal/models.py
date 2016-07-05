from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
import datetime
from django import forms


# Create your models here.
class Camps(models.Model):
    name = models.CharField(max_length=20, verbose_name='Camp', help_text='The groups based on languages taught')
    jumbotronImage = models.ImageField(upload_to='uploads', null=True)
    thumbnailImage = models.ImageField(upload_to='uploads', null=True)

    class Meta:
        verbose_name = 'Camp'

    def __str__(self):
        return "%s" % self.name


class Users(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, verbose_name="Name")

    class Meta:
        abstract = True

    def __str__(self):
        return "%s" % self.name


LANGUAGES_AND_FRAMEWORKS = (

    ('C#', 'C#'),
    ('C++', 'C++'),
    ('C', 'C'),
    ('JV', 'Java'),
    ('ANRD', 'Android'),
    ('Py', 'Python'),
    ('RB', 'Ruby'),
    ('JS', 'Javascript'),
    ('NJS', 'node.js'),
)

FACULTY_CHOICES = (
    ('FES', 'Engineering Sciences'),
    ('FME', 'Mechanical Engineering'),
    ('FCSE', 'Computer Sciences and Engineering'),
)
"""
This is a block comment :D
"""


class Mentor(Users):
    camp = models.ManyToManyField(Camps)


class Developer(Users):
    """
    The students who sign up for the portal
    """

    regNo = models.CharField(max_length=7,
                             verbose_name='Registration Number'
                             )
    faculty = models.CharField(choices=FACULTY_CHOICES, max_length=50)
    camp = models.ForeignKey(Camps, on_delete=models.CASCADE)
    previousExperience = models.BooleanField(default=True, verbose_name="Any previous Programming Experience")
    whyjoin = models.TextField(verbose_name="Why do you want to join Developers' Cell")
    languagesKnown = models.CharField(choices=LANGUAGES_AND_FRAMEWORKS, verbose_name="Languages and Frameworks Known",
                                      max_length=60)


class Executive(Users):
    class Meta:
        verbose_name = "Executive"


class ResourceCategory(models.Model):
    name = models.CharField(max_length=20, verbose_name='Category')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Resources(models.Model):
    category = models.ForeignKey(ResourceCategory)
    camp = models.ForeignKey(Camps, verbose_name='Camp')
    link = models.FileField(upload_to='uploads')
    title = models.CharField(max_length=60, verbose_name='Name')
    timestamp = models.DateTimeField(auto_now=True)
    description = models.TextField(null=True)
    user = models.ForeignKey(User)

    class Meta:
        verbose_name = 'Resource'
        ordering = ['-timestamp']

    def __str__(self):
        return "%s" % self.title


class DeveloperForm(ModelForm):
    class Meta:
        model = Developer
        fields = ['name', 'regNo', 'faculty', 'camp', 'previousExperience', 'whyjoin', 'languagesKnown']


class FileUploadForm(ModelForm):
    class Meta:
        model = Resources
        fields = ['title', 'link', 'description', 'category', 'camp', 'user']
        widgets = {'user': forms.HiddenInput()}


class ModelUpload(models.Model):
    thefile = models.FileField(upload_to='uploads')
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class FormModel(ModelForm):
    class Meta:
        model = ModelUpload
        fields = ['name', 'thefile']


class ForumTopics(models.Model):
    camp = models.ForeignKey(Camps, on_delete=models.CASCADE)
    title = models.CharField(max_length=300, verbose_name=
    "Title")
    description = models.TextField(max_length=1000, verbose_name="Description")
    user = models.ForeignKey(User, verbose_name='User')
    datetime = models.DateTimeField(verbose_name='Time', auto_now=datetime.timedelta)

    def __str__(self):
        return self.title


class ForumThreads(models.Model):
    topic = models.ForeignKey(ForumTopics, on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name="User")
    datetime = models.DateTimeField(verbose_name="Time", auto_now=datetime.time)
    text = models.TextField(max_length=5000, verbose_name='Text')
    images = models.ImageField(null=True, upload_to='uploads')


class Posts(models.Model):
    user = models.ForeignKey(User, default=None)
    text = models.TextField()
    datetime = models.DateTimeField(auto_now=datetime.time)
    camp = models.ForeignKey(Camps)

    class Meta:
        verbose_name = "Post"

    def __str__(self):
        return "%s"[:30] % self.text


class PosttoResources(models.Model):
    resource = models.OneToOneField(Resources)
    Post = models.ForeignKey(Posts, default=None)
