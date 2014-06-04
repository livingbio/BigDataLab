import webapp2
from models import _GP_code, GenericPipeline
from mapreduce import base_handler

app = webapp2.WSGIApplication([
    # (r'.*', Test)
], debug=True)
