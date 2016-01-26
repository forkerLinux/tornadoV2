#!/usr/bin/env python
#coding:utf-8

import tornado.web
from util import session

class BaseHandler(tornado.web.RequestHandler):
	def __init__(self, *argc, **kwarg):
		super(BaseHandler, self).__init__(*argc, **kwarg)
		#定义handler的session,每次访问都会初始化一个Session
		self.session = session.Session(self.application.session_manager, self)

	def get(self):
		"""捕获404
		"""
		self.send_error(404)

	def get_current_user(self):
		"""复写get_current_user方法，在使用登录装饰器的时候判断是否登录
		"""
		return self.session.get('username')

	def write_error(self, status_code, **kwargs):
		"""重写404错误页
		"""
		if status_code == 404:
			self.render("public/404.html")
		elif status_code == 500:
			self.render("public/500.html")
		else:
			self.write('error' + str(status_code))

