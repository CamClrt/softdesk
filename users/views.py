from django.contrib.auth.models import User
from rest_framework import viewsets

from users.serializers import UserSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()
