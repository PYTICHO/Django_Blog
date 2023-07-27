from email.policy import default
from tabnanny import verbose
from django.urls import reverse
from django.db import models
from django.core.exceptions import ValidationError
from django.shortcuts import render
from django.contrib.auth.models import User



# Пользовательская проверка 
def validate_text(value: str) -> str:
    text_length = len(value)
    if text_length < 5:
        raise ValidationError(f"Символов:  {text_length} *  Текст статьи не может быть менее 5 символов!")
    
    return value


def validate_image(image):
    return image



# Create your models here.



# Модель Статьи
class Article(models.Model):
    author = models.ForeignKey(User, verbose_name='Автор' , on_delete=models.CASCADE, default=None, null=False, blank=False)
    title = models.CharField(max_length = 135, verbose_name = 'Название статьи')
    text = models.TextField(verbose_name = 'Текст статьи', validators=[validate_text])
    image = models.ImageField(verbose_name = 'Картинка', upload_to = 'images/%Y/%m/%d', null=True, blank=True, validators=[validate_image])
    is_published = models.BooleanField(default=True)
    time_create = models.DateTimeField(verbose_name='Дата публикации', auto_now_add=True)

    


    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'article_pk': self.pk})


    class Meta:
        verbose_name = 'Статьи'
        verbose_name_plural = 'Статьи'
        ordering = ('-time_create',)





# Модель комментария к статье
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete = models.CASCADE, verbose_name='Статья', null = False, blank=False, related_name='comment_article')
    time_create = models.DateTimeField(verbose_name='Дата комментария', auto_now=True)
    text = models.TextField(verbose_name = 'Текст комментария')
    status = models.BooleanField(default=True, verbose_name='Видимость статьи')
    comment_author = models.ForeignKey(User, on_delete=models.PROTECT, null=False, blank=False, default= None)
    
    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ('-time_create',)

    def __str__(self):
        return f"Комментарий к {self.article.pk} статье "