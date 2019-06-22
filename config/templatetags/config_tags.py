#-*- coding:utf-8 -*-
from __future__ import unicode_literals

from pyquery import PyQuery
from django.template import Library, loader
from config.models import Config, Contact, About, FriendLink, CONTACT_CATEGORIES

register = Library()

UNKNOWN = "UNKNOWN"

@register.simple_tag
def config(key):
    if key:
        try:
            cfg = Config.objects.get(key = key)
            return cfg.value or UNKNOWN
        except Config.DoesNotExist:
            pass
    return UNKNOWN


@register.simple_tag
def about(key):
    if key:
        try:
            abt = About.objects.get(category = key)
            ctnt = abt.content or UNKNOWN
            if ctnt != UNKNOWN:
                ctnt = PyQuery(ctnt).text()
            return ctnt
        except About.DoesNotExist:
            pass
    return UNKNOWN


@register.simple_tag
def contact(key):
    if key:
        try:
            ctct = Contact.objects.get(category = key)
            return ctct.value or UNKNOWN
        except Contact.DoesNotExist:
            pass
    return UNKNOWN


@register.simple_tag
def contact_html():
    ctcts = Contact.objects.all()
    res = dict([(i.category, i.value) for i in ctcts])
    tpl = loader.get_template("tpl/contact.html")
    return tpl.render({"contact": res})


@register.simple_tag
def friends(size):
    sz = size or 3
    fdls = FriendLink.objects.all()[:sz]
    tpl = loader.get_template("tpl/friends.html")
    return tpl.render({"friends": fdls})


