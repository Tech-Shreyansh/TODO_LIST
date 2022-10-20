# Generated by Django 4.1.2 on 2022-10-20 19:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("notes", "0002_trial_class_trial_age_trial_town_trial_user_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="trial",
            name="user",
        ),
        migrations.RemoveField(
            model_name="trial_skill",
            name="user",
        ),
        migrations.AddField(
            model_name="trial_class",
            name="user",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]