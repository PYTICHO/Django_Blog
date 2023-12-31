# Generated by Django 4.0.3 on 2022-10-07 20:40

from django.db import migrations, models
import home.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=135, verbose_name='Название статьи')),
                ('text', models.TextField(validators=[home.models.validate_text], verbose_name='Текст статьи')),
                ('is_published', models.BooleanField(default=True)),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
            ],
            options={
                'verbose_name': 'Статьи',
                'verbose_name_plural': 'Статьи',
            },
        ),
    ]
