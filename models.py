from google.appengine.ext import ndb
import pipeline
from pipeline import common

def _issubclass(a, b):
    """ issubclass will raise exception while a is not a class type"""
    try:
        return issubclass(a, b)
    except:
        pass

    return False

COMMON_PIPE = {k: common.__dict__[k]
    for k in dir(common.__dict__)
    if not k.startswith('_') and k in common.__dict__ and _issubclass(common.__dict__[k], pipeline.Pipeline)
}

class _GP_code(ndb.Model):
    name = ndb.StringProperty(indexed=False)

    exec_code = ndb.TextProperty()
    eval_code = ndb.TextProperty()


class GenericPipeline(pipeline.Pipeline):
    def __unicode__(self):
        return self.name

    def __init__(self, _id, *args, **kwargs):
        super(GenericPipeline, self).__init__(_id, *args, **kwargs)
        p = _GP_code.get_by_id(_id)
        self.name = p.name
        self.env = {
            "Pipe": GenericPipeline,
            "InOrder": pipeline.InOrder,
            "After": pipeline.After
        }
        self.env.update(COMMON_PIPE)

    def run(self, _id, **kwargs):
        p = _GP_code.get_by_id(_id)
        assert p

        exec(p.exec_code, self.env, kwargs)
        f = eval(p.eval_code, self.env, kwargs)

        for i in f:
            yield i
