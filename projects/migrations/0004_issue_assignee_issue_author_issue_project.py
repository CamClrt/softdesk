# Generated by Django 4.1.1 on 2022-10-01 06:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0003_contributor_project_contributor_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='assignee',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='assignee_issues', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='issue',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='author_issues', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='issue',
            name='project',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='project_issues', to='projects.project'),
            preserve_default=False,
        ),
    ]