import webapp2
import jinja2

jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))

class HtmlHandler(webapp2.RequestHandler):
    def HtmlResponse(self, template_path, data):
        template = jinja_environment.get_template(template_path)
        self.response.out.write(template.render(data))

    def handle_exception(self, exception, debug):
        raise

class IndexPage(HtmlHandler):
    def get(self):
        self.HtmlResponse("index.html", {"app_id": "bigdatalab"})
