# -*- coding: utf-8 -*-

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###

from .api.hello_user import HelloUser


routes = [
    dict(resource=HelloUser, urls=['/hello/<user>'], endpoint='hello_user'),
]