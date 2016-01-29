#!/usr/bin/env python
#coding:utf-8

import tornado.web
import pymongo
import json
import logging
from base import BaseHandler

class LoginHandler(BaseHandler):
	def get(self):
		logging.info("login html")
		self.render("login.html")

	def post(self):
		"""handle the login request 
		"""
		username = self.get_argument('username')
		passwd = self.get_argument('passwd')

		db = self.application.myMongodb
		user = db.users.find_one({'name':username, 'passwd':passwd})
		if user is not None:
			del user['_id']
			context = {'status':'success'}
			#存储进session
			self.session['username'] = user['name']
			self.session.save()

			self.write(json.dumps(context))
		else:
			context = {'status':'error'}
			self.write(json.dumps(context))

class RegisterHandler(tornado.web.RequestHandler):
	def get(self):
		self.render("register.html")

	def post(self):
		"""handle the register request
		"""
		name = self.get_argument('name')
		sex = self.get_argument('sex')
		age = self.get_argument('age')
		tel = self.get_argument('tel')
		passwd = self.get_argument('passwd')

		db = self.application.myMongodb
		context = {'name':name, 'sex':sex, 'age':age, 'tel':tel, 'passwd':passwd}
		db.users.insert(context)
		self.write('注册成功')

class LogoutHandler(BaseHandler):
	def get(self):
		self.session['username'] = None
		self.session.save()
		self.redirect('/')


