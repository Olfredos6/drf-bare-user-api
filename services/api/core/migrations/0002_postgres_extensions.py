# Generated by Django 4.0 on 2022-02-01 06:22

from django.contrib.postgres.operations import CITextExtension
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        CITextExtension()
    ]
