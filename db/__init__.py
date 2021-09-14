import sqlite3

COLUMN_PERSON = "people"


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.dob = dob

def write_person(person: Person):
    cur = con.cursor()
    params = [person.name, person.age, person.dob]
    cur.execute(f'insert into {COLUMN_PERSON} (name, age) values(?, ?, ?)', params)
    con.commit()

def get_person(con, name) -> Person:
    cur = con.cursor()
    cur.execute('select * from name where name = ?', [name])
    rows = cur.fetchall()
    if len(rows) == 0:
        return None

    return Person(rows[0][0], rows[0][1])

def get_person(person):
    pass

if __name__ == '__main__':
    person = Person("", 10)

    "<10, IS_PROFICIENT>"
