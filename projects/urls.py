from django.urls import path, include
from rest_framework.routers import DefaultRouter

from projects import views

router = DefaultRouter()
router.register(r'projects', views.ProjectViewSet, basename="project")
router.register(r'tags', views.ProjectViewSet, basename="tag")

urlpatterns = [
    path('', include((router.urls, 'projects'))),
]
