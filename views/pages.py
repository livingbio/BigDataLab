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


class TestView(webapp2.RequestHandler):
    def get(self):
        html = '''
        <head>
            <script src="//cdnjs.cloudflare.com/ajax/libs/codemirror/4.2.0/codemirror.js"></script>
            <link rel="stylesheet" href="//cdnjs.cloudflare.com/ajax/libs/codemirror/4.2.0/codemirror.css">
            <script src="//cdnjs.cloudflare.com/ajax/libs/codemirror/4.2.0/mode/python/python.js"></script>
            <script src="//ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
            <script>
                $( document ).ready(function(){
                    var myCodeMirror = CodeMirror($("#code")[0], {
                    value: "",
                        mode:  "python"
                    });
                
                })

                function send(){
                }
            </script>
        </head>
        
        <body>
            <div style="width:100%; height:90%;" id="code">
            <buttom>test</buttom>
        </body>

        '''

        self.response.write(html)
