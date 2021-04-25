# Generated by Django 3.2 on 2021-04-24 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_lab_board_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lab_board_model',
            name='number_path',
            field=models.CharField(choices=[('', ''), ('1', '1 cvtyf'), ('2', '2'), ('3', '3'), ('4', '4')], max_length=1, verbose_name='Номер партии'),
        ),
        migrations.AlterField(
            model_name='lab_board_model',
            name='number_shift',
            field=models.CharField(choices=[('', ''), ('1', '1 cvtyf'), ('2', '2'), ('3', '3'), ('4', '4')], max_length=1, verbose_name='Смена (производства)№'),
        ),
        migrations.AlterField(
            model_name='lab_board_model',
            name='value2',
            field=models.CharField(max_length=4, null=True, verbose_name='Длина, мм'),
        ),
    ]
