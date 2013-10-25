from tornado import ioloop
from tornado import web


class Main(web.RequestHandler):
    def get(self):
        self.write('Hola')


application = web.Application([
    (ur'/', Main),
])


if __name__ == '__main__':
    application.listen('8888')
    ioloop.IOLoop.instance().start()
