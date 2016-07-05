from django.contrib import admin
from .models import Developer, Mentor, Executive, Camps, Resources as ResourceModel, ResourceCategory
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from portal.models import Posts


# Register your models here.
class DeveloperInLine(admin.StackedInline):
    model = Developer


class ExecutiveInLine(admin.StackedInline):
    model = Executive


class MentorInLine(admin.StackedInline):
    model = Mentor


class UserAdmin(BaseUserAdmin):
    inlines = (ExecutiveInLine, DeveloperInLine, MentorInLine)


class Resource(admin.ModelAdmin):
    list_display = ['__str__', 'timestamp']

    class Meta:
        model = ResourceModel
        fields = ('title', 'timestamp', 'link', 'category', 'camp')


class PostAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'user','datetime']

    class Meta:
        model = Posts
        field = ('user', 'datetime', 'text', 'camp')


admin.site.register(Developer)
admin.site.register(Executive)
admin.site.register(Mentor)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Camps)
admin.site.register(ResourceModel, Resource)
admin.site.register(ResourceCategory)
admin.site.register(Posts,PostAdmin)
