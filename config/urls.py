#!/usr/bin/env python
#coding:utf-8

import os
import sys

from handler import index,base

urls = [
	(r"/", index.MainHandler),
	(r"/register", index.RegisterHandler),
	(r"/login", index.LoginHandler),
	(r"/logout", index.LogoutHandler),

	#用于捕获未定义url
	(r".*", base.BaseHandler),
]
