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
        templates = jinja_env.get_template('templates/new_post.html')
        post_title = self.request.get('title')
        post_content = self.request.get('content')
        authors_name = self.request.get('name')
        print(post_title)
        print(post_content)
        print(authors_name)
        the_variable_dict = {
        "post_title": post_title,
        "post_content": post_title,
        "authors_name": authors_name,
        }
        self.response.write(templates.render(the_variable_dict))
    def post(self):
        templates = jinja_env.get_template('templates/view_post.html')
        post_title = self.request.get('title')
        post_content = self.request.get('content')
        authors_name = self.request.get('name')
        the_variable_dict = {
        "post_title": post_title,
        "post_content": post_title,
        "authors_name": authors_name,
        }
        self.response.write(templates.render(the_variable_dict))


app = webapp2.WSGIApplication([
    # This line routes the main url ('/')  - also know as
    # The root route - to the Fortune Handler
    ('/', Game),
    ('/konamicode', KonamiCode),
    ('/newblog', BlogHandler)



], debug=True)
