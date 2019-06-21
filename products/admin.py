# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from products.models import Product, Category, ProjectCase

class ProductAdmin(admin.ModelAdmin):
    list_filter = ("review",)
    search_fields = ("title",)
    list_display = ("id", "title", "img_url", "category", "view_count", "review")
    list_editable = ("review",)
    fieldsets = (
        (None, {
            "fields": ("title", "image", "category", "content", "review"),
        }),
    )
    actions = None

    def save_model(self, request, obj, form, change):
        if not change:
            obj.user = request.user
        obj.save()


class CategoryAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_display = ("id", "name", "create_dt")
    fieldsets = (
        (None, {
            "fields": ("name",),
        }),
    )
    actions = None


class ProjectCaseAdmin(admin.ModelAdmin):
    list_filter = ("review",)
    search_fields = ("title",)
    list_display = ("id", "title", "img_url", "category", "view_count", "review")
    list_editable = ("review",)
    fieldsets = (
        (None, {
            "fields": ("title", "image", "category", "content", "review"),
        }),
    )
    actions = None

    def save_model(self, request, obj, form, change):
        if not change:
            obj.user = request.user
        obj.save()


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ProjectCase, ProjectCaseAdmin)
