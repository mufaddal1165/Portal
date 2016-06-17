from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
import datetime


# Create your models here.
class Camps(models.Model):
    name = models.CharField(max_length=20, verbose_name='Camp', help_text='The groups based on languages taught')

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
    whyjoin = models.CharField(max_length=500, verbose_name="Why do you want to join Developers' Cell")
    languagesKnown = models.CharField(choices=LANGUAGES_AND_FRAMEWORKS, verbose_name="Languages and Frameworks Known",
                                      max_length=60)


class Executive(Users):
    class Meta:
        verbose_name = "Executive"


class Resources(models.Model):
    CATEGORY = (
        ('VD', 'Video'),
        ('BK', 'Book'),
        ('WEB', 'Website'),
        ('DOC', 'Document'),
        ('IMG','Image')
    )

    category = models.CharField(max_length=20, verbose_name='Category', choices=CATEGORY)
    camp = models.ForeignKey(Camps, verbose_name='Camp')
    link = models.FileField(upload_to='uploads')
    title = models.CharField(max_length=60, verbose_name='Name')

    class Meta:
        verbose_name = 'Resource'

    def __str__(self):
        return self.title


class DeveloperForm(ModelForm):
    class Meta:
        model = Developer
        fields = ['name', 'regNo', 'faculty', 'camp', 'previousExperience', 'whyjoin', 'languagesKnown']


class FileUploadForm(ModelForm):
    class Meta:
        model = Resources
        fields = ['title', 'link', 'category', 'camp', ]


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
    description = models.CharField(max_length=1000, verbose_name="Description")
    user = models.ForeignKey(User, verbose_name='User')
    datetime = models.DateTimeField(verbose_name='Time', auto_now=datetime.timedelta)

    def __str__(self):
        return self.title


class ForumThreads(models.Model):
    topic = models.ForeignKey(ForumTopics, on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name="User")
    datetime = models.DateTimeField(verbose_name="Time", auto_now=datetime.time)
    text = models.CharField(max_length=5000, verbose_name='Text')
    images = models.ImageField(null=True, upload_to='uploads')

class Posts(models.Model):
    text = models.CharField(max_length=5000)
    datetime=models.DateTimeField(auto_now=datetime.time)
    camp=models.ForeignKey(Camps)
    attachment = models.OneToOneField(Resources)