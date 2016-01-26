#!/usr/bin/env python
#coding:utf-8

import tornado.web
import pymongo
from base import BaseHandler

class MainHandler(BaseHandler):
	@tornado.web.authenticated
	def get(self):
		self.render("index.html")


class LoginHandler(BaseHandler):
	def get(self):
		self.render("login.html")

	def post(self):
		"""handle the login request 
		"""
		pass

class RegisterHandler(BaseHandler):
	def get(self):
		self.render("register.html")

	def post(self):
		"""handle the register request
		"""
		pass

class LogoutHandler(BaseHandler):
	def get(self):
		self.session['username'] = None
		self.save()


