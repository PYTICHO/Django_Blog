from django.contrib import admin

from .models import *

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'is_published')
    list_display_links = ('title', 'id')
    list_editable = ('is_published',)


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)

