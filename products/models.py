# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.conf import settings
from ckeditor.fields import RichTextField

review_status = (
    (0, "待发布"),
    (1, "已发布"),
)

class Category(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID")
    create_dt = models.DateTimeField(default=timezone.now, verbose_name="创建时间")
    name = models.CharField(max_length=127, unique=True, verbose_name="名称")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "tb_category"
        verbose_name = "产品类型"
        verbose_name_plural = "产品类型"
        ordering = ["-id"]

class Product(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID")
    create_dt = models.DateTimeField(default=timezone.now, verbose_name="创建时间")
    review = models.IntegerField(choices=review_status, verbose_name="状态", default=0)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="作者", related_name="products", on_delete=models.DO_NOTHING)
    category = models.ForeignKey(Category, verbose_name="类型", related_name="products", on_delete=models.DO_NOTHING)
    view_count = models.IntegerField(verbose_name="浏览数", default=0)
    title = models.CharField(max_length=127, verbose_name="标题")
    image = models.ImageField(upload_to="images/product/%Y/%m", null=True, blank=True, verbose_name="产品图")
    content = RichTextField(verbose_name="内容")

    def img_url(self):
        return "<image src=\"%s\" width='200px' height='100px'/>" % (self.image.url if self.image else "")
    img_url.short_description = "产品图"
    img_url.allow_tags = True

    def __str__(self):
        return self.title

    class Meta:
        db_table = "tb_product"
        verbose_name = "产品介绍"
        verbose_name_plural = "产品介绍" 
        ordering = ["-id"]

class ProjectCase(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID")
    create_dt = models.DateTimeField(default=timezone.now, verbose_name="创建时间")
    review = models.IntegerField(choices=review_status, verbose_name="状态", default=0)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="作者", related_name="project_cases", on_delete=models.DO_NOTHING)
    category = models.ForeignKey(Category, verbose_name="类型", related_name="project_cases", on_delete=models.DO_NOTHING)
    view_count = models.IntegerField(verbose_name="浏览数", default=0)
    title = models.CharField(max_length=127, verbose_name="标题")
    image = models.ImageField(upload_to="images/project_case/%Y/%m", null=True, blank=True, verbose_name="产品图")
    content = RichTextField(verbose_name="内容")

    def img_url(self):
        return "<image src=\"%s\" width='200px' height='100px'/>" % (self.image.url if self.image else "")
    img_url.short_description = "产品图"
    img_url.allow_tags = True

    def __str__(self):
        return self.title

    class Meta:
        db_table = "tb_project_case"
        verbose_name = "工程案例"
        verbose_name_plural = "工程案例" 
        ordering = ["-id"]


