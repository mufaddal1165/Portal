import rest_framework
from rest_framework import serializers, viewsets
from rest_framework.generics import ListAPIView
from portal.models import Resources, Camps, Developer, ForumThreads, ForumTopics, Mentor, User, Posts, ResourceCategory


class ResourceCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ResourceCategory
        fields = ('name',)


class ResourceCategoryViewSet(viewsets.ModelViewSet):
    queryset = ResourceCategory.objects.all()
    serializer_class = ResourceCategorySerializer


class MentorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Mentor


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
        fields = ('url', 'username', 'email',)


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


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Posts
        fields = ('text', 'datetime', 'attachment', 'camp')


class PostViewSet(viewsets.ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class = PostSerializer
