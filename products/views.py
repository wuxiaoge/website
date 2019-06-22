# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url
from django.views.generic.base import TemplateView
from django.core.paginator import Paginator
from django.core.paginator import PageNotAnInteger
from django.core.paginator import EmptyPage
from products.models import Category, Product, ProjectCase


class ProductsView(TemplateView):
    template_name = "prods.html"

    def get_context_data(self, **kwargs):
        context = super(ProductsView, self).get_context_data(**kwargs)
        categories = Category.objects.all()
        context["categories"] = categories
        products = Product.objects.filter(review = 1)
        paginator = Paginator(products, 10)
        try:
            curr_page = self.request.GET.get("page", 1)
            products = paginator.page(curr_page)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)
        context["objects"] = products
        context["categoryKey"] = "Category"
        context["categoryName"] = "产品类型"
        return context

urlpatterns = [
    url(r"^products$", ProductsView.as_view(), name="products_view")
]
