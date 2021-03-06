# Generated by Django 4.0.4 on 2022-04-21 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='filemodel',
            options={'ordering': ['-time_update', '-time_create'], 'verbose_name': 'Файл', 'verbose_name_plural': 'Файлы'},
        ),
        migrations.AlterField(
            model_name='filemodel',
            name='file',
            field=models.FileField(upload_to='files', verbose_name='Путь к файлу'),
        ),
        migrations.AlterField(
            model_name='filemodel',
            name='sender',
            field=models.CharField(default='user', max_length=50, verbose_name='Отправитель'),
        ),
        migrations.AlterField(
            model_name='filemodel',
            name='time_create',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Время создания'),
        ),
        migrations.AlterField(
            model_name='filemodel',
            name='time_update',
            field=models.DateTimeField(auto_now=True, verbose_name='Время изменения'),
        ),
        migrations.AlterField(
            model_name='filemodel',
            name='title',
            field=models.CharField(default='', max_length=50, verbose_name='Заголовок'),
        ),
    ]
