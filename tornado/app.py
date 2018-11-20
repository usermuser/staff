# -*- coding: utf-8 -*-
import tornado.ioloop
import tornado.web
from tornado.web import url
from tornado.options import define, options
import handlers
import settings


def make_app():
    return tornado.web.Application([
        url(r'/', handlers.HomePageHandler, name='home'),
        url(r'/staff/list', handlers.StaffListHandler, name='list'),
        url(r'/staff/add', handlers.AddHandler, name='add'),
        url(r'/staff/drop', handlers.DBInitHandler, name='drop'),
        url(r'/staff/delete', handlers.DelHandler, name='delete'),
    ], autoreload=False)

def main():
    app = make_app()
    server = tornado.httpserver.HTTPServer(app)
    server.bind(options.port)
    print('server started on port {}:'.format(options.port))
    # print(options.as_dict()) #
    # since i use ubuntu, think about using listen
    # instead of bind https://github.com/tornadoweb/tornado/issues/2426
    server.start(0)  # forks one process per cpu
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()


