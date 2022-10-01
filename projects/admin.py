from django.contrib import admin

from projects.models import Project, Issue, Comment, Contributor, Tag

admin.site.register(Project)
admin.site.register(Tag)
admin.site.register(Issue)
admin.site.register(Comment)
admin.site.register(Contributor)
