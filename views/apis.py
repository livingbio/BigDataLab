#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2014 george 
#
# Distributed under terms of the MIT license.

import webapp2
from models import _GP_code, GenericPipeline
from mapreduce import base_handler

import re

class PipelineTrigger(webapp2.RequestHandler):
    def get(self, _id):
        assert _id

        p = GenericPipeline(id)
        p.start()

        self.redirect("/_ah/pipeline/status?root=%s#pipeline-%s" % (
            p.root_pipeline_id,
            p.pipeline_id
        ))


import json
class ApiHandler(webapp2.RequestHandler):
    def output(self, result):
        result = json.dumps(result)

        if self.request.method == 'GET' and self.request.GET.get('callback', False):
            result = "{}({})".format(self.request.GET.get('callback'), result)
            content_type = 'application/javascript'    
        else:
            content_type = 'application/json'

        self.response.content_type = content_type
        self.response.write(result)

    def handle_exception(self, exception, debug):
        result = {
                'status': 'error',
                'msg': exception.message
            }
        result = json.dumps(result)

        self.response.status = 500
        self.response.write(result)




class PipelineApi(ApiHandler):
    def get(self, _id):
        try:
            assert _id, 'id is not define'
            code = _GP_code.get_by_id(int(_id))
            
        except Exception as e:
            raise Exception(' get pipeline code error')

        result = {
                'exec_code' : code.exec_code,
                'eval_code' : code.eval_code,
                'name' : code.name
            }
        
        self.output(result)


    def post(self, _id=None):
        exec_code = self.request.POST.get('exec_code')
        eval_code = self.request.POST.get('eval_code')
        name = self.request.POST.get('name')
    
        try:
            assert id, 'no id'
            code = _GP_code.get_by_id(_id)
        except Exception as e:
            code = _GP_code()

        code.exec_code = exec_code
        code.eval_code = eval_code
        code.name = name

        code.put()

        result = {"id": code.key.id()}

        self.output(result)



