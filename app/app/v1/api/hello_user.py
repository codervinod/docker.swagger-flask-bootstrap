# -*- coding: utf-8 -*-
from flask import request, g

from . import Resource
from .. import schemas


class HelloUser(Resource):

    def get(self, user):

        return user, 200, None