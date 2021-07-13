# Generated by Django 3.2 on 2021-07-13 09:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0031_auto_20210713_0826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sizes_unpolished_board_model',
            name='value1',
            field=models.CharField(max_length=4, null=True, verbose_name='Ширина 2070(+/- 5), мм'),
        ),
        migrations.AlterField(
            model_name='sizes_unpolished_board_model',
            name='value2',
            field=models.CharField(max_length=4, null=True, verbose_name='Длинна правая сторона в мм'),
        ),
        migrations.AlterField(
            model_name='sizes_unpolished_board_model',
            name='value3',
            field=models.CharField(max_length=4, null=True, verbose_name='Длинна левая сторона в мм '),
        ),
        migrations.AlterField(
            model_name='sizes_unpolished_board_model',
            name='value4',
            field=models.CharField(max_length=1, null=True, verbose_name='Разница диагоналей в мм'),
        ),
        migrations.CreateModel(
            name='Cleaning_press_tape_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Дата')),
                ('value0', models.CharField(choices=[('', ''), ('Грязная', 'Грязная'), ('Чистая', 'Чистая'), ('Очистка', 'Очистка')], max_length=20, verbose_name='Левая сторона ленты')),
                ('value1', models.CharField(choices=[('', ''), ('Грязная', 'Грязная'), ('Чистая', 'Чистая'), ('Очистка', 'Очистка')], max_length=20, verbose_name='Центр ленты')),
                ('value2', models.CharField(choices=[('', ''), ('Грязная', 'Грязная'), ('Чистая', 'Чистая'), ('Очистка', 'Очистка')], max_length=20, verbose_name='Правая сторона ленты')),
                ('value3', models.CharField(choices=[('', ''), ('Грязная', 'Грязная'), ('Чистая', 'Чистая'), ('Очистка', 'Очистка')], max_length=20, verbose_name='Левая сторона ленты')),
                ('value4', models.CharField(choices=[('', ''), ('Грязная', 'Грязная'), ('Чистая', 'Чистая'), ('Очистка', 'Очистка')], max_length=20, verbose_name='Центр ленты')),
                ('value5', models.CharField(choices=[('', ''), ('Грязная', 'Грязная'), ('Чистая', 'Чистая'), ('Очистка', 'Очистка')], max_length=20, verbose_name='Правая сторона ленты')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Владелец записи')),
            ],
            options={
                'verbose_name': 'поля',
                'verbose_name_plural': 'Пресс - Очистка ленты пресса',
                'ordering': ('-date_created',),
            },
        ),
    ]
