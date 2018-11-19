# -*- coding: utf-8 -*-
import tornado.ioloop
import tornado.web
from tornado.options import define, options
from handlers import MainHandler, AddHandler
import settings


def make_app():
    return tornado.web.Application([
        (r'/', MainHandler),
        (r'/staff/add', AddHandler),
    ], autoreload=False)

def main():
    app = make_app()
    server = tornado.httpserver.HTTPServer(app)
    server.bind(options.port)
    print('server started on port {}:'.format(options.port))
    # since i use ubuntu, think about using listen
    # instead of bind https://github.com/tornadoweb/tornado/issues/2426
    server.start(0)  # forks one process per cpu
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()


