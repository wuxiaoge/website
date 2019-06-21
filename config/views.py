# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.conf.urls import url
from django.views.generic.base import TemplateView


class IndexView(TemplateView):
	template_name = "index.html"

	def get_context_data(self, **kwargs):
		return super(IndexView, self).get_context_data(**kwargs)


urlpatterns = [
	url(r"^$", IndexView.as_view(), name="index_view"),
]