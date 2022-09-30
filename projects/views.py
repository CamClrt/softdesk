from rest_framework import permissions, viewsets

from projects.models import Project
from projects.serializers import ProjectSerializer
from users.permissions import IsOwnerOrReadOnly


class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get_queryset(self):
        return Project.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
