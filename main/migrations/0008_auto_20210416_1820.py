# Generated by Django 3.1.4 on 2021-04-16 18:20

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0007_auto_20210416_1707'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='table_thickness_ground_plate_model',
            new_name='Table_thickness_plate_model',
        ),
    ]