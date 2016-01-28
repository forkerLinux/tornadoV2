#!/usr/bin/env python
#coding:utf-8
"""数据库以及一些常用配置
"""

settings = {
        #"secure cookies":True,
        #用于 secure_cookie
        "cookie_secret":"y6KHYgM1SbCtH8axxEgt1omSARJwmkaMoBlezBg0EEE=",

        #session_secret 用于session
        "session_secret":"6Mv2JMqLQVC/WO6x0pStUKXy6deVg0ULvOSVQzp1A88=",
        "template_path": "templates", 
        "static_path": "static",
        "login_url":"/login",
        "xsrf_cookies":True,
        #redis设置
        "store_options":{
            'redis_host':'localhost',           
            'redis_port':6379,
            'redis_pass':'',
        },

		#mongodb设置
		"mongo_options":{
			'hostaddress':'localhost',
			'collection':'demo',
		},

		#mysql设置
		"mysql_options":{
			'hostaddress':'localhost',
			'database':'demo',
			'user':'root',
			'password':'123456',
		},

        #session生存周期 seconds
        "session_timeout":30*60,
        "debug":True
       }


