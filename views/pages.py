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
<style type="text/css">
      .breakpoints {width: .8em;}
      .breakpoint { color: #822; }
      .CodeMirror {border: 1px solid #aaa;}
    </style>
            <script src="//cdnjs.cloudflare.com/ajax/libs/codemirror/4.2.0/codemirror.js"></script>
            <link rel="stylesheet" href="//cdnjs.cloudflare.com/ajax/libs/codemirror/4.2.0/codemirror.css">
            <script src="//cdnjs.cloudflare.com/ajax/libs/codemirror/4.2.0/mode/python/python.js"></script>
            <script src="//ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
            <script>
                function get_id(){
                    var id = document.location.href.split('#')[1] || "";
                    return id;
                }

                // get code object from server
                function fetch_code(id, callback){
                    if(!id){
                        return;
                    }
                    
                    $.ajax({
                        type: "GET",
                        url: "/api/pipeline/" + id ,
                        dataType: "json",
                        success: callback
                    })
                }
                // push code object to server
                function save_code(id, data, callback){
                    $.ajax({
                        type: "POST",
                        url: "/api/pipeline/" + id,
                        data: data,
                        dataType: "json",
                        success: callback
                    })
                }

                // set code object to html
                function set_code(data){
                    var exec_code = $("#exec_code").data("code");
                    var eval_code = $("#eval_code").data("code");
                    exec_code.setValue(data['exec_code']);
                    eval_code.setValue(data['eval_code']);
                    $("#name").val(data["name"]);
                }
                // get code object from html
                function get_code(){
                    var result = {};
                    var exec_code = $("#exec_code").data("code");
                    var eval_code = $("#eval_code").data("code");
                    var name = $("#name").val();
                    result['exec_code'] = exec_code.getValue();
                    result['eval_code'] = eval_code.getValue();
                    result['name'] = name;

                    return result;
                }

                //send code object to server
                function send(){
                    save_code(get_id(), get_code(), function(data){
                        document.location.href="#" + data['id'];
                    })
                }
        
                function onload(){
                    var exec_code = CodeMirror.fromTextArea($("#exec_code")[0], { value: "", mode:  "python", lineNumbers: true, gutters: ["CodeMirror-linenumbers", "breakpoints"]});
                    var eval_code = CodeMirror.fromTextArea($("#eval_code")[0], { value: "", mode:  "python", lineNumbers: true, gutters: ["CodeMirror-linenumbers", "breakpoints"]});
                    $("#exec_code").data("code", exec_code);
                    $("#eval_code").data("code", eval_code);
                    
                    fetch_code(get_id(), set_code);
                }


            </script>
        </head>
        
        <body onload="onload()">
            <h2>name:</h2> <input id="name">
            <h2>exec_code:</h2>
            <textarea  style="width:100%; height:90%;" id="exec_code"></textarea>
            <h2>eval_code:</h2>
            <textarea  style="width:100%; height:90%;" id="eval_code"></textarea>
            <BUTTON name="btn" onclick="send()">send</BUTTON>
        </body>

        '''

        self.response.write(html)
