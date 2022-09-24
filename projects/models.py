from django.db import models


class Project(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField()
    type = models.CharField(max_length=100, blank=False)

    class Meta:
        ordering = ['created']


class Issue(models.Model):
    created_time = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField()
    tag = models.CharField(max_length=100, blank=False)
    priority = models.CharField(max_length=100, blank=False)
    status = models.CharField(max_length=100, blank=False)

    class Meta:
        ordering = ['created_time']


class Comment(models.Model):
    created_time = models.DateTimeField(auto_now_add=True)
    description = models.TextField()

    class Meta:
        ordering = ['created_time']


class Contributors(models.Model):
    PERMISSIONS_CHOICES = (
        ('a', 'a'),
        ('b', 'b'),
        ('c', 'c'),
    )

    created_time = models.DateTimeField(auto_now_add=True)
    permission = models.CharField(choices=PERMISSIONS_CHOICES, default='friendly', max_length=100)
    role = models.CharField(max_length=50, blank=False)

    class Meta:
        ordering = ['created_time']
