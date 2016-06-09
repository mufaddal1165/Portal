from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


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


class Mentor(Users):
    camp = models.ManyToManyField(Camps)


class Developer(Users):
    """
    The students who sign up for the portal
    """
    FACULTY_CHOICES = (
        ('FES', 'Engineering Sciences'),
        ('FME', 'Mechanical Engineering'),
        ('FCSE', 'Computer Sciences and Engineering'),
    )

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
