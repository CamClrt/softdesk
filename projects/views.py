from rest_framework import permissions, viewsets

from projects.models import Project, Tag
from projects.serializers import ProjectSerializer, TagSerializer
from users.permissions import IsOwnerOrReadOnly


class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get_queryset(self):
        queryset = Project.objects.all()
        tag_id = self.request.GET.get('tag_id')
        if tag_id is not None:
            queryset = Project.objects.filter(tags=tag_id)
        return queryset

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class TagViewSet(viewsets.ModelViewSet):
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get_queryset(self):
        return Tag.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
