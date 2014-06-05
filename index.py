import webapp2
from views.apis import PipelineTrigger, PipelineApi

app = webapp2.WSGIApplication([
    (r'/api/pipeline/([\w]+)/trigger$', PipelineTrigger),
    (r'/api/pipeline/?([\w]*)$', PipelineApi),

], debug=True)
