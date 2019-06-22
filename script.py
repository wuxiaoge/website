# -*- coding:utf-8 -*-
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "website.settings")
import django
django.setup()

from config.models import Config, About, Contact, CONFIG_KEYS, ABOUT_CATEGORIES, CONTACT_CATEGORIES

map(lambda x:Config(id=x[0], value=x[1]).save(), CONFIG_KEYS)
map(lambda x:About(id=x[0], content=x[1]).save(), ABOUT_CATEGORIES)
map(lambda x:Contact(id=x[0], value=x[1]).save(), CONTACT_CATEGORIES)
