# 使得django在启动的时候会加载celery的app
from binblog.celery import app as celery_app
import pymysql

__all__ = ('celery_app',)

pymysql.install_as_MySQLdb()