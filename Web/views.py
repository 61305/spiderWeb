# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from . import models

# Create your views here.

def index(request):
    articles = models.Article.objects.all()
    return render(request, 'Web/index.html', {'articles': articles})


def page(request, art_id):
    article = models.Article.objects.get(pk=art_id)
    return render(request, 'Web/page.html', {'article': article})

def archives(request, year, month):
    post_list = models.Article.objects.filter(created_time__year=year,
                                              created_time__month=month).order_by('-created_time')
    return render(request, 'Web/index.html', context={'post_list': post_list})

