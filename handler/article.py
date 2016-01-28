#!/usr/bin/env python
#coding:utf-8

import tornado.web
import pymongo
import json
from tornado import gen
from base import BaseHandler
from model.models import Article
from peewee import DatabaseError, DoesNotExist

class MainHandler(BaseHandler):
	@tornado.web.authenticated
	def get(self):
		articles = Article.select()
		self.render("article/index.html", articles=articles)


class AddHandler(BaseHandler):
	@tornado.web.authenticated
	def get(self):
		self.render("article/add.html")

	def post(self):
		title = self.get_argument('title')
		author = self.get_argument('author')
		description = self.get_argument('description')
		content = self.get_argument('content')

		article = Article.create(title=title, author=author, description=description, content=content)
		article.save()
		self.redirect('/manage')

class ManageHandler(BaseHandler):
	@tornado.web.authenticated
	def get(self):
		articles = Article.select().order_by(Article.id.desc())
		self.render("article/manage.html", articles=articles)


class DeleteHandler(BaseHandler):
	@tornado.web.authenticated
	def get(self):
		id = self.get_argument('id')
		article = Article.get(Article.id == id)
		article.delete_instance()

		self.redirect('/manage')


class ModifyHandler(BaseHandler):
	@tornado.web.authenticated
	def get(self):
		id = self.get_argument('id')
		article = Article.get(Article.id == id)

		self.render("article/modify.html", article=article)

	def post(self):
		id = self.get_argument('id')

		title = self.get_argument('title')
		author = self.get_argument('author')
		description = self.get_argument('description')
		content = self.get_argument('content')

		article = Article.get(Article.id == id)
		article.title = title
		article.author = author
		article.description = description
		article.content = content
		article.save()
		
		self.redirect('/manage')
		
class SearchHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
		key = self.get_argument('key')

		articles = Article.select().where(Article.title.contains(key))
		self.render("article/index.html", articles=articles)
	

class ShowHandler(BaseHandler):
    @tornado.web.authenticated
#   @gen.coroutine
    def get(self):
        id = self.get_argument('id')
        article = Article.get(Article.id == id)
        self.render("article/show.html", article=article)

