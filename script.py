# -*- coding:utf-8 -*-
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "website.settings")
import django
django.setup()

from config.models import Config, About

cfg_names = [
    (1, "网站标题"),
    (2, "网站关键字"),
    (3, "网站描述"),
]

for key, value in cfg_names:
    cfg = Config(key = key, value = value)
    cfg.save()

about_names = [
    (1, "企业历史"),
    (2, "企业文化"),
    (3, "企业荣誉"),
]

for key, value in about_names:
    abt = About(category = key, content = value)
    abt.save()

