# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url
from django.shortcuts import get_object_or_404
from django.views.generic.base import TemplateView
from django.core.paginator import Paginator
from django.core.paginator import PageNotAnInteger
from django.core.paginator import EmptyPage
from products.models import Category, Product, ProjectCase


class ProductsByCategoryView(TemplateView):
    template_name = "prods.html"

    def get_context_data(self, **kwargs):
        category_id = int(kwargs["id"])
        category = get_object_or_404(Category, pk=category_id)
        context = super(ProductsByCategoryView, self).get_context_data(**kwargs)
        products = category.products.filter(review = 1)
        paginator = Paginator(products, 10)
        try:
            curr_page = self.request.GET.get("page", 1)
            products = paginator.page(curr_page)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)
        context["objects"] = products
        categories = Category.objects.all()
        context["categories"] = categories
        context["categoryKey"] = "Category"
        context["categoryName"] = "产品类型"
        return context

class ProductsView(TemplateView):
    template_name = "prods.html"

    def get_context_data(self, **kwargs):
        context = super(ProductsView, self).get_context_data(**kwargs)
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
        categories = Category.objects.all()
        context["categories"] = categories
        context["categoryKey"] = "Category"
        context["categoryName"] = "产品类型"
        return context

class ProductView(TemplateView):
    template_name = "prod.html"

    def get_context_data(self, **kwargs):
        product_id = int(kwargs["id"])
        context = super(ProductView, self).get_context_data(**kwargs)
        categories = Category.objects.all()
        context["categories"] = categories
        context["categoryKey"] = "Category"
        context["categoryName"] = "产品类型"
        context["object"] = get_object_or_404(Product, pk=product_id)
        return context


urlpatterns = [
    url(r"^category/(?P<id>\d+)/product/$", ProductsByCategoryView.as_view(), name="products_by_category_view"),
    url(r"^product/$", ProductsView.as_view(), name="products_view"),
    url(r"^product/(?P<id>\d+)$", ProductView.as_view(), name="product_view"),
]
