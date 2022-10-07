from django.contrib.auth.models import User
from rest_framework import serializers

from projects.models import Project


class UserSerializer(serializers.ModelSerializer):
    # projects = serializers.PrimaryKeyRelatedField(many=True, queryset=Project.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'email']
