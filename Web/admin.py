# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Article, Category

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'author']

admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)