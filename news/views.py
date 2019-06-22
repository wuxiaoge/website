# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.conf.urls import url
from django.shortcuts import get_object_or_404
from django.views.generic.base import TemplateView
from django.core.paginator import Paginator
from django.core.paginator import PageNotAnInteger
from django.core.paginator import EmptyPage
from news.models import News

class NewListView(TemplateView):
    template_name = "news.html"

    def get_context_data(self, **kwargs):
        context = super(NewListView, self).get_context_data(**kwargs)
        news = News.objects.filter(review = 1)
        paginator = Paginator(news, 10)
        try:
            curr_page = self.request.GET.get("page", 1)
            news = paginator.page(curr_page)
        except PageNotAnInteger:
            news = paginator.page(1)
        except EmptyPage:
            news = paginator.page(paginator.num_pages)
        context["objects"] = news
        context["categories"] = []
        context["categoryKey"] = "News"
        context["categoryName"] = "企业新闻"
        return context

class NewsView(TemplateView):
    template_name = "new.html"

    def get_context_data(self, **kwargs):
        try:
            new_id = int(self.request.GET.get("new_id"))
        except Exception:
            new_id = 0
        context = super(NewsView, self).get_context_data(**kwargs)
        context["object"] = get_object_or_404(News, pk=new_id)
        context["categories"] = []
        context["categoryKey"] = "News"
        context["categoryName"] = "企业新闻"
        return context


urlpatterns = [
    url(r"^news$", NewListView.as_view(), name="new_list_view"),
    url(r"^new$", NewsView.as_view(), name="news_view"),
]
