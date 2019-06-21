# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from news.models import News

class NewsAdmin(admin.ModelAdmin):
    list_filter = ("review",)
    search_fields = ("title",)
    list_display = ("title", "create_dt", "review")
    list_editable = ("review",)
    fieldsets = (
        (None, {
            "fields": ("title", "content", "review"),
        }),
    )
    actions = None

    def save_model(self, request, obj, form, change):
        if not change:
            obj.user = request.user
        obj.save()


admin.site.register(News, NewsAdmin)
