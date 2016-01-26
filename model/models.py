#!/usr/bin/env python
#coding:utf-8
import sys
sys.path.append("..")

from datetime import datetime
from peewee import *
from config.settings import settings

db = MySQLDatabase(
		host = settings['mysql_options']['hostaddress'],
		database = settings['mysql_options']['database'],
		user = settings['mysql_options']['user'],
		passwd = settings['mysql_options']['password'],
		charset = 'utf8'
		)


class BaseModel(Model):
	class Meta:
		database = db 

class Article(BaseModel):
	title = CharField(max_length=100)
	author = CharField(max_length=50)
	description = CharField(max_length=50)
	content = TextField()
	dateline = DateTimeField(default=datetime.now())


if __name__ == '__main__':
	#创建表
	Article.create_table()

