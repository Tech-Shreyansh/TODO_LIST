# Generated by Django 4.1.2 on 2022-10-21 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("note", "0003_alter_description_description"),
    ]

    operations = [
        migrations.AddField(
            model_name="description",
            name="bookmark",
            field=models.CharField(max_length=2, null=True),
        ),
    ]