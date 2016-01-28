#!/usr/bin/env python
#coding:utf-8

import os
import sys

from handler import index,base,article

urls = [
	(r"/", article.MainHandler),
	(r"/register", index.RegisterHandler),
	(r"/login", index.LoginHandler),
	(r"/logout", index.LogoutHandler),

	#article
	(r"/add", article.AddHandler),
	(r"/manage", article.ManageHandler),
	(r"/del", article.DeleteHandler),
	(r"/modify", article.ModifyHandler),
	(r"/show", article.ShowHandler),
	(r"/search", article.SearchHandler),

	#用于捕获未定义url
	(r".*", base.BaseHandler),
]
