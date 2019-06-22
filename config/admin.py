# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from config.models import Config, About, Contact, FriendLink

class ConfigAdmin(admin.ModelAdmin):
    readonly_fields = ("id",)
    list_display = ("id", "value")
    fieldsets = (
        (None, {
            "fields": ("id", "value"),
        }),
    )
    actions = None
    save_as = False
    save_as_continue = False

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

class AboutAdmin(admin.ModelAdmin):
    readonly_fields = ("id",)
    list_display = ("id",)
    fieldsets = (
        (None, {
            "fields": ("id", "content"),
        }),
    )
    actions = None
    save_as = False
    save_as_continue = False

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

class ContactAdmin(admin.ModelAdmin):
    list_display = ("id", "value")
    fieldsets = (
        (None, {
            "fields": ("id", "value"),
        }),
    )
    actions = None


class FriendLinkAdmin(admin.ModelAdmin):
    list_display = ("name", "link")
    fieldsets = (
        (None, {
            "fields": ("name", "link"),
        }),
    )
    actions = None


admin.site.register(Config, ConfigAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(FriendLink, FriendLinkAdmin)

