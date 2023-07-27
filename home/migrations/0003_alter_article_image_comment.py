# Generated by Django 4.0.3 on 2022-10-14 16:28

from django.db import migrations, models
import django.db.models.deletion
import home.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_article_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(null=True, upload_to='images/%Y/%m/%d', validators=[home.models.validate_image], verbose_name='Картинка'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_create', models.DateTimeField(auto_now=True, verbose_name='Дата комментария')),
                ('text', models.TextField(verbose_name='Текст комментария')),
                ('status', models.BooleanField(default=True, verbose_name='Видимость статьи')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_article', to='home.article', verbose_name='Статья')),
            ],
        ),
    ]