# Generated by Django 4.0.3 on 2022-10-31 19:25

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0006_alter_article_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
