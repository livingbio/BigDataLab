import pipeline
import pipeline.common
import webapp2

class TestParallelism(pipeline.Pipeline):
    def run(self, u):
        return sum(range(u))

class TestAchievingParallelism(pipeline.Pipeline):
  def run(self):
    results = []
    for u in range(10):
        results.append((yield TestParallelism(u)))

    yield pipeline.common.Sum(*results)


class TestNormal(webapp2.RequestHandler):
    def get(self):
        p = TestAchievingParallelism()
        p.start()
        self.redirect("/_ah/pipeline/status?root=%s#pipeline-%s" % (
            p.root_pipeline_id,
            p.pipeline_id
        ))


from models import GPCode, GenericPipeline
GPCode(
    id="TestAchievingParallelism",
    name="TestAchievingParallelism",
    exec_code="""
def run():
    results = []
    for u in range(10):
        results.append((yield Pipe("TestParallelism", u=u)))

    yield pipeline.common.Sum(*results)
""",
    eval_code="""
run()
"""
).put()

GPCode(
    id="TestParallelism",
    name="TestParallelism",
    exec_code="""
def run(u):
    return sum(range(u))
""",
    eval_code="""run(u)"""
).put()


class TestGeneric(webapp2.RequestHandler):
    def get(self):
        p = GenericPipeline(2)
        p.start()
        self.redirect("/_ah/pipeline/status?root=%s#pipeline-%s" % (
            p.root_pipeline_id,
            p.pipeline_id
        ))


app = webapp2.WSGIApplication([
    (r'/test/normal', TestNormal),
    (r'/test/generic', TestGeneric)
], debug=True)




