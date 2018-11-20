import tornado, database

class AddHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('templates/add.html', title='Add')


class HomePageHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('templates/index.html', title='Home Page')


class StaffListHandler(tornado.web.RequestHandler):
    def initilize(self, all_records):
        self.all_records=all_records

    def get(self):
        all_records=database.get_all()
        self.render('templates/list.html', all_records=all_records, title='Staff List')


class DBInitHandler(tornado.web.RequestHandler):
    def get(self):
        database.db_init()
        self.render('templates/list.html', title='Drop DB and fill with prepared data')
