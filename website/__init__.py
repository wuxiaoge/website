# -*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import pymysql
pymysql.install_as_MySQLdb()

from django.contrib import admin
admin.site.site_header = 'website 项目管理系统'
admin.site.site_title = '系统后台'
admin.site.index_title = '后台管理'

import mimetypes
mimetypes.add_type("image/svg+xml", ".svg", True)
mimetypes.add_type("image/svg+xml", ".svgz", True)
