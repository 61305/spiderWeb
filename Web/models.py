# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField('类名', max_length=30)
    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField('标题', max_length=70)
    body = models.TextField('正文')
    author = models.CharField('作者', max_length=50, null=True)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    abstract = models.CharField('摘要', max_length=54, blank=True, null=True,
                                help_text="可选，如若为空将摘取正文的前54个字符")
    category = models.ForeignKey('Category', verbose_name='分类',
                                 null=True,
                                 on_delete=models.SET_NULL)
    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-created_time']
