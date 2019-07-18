import webapp2
import jinja2
import os

jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class Game(webapp2.RequestHandler):
    def get(self):
        templates = jinja_env.get_template('index.html')
        self.response.write(templates.render())

class KonamiCode(webapp2.RequestHandler):
    def get(self):
        templates = jinja_env.get_template('konamicode.html')
        self.response.write(templates.render())
class BlogHandler(webapp2.RequestHandler):
    def get(self):
        templates = jinja_env.get_template('new_post.html')
        self.response.write(templates.render())

app = webapp2.WSGIApplication([
    # This line routes the main url ('/')  - also know as
    # The root route - to the Fortune Handler
    ('/', Game),
    ('/konamicode', KonamiCode)


], debug=True)
