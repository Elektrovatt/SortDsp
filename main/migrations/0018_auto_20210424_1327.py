# Generated by Django 3.2 on 2021-04-24 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_auto_20210424_1322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lab_board_model',
            name='date_cr',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='Дата создания записи'),
        ),
        migrations.AlterField(
            model_name='lab_board_model',
            name='date_created',
            field=models.DateField(verbose_name='Дата производства'),
        ),
    ]
