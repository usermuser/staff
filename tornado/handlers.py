import tornado

class AddHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('templates/add.html', title='Add')

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('templates/list.html', title='Staff List')
