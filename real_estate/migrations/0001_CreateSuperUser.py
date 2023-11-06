# Generated by Django 4.2.7 on 2023-11-06 06:15

from django.db import migrations
from django.contrib.auth.hashers import make_password


def create_super_user(apps, schema_editor):
    User = apps.get_model("auth", "User")

    User.objects.create(
        username="admin",
        password=make_password("qwerty123"),
        is_superuser=True,
        is_staff=True,
    )


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.RunPython(create_super_user, migrations.RunPython.noop),
    ]
