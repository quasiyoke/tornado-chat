import colors
from os import path
from tornado import ioloop
from tornado import template
from tornado import web

PROJECT_PATH = path.dirname(__file__)

template_loader = template.Loader(path.join(PROJECT_PATH, 'templates'))


class Main(web.RequestHandler):
    def get(self):
        self.write(template_loader.load('main.html').generate(color=colors.get_random_color()))


application = web.Application([
    (ur'/', Main),
    (ur'/static/(.*)', web.StaticFileHandler, {'path': path.join(PROJECT_PATH, 'static')}),    
])


if __name__ == '__main__':
    application.listen('8888')
    ioloop.IOLoop.instance().start()
