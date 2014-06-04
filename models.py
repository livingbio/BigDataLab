from google.appengine.ext import ndb
import mapreduce
from mapreduce import base_handler
from mapreduce.lib.pipeline import common
from mapreduce.lib import pipeline

class _GP_code(ndb.Model):
    name = ndb.StringProperty(indexed=False)

    exec_code = ndb.TextProperty()
    eval_code = ndb.TextProperty()


class GenericPipeline(base_handler.PipelineBase):
    def __unicode__(self):
        return self.name

    def __init__(self, _id, *args, **kwargs):
        super(GenericPipeline, self).__init__(_id, *args, **kwargs)
        p = _GP_code.get_by_id(_id)
        self.name = p.name
        self.env = {
            "Pipe": GenericPipeline,
            "Return": common.Return,
            "List": common.List,
            "InOrder": pipeline.InOrder
        }
    def run(self, _id, **kwargs):
        p = _GP_code.get_by_id(_id)

        exec(p.exec_code, self.env, kwargs)
        f = eval(p.eval_code, self.env, kwargs)

        for i in f:
            yield i
