import webapp2
from models import _GP_code, GenericPipeline
from mapreduce import base_handler

# _GP_code(
#     id=1,
#     name="test1",
#     exec_code="""
# def run(code):
#     from collections import Counter
#     c = Counter()
#     c.update(code)
#     yield Return(c)
# """,
#     eval_code="""
# run(code)
# """
# ).put()

# _GP_code(
#     id=3,
#     name="test3",
#     exec_code="""
# def run(values):
#     from collections import Counter
#     c = Counter()
#     for v in values:
#         c.update(v)

#     yield Return(c)
# """,
#     eval_code="""
# run(values)
# """
# ).put()

# _GP_code(
#     id=2,
#     name="test2",
#     exec_code="""
# def run():
#     arrays = []
#     with InOrder:
#     for i in range(10):
#         arrays.append(( yield Pipe(1, code="123 456 789")))

#     yield Pipe(3, values=arrays)
# """,
#     eval_code="""
# run()
# """
# ).put()


# from mapreduce.lib.pipeline import common
# from mapreduce.lib import pipeline
import pipeline
import pipeline.common

class TestParallelism(pipeline.Pipeline):
  def run(self, u):
    return sum(range(u))

class TestAchievingParallelism(pipeline.Pipeline):
  def run(self):
    results = []
    for u in range(10):
      results.append((yield TestParallelism(u)))

    yield pipeline.common.Sum(*results)

class Test(webapp2.RequestHandler):
    def get(self):
        # p = GenericPipeline(2)
        p = TestAchievingParallelism()
        p.start()
        self.redirect("%s/status?root=%s#pipeline-%s" % (
            p.base_path,
            p.root_pipeline_id,
            p.pipeline_id
        ))

app = webapp2.WSGIApplication([
    (r'.*', Test)
], debug=True)
