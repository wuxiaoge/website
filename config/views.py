# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.conf.urls import url
from django.views.generic.base import TemplateView
from news.models import News
from products.models import Category
from config.models import About, ABOUT_CATEGORIES


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        news = News.objects.filter(review = 1)[:5]
        context["news"] = news
        categories = Category.objects.all()[:8]
        context["categories"] = [(c.name, c.products.all()[:6]) for c in categories]
        return context


class AboutView(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        about_id = int(kwargs["id"])
        context = super(AboutView, self).get_context_data(**kwargs)
        about = get_object_or_404(About, pk=about_id)
        context["object"] = {"title": dict(ABOUT_CATEGORIES)[about.id], "content":about.content}
        context["categories"] = [{"name":v, "url":"/about/%d" % k} for k, v in ABOUT_CATEGORIES]
        context["categoryKey"] = "About"
        context["categoryName"] = "关于我们"
        return context


urlpatterns = [
    url(r"^$", IndexView.as_view(), name="index_view"),
    url(r"^about/(?P<id>\d+)$", AboutView.as_view(), name="about_view"),
]
