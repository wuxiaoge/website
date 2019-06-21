# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ckeditor.fields import RichTextField

class Config(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID")
    key = models.CharField(max_length=255, unique=True, verbose_name="名称")
    value = models.CharField(max_length=255, verbose_name="内容")

    def __str__(self):
        return self.key

    class Meta:
        db_table = "tb_config"
        verbose_name = "网站配置"
        verbose_name_plural = "网站配置"
        ordering = ["id"]


class About(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID")
    category = models.CharField(max_length=127, unique=True, verbose_name="类型")
    content = RichTextField(verbose_name="内容")

    def __str__(self):
        return dict(ABOUT_CATEGORIES).get(self.category, "UNKNOWN")

    class Meta:
        db_table = "tb_about"
        verbose_name = "关于我们"
        verbose_name_plural = "关于我们"
        ordering = ["id"]


class Contact(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID")
    category = models.CharField(max_length=127, unique=True, verbose_name="名称")
    value = models.CharField(max_length=255, verbose_name="内容")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "tb_contact"
        verbose_name = "联系我们"
        verbose_name_plural = "联系我们"
        ordering = ["id"]


class FriendLink(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID")
    name = models.CharField(max_length=127, unique=True, verbose_name="网站名称")
    link = models.URLField(max_length=254, verbose_name="网站地址")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "tb_friendlink"
        verbose_name = "友情链接"
        verbose_name_plural = "友情链接"
        ordering = ["-id"]


