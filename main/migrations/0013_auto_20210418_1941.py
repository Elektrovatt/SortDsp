# Generated by Django 3.2 on 2021-04-18 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20210418_1937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='number_tapes_model',
            name='liner_2_1_choices',
            field=models.CharField(choices=[('', ''), ('Foam', 'Foam'), ('Pes', 'Pes')], max_length=20),
        ),
        migrations.AlterField(
            model_name='number_tapes_model',
            name='liner_2_2_choices',
            field=models.CharField(choices=[('', ''), ('Foam', 'Foam'), ('Pes', 'Pes')], max_length=20),
        ),
        migrations.AlterField(
            model_name='number_tapes_model',
            name='liner_2_3_choices',
            field=models.CharField(choices=[('', ''), ('Foam', 'Foam'), ('Pes', 'Pes')], max_length=20),
        ),
        migrations.AlterField(
            model_name='number_tapes_model',
            name='liner_2_4_choices',
            field=models.CharField(choices=[('', ''), ('Foam', 'Foam'), ('Pes', 'Pes')], max_length=20),
        ),
        migrations.AlterField(
            model_name='number_tapes_model',
            name='number_1_1_choices',
            field=models.CharField(choices=[('', ''), ('P 50', 'P 50'), ('P 80', 'P 80'), ('P 120', 'P 120')], max_length=20),
        ),
        migrations.AlterField(
            model_name='number_tapes_model',
            name='number_1_2_choices',
            field=models.CharField(choices=[('', ''), ('P 50', 'P 50'), ('P 80', 'P 80'), ('P 120', 'P 120')], max_length=20),
        ),
        migrations.AlterField(
            model_name='number_tapes_model',
            name='number_2_1_choices',
            field=models.CharField(choices=[('', ''), ('P 50', 'P 50'), ('P 80', 'P 80'), ('P 120', 'P 120')], max_length=20),
        ),
        migrations.AlterField(
            model_name='number_tapes_model',
            name='number_2_2_choices',
            field=models.CharField(choices=[('', ''), ('P 50', 'P 50'), ('P 80', 'P 80'), ('P 120', 'P 120')], max_length=20),
        ),
        migrations.AlterField(
            model_name='number_tapes_model',
            name='number_2_3_choices',
            field=models.CharField(choices=[('', ''), ('P 50', 'P 50'), ('P 80', 'P 80'), ('P 120', 'P 120')], max_length=20),
        ),
        migrations.AlterField(
            model_name='number_tapes_model',
            name='number_2_4_choices',
            field=models.CharField(choices=[('', ''), ('P 50', 'P 50'), ('P 80', 'P 80'), ('P 120', 'P 120')], max_length=20),
        ),
        migrations.AlterField(
            model_name='number_tapes_model',
            name='value0',
            field=models.CharField(max_length=20, verbose_name='Пробег ленты Agg 1.1'),
        ),
        migrations.AlterField(
            model_name='number_tapes_model',
            name='value1',
            field=models.CharField(max_length=20, verbose_name='Пробег ленты Agg 1.2'),
        ),
        migrations.AlterField(
            model_name='number_tapes_model',
            name='value2',
            field=models.CharField(max_length=20, verbose_name='Пробег ленты Agg 2.1'),
        ),
        migrations.AlterField(
            model_name='number_tapes_model',
            name='value3',
            field=models.CharField(max_length=20, verbose_name='Пробег ленты Agg 2.2'),
        ),
        migrations.AlterField(
            model_name='number_tapes_model',
            name='value4',
            field=models.CharField(max_length=20, verbose_name='Пробег ленты Agg 2.3'),
        ),
        migrations.AlterField(
            model_name='number_tapes_model',
            name='value5',
            field=models.CharField(max_length=20, verbose_name='Пробег ленты Agg 2.4'),
        ),
    ]