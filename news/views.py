# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.conf.urls import url
from django.views.generic.base import TemplateView
from django.core.paginator import Paginator
from django.core.paginator import PageNotAnInteger
from django.core.paginator import EmptyPage
from news.models import News

class NewListView(TemplateView):
    template_name = "list.html"

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

urlpatterns = [
    url(r"^news$", NewListView.as_view(), name="new_list_view")
]
