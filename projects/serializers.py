from rest_framework import serializers

from projects.models import Project, Issue, Comment, Contributor, Tag


class TagSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Tag
        fields = ['id', 'created_time', 'title', 'author']


class ProjectSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Project
        fields = ['id', 'created_time', 'title', 'description', 'type', 'author']


class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = ['id', 'created_time', 'title', 'description', 'tag', 'priority', 'status']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'created_time', 'description']


class ContributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributor
        fields = ['id', 'created_time', 'permission', 'role']
