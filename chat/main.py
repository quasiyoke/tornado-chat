import colors
import json
from os import path
from tornado import ioloop
from tornado import template
from tornado import web
from tornado import websocket

PROJECT_PATH = path.dirname(__file__)

template_loader = template.Loader(path.join(PROJECT_PATH, 'templates'))


class Main(web.RequestHandler):
    def get(self):
        self.write(template_loader.load('main.html').generate(color=colors.get_random_color()))


class Socket(websocket.WebSocketHandler):
    def open(self):
        sockets.append(self)

    def on_message(self, message):
        message = json.loads(message)
        if message['type'] == 'set_color':
            self.color = message['color']
            sockets.write_message({
                'type': 'user_come',
                'color': self.color
            }, exc=self)
        elif not hasattr(self, 'color'):
            return
            

    def on_close(self):
        sockets.remove(self)


class Sockets(object):
    _sockets = []

    def write_message(self, message, exc=None):
        for socket in self._sockets:
            if socket != exc:
                socket.write_message(message)

    def append(self, socket):
        self._sockets.append(socket)

    def remove(self, socket):
        self._sockets.remove(socket)
        message = {
            'type': 'user_gone',
        }
        if hasattr(socket, 'color'):
            message['color'] = socket.color
        self.write_message(message)

sockets = Sockets()


application = web.Application([
    (ur'/', Main),
    (ur'/socket/', Socket),
    (ur'/static/(.*)', web.StaticFileHandler, {'path': path.join(PROJECT_PATH, 'static')}),    
])


if __name__ == '__main__':
    application.listen('8888')
    ioloop.IOLoop.instance().start()
