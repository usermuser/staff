# -*- coding: utf-8 -*-
import tornado.ioloop
import tornado.web
from tornado.options import define, options
define("port", default=8888, help="run on the given port", type=int)


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        # self.write("Hello, world")
        self.render('templates/list.html', title='Staff List')

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ], debug=True)

def main():
    app = make_app()
    server = tornado.httpserver.HTTPServer(app)
    server.bind(options.port)
    server.start(0)  # forks one process per cpu
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()


