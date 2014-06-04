import webapp2
from views.apis import PipelineTrigger, PipelineApi

from views.pages import TestView


app = webapp2.WSGIApplication([
    (r'/api/pipeline/([\w]+)/trigger$', PipelineTrigger),
    (r'/api/pipeline/?([\w]*)$', PipelineApi),

    (r'/test', TestView)
], debug=True)
