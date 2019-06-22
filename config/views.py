# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.conf.urls import url
from django.views.generic.base import TemplateView
from news.models import News
from products.models import Category


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        news = News.objects.filter(review = 1)[:5]
        context["news"] = news
        categories = Category.objects.all()[:8]
        context["categories"] = [(c.name, c.products.all()[:6]) for c in categories]
        return context


urlpatterns = [
    url(r"^$", IndexView.as_view(), name="index_view"),
]
