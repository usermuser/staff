import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        # self.write("Hello, world")
        self.render('templates/list.html', title='Staff List')
