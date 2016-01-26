#!/usr/bin/env python
#coding:utf-8

import os
import sys

import tornado.ioloop
import tornado.options
import tornado.httpserver

#multi process
import tornado.netutil
import tornado.process
import pymongo

from tornado.options import define, options
from config import urls
from config import settings
from util import session

import torndb

define("port", default=8888, help="run on the given port", type=int)


class Application(tornado.web.Application):
	def __init__(self):
		handlers = urls.urls
		setting = settings.settings
		#connect mongo
		client = pymongo.MongoClient(setting['mongo_options']['hostaddress'])
		self.myMongodb = client[setting['mongo_options']['collection']]

		#connect mysql
		db = torndb.Connection(
			setting['mysql_options']['hostaddress'],
			setting['mysql_options']['database'],
			setting['mysql_options']['user'],
			setting['mysql_options']['password']
				)

		tornado.web.Application.__init__(self, handlers, **setting)
		self.session_manager = session.SessionManager(
				setting['session_secret'],	
				setting['store_options'],
				setting['session_timeout']
				)


#server start
def main():
	tornado.options.parse_command_line()
	#multi process
	sockets = tornado.netutil.bind_sockets(options.port)
	tornado.process.fork_processes(4)

	http_server = tornado.httpserver.HTTPServer(Application())
	http_server.add_sockets(sockets)
	print 'Development server is running at http://127.0.0.1:%s/' % options.port
	tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
	main()

