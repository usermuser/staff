import tornado, database

class AddHandler(tornado.web.RequestHandler):
    # def get(self):
    #     self.render('templates/add.html', title='Add')

    def post(self):
        name = self.get_argument('name')
        surname = self.get_argument('surname')
        date_of_birth = self.get_argument('date_of_birth')
        sex = self.get_argument('sex')
        email = self.get_argument('email')
        salary = self.get_argument('salary')
        new_record = [name, surname, date_of_birth, sex, email, salary]
        # print('new record data', new_record)
        database.add(new_record)
        # all_records = database.get_all()
        # self.redirect('templates/list.html', title='Added new record with name: {}'.format(name))
        self.redirect('/staff/list')


class DelHandler(tornado.web.RequestHandler):
    def post(self):
        email = self.get_argument('email')
        database.delete(email)
        self.redirect('/staff/list')


class HomePageHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('templates/index.html', title='Home Page')


class StaffListHandler(tornado.web.RequestHandler):
    def initilize(self, all_records):
        self.all_records=all_records

    def get(self):
        all_records=database.get_all()
        print(all_records)
        self.render('templates/list.html', all_records=all_records, title='Staff List')


class DBInitHandler(tornado.web.RequestHandler):
    def get(self):
        database.db_init()
        # self.render('templates/list.html', title='Drop DB and fill with prepared data')
        self.redirect('/')
