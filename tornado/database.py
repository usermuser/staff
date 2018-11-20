import sqlite3 as lite

## I'm not using try except constructions because of speed
## Going to add them in refactoring phase
DATABASE='staff.db'
people = (
    (1, 'Max', 'Frei', '01.01.1980', 'F', 'max_01@gmail.com', 1000),
    (2, 'Guido', 'Helsing', '03.05.1985', 'M', 'guido_van_helsing@rambler.ru', 2999),
    (3, 'James', 'Bennet', '13.12.2000', 'M', 'jamesbennet@yandex.ru', 5000),
)
def db_init(dbname=DATABASE): # Drop table and fill with test data
    con = lite.connect(dbname)
    with con:
        cur = con.cursor()
        cur.execute("DROP TABLE IF EXISTS Staff_table")
        cur.execute("CREATE TABLE Staff_table(Id INT, Name TEXT, Surname TEXT, Date_of_Birth DATE, Sex TEXT, Email TEXT, Salary INT)")
        cur.executemany("INSERT INTO Staff_table VALUES(?, ?, ?, ?, ?, ?, ?)", people)
    return

def add(new_record, dbname=DATABASE):
    # TODO fix wrong Id writing to db while adding new_record
    con = lite.connect(dbname)
    with con:
        cur = con.cursor()
        new_record.insert(0,5) # 0 - index, 5 - Id value to be inserted in db
        cur.execute('INSERT INTO Staff_table VALUES(?, ?, ?, ?, ?, ?, ?)',new_record)
        con.commit()


def delete(email, dbname=DATABASE): # delete record from db, where email==given email
    con = lite.connect(dbname)
    with con:
        cur = con.cursor()
        cur.execute('DELETE FROM Staff_table WHERE Email={}'.format(email))
        con.commit()


def get_filtered_by_sex(dbname=DATABASE,sex='M'): # temporary hardcode sex='M' for testing
    sex.upper()
    con = lite.connect(dbname)
    with con:
        cur = con.cursor()
        cur.execute("SELECT Name, Surname, Sex, Salary FROM Staff_table WHERE Sex=:sex",{'sex':sex})

    rows = cur.fetchall()
    print(rows)
    return rows


def get_all(dbname=DATABASE):
    con = lite.connect(dbname)
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Staff_table")
    rows = cur.fetchall()
    return rows

if __name__ == "__main__":
    db_init()


