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

class News(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID")
    create_dt = models.DateTimeField(default=timezone.now, verbose_name="创建时间")
    review = models.IntegerField(choices=review_status, verbose_name="状态", default=0)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="作者", related_name="news", on_delete=models.DO_NOTHING)
    view_count = models.IntegerField(verbose_name="浏览数", default=0)
    title = models.CharField(max_length=127, verbose_name="标题")
    content = RichTextField(verbose_name="内容")

    def __str__(self):
        return self.title

    class Meta:
        db_table = "tb_news"
        verbose_name = "企业新闻"
        verbose_name_plural = "企业新闻" 
        ordering = ["-id"]


