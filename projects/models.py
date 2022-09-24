from django.db import models
from django.utils.translation import gettext_lazy as _


class GenericCustomModel(models.Model):
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_time']
        abstract = True


class Project(GenericCustomModel):
    TYPE_CHOICES = [
        ('back', 'back-end'),
        ('front', 'front-end'),
        ('iOS', 'iOS'),
        ('Androïd', 'Androïd')
    ]

    title = models.CharField(max_length=100, blank=False)
    description = models.TextField()
    type = models.CharField(choices=TYPE_CHOICES, default='back', max_length=10)


class Issue(GenericCustomModel):
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField()

    TAG_CHOICES = [
        ('BU', _('Bug')),
        ('AM', _('Improvement')),
        ('TA', _('Task'))
    ]

    tag = models.CharField(choices=TAG_CHOICES, default='BU', max_length=3)

    PRIORITY_CHOICES = [
        ('0', _('Low')),
        ('1', _('Medium')),
        ('2', _('High')),
    ]

    priority = models.CharField(choices=PRIORITY_CHOICES, default='1', max_length=2)

    STATUS_CHOICES = [
        ('todo', _('To do')),
        ('wip', _('In progress')),
        ('done', _('Completed')),
    ]

    status = models.CharField(choices=STATUS_CHOICES, default='todo', max_length=25)


class Comment(GenericCustomModel):
    description = models.TextField()


class Contributor(GenericCustomModel):
    PERMISSION_CHOICES = [
        ('0', 'no'),
        ('1', 'yes'),
        ('2', 'maybe'),
    ]

    permission = models.CharField(choices=PERMISSION_CHOICES, default='0', max_length=1)
    role = models.CharField(max_length=50, blank=False)
