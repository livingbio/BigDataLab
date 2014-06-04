import webapp2
from models import _GP_code, GenericPipeline
from mapreduce import base_handler

class PipelineTrigger(webapp2.RequestHandler):
    def get(self, _id):
        assert _id

        p = GenericPipeline(id)
        p.start()

        self.redirect("/_ah/pipeline/status?root=%s#pipeline-%s" % (
            p.root_pipeline_id,
            p.pipeline_id
        ))

class PipelineApi(webapp2.RequestHandler):
    def get(self):
        # get piplein details
        pass

    def post(self):
        # create / update pipeline
        pass

app = webapp2.WSGIApplication([
    (r'/api/pipeline/([\w]+)/trigger', PipelineTrigger),
    (r'/api/pipeline', PipelineApi),
], debug=True)
