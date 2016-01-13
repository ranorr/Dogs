from dbconnection import connection

c, conn = connection()


def create_person_table():
    """Create preson table"""
    c.execute("CREATE TABLE person (Id INT PRIMARY KEY, firstName VARCHAR(25), lastName VARCHAR(25))")
    c.close()


def enter_new_person():
    id = input("id number?: ")
    firstName = input("First Name?: ")
    lastName = input("Last Name?: ")
    c.execute("INSERT INTO person (Id, firstName, lastName) VALUES (%s, %s, %s)", (id, firstName, lastName))
    conn.commit()
    print_table()


def delete_person_by_id(id):
    try:
        sql = "DELETE FROM person WHERE Id = %s"
        c.execute(sql, id)
        conn.commit()
        print_table()
    except Exception:
        print ("Something wrong happened")


def print_person_by_id(id):
    sql = "SELECT * FROM person WHERE Id = %s"
    c.execute(sql, id)
    data = c.fetchall()
    if len(data) != 0:
        for row in data:
            print row
    else:
        print "There is no person with this Id"


def print_dog_by_person_id(id):
    sql = "SELECT dog.name, dog.age FROM dog, person WHERE person.id AND dog.ownerID = %s"
    c.execute(sql, id)
    data = c.fetchall()
    if len(data) != 0:
        for row in data:
            print row
    else:
        print "There is no dog with this Id"


def print_table():
    c.execute("SELECT * FROM person")
    data = c.fetchall()
    for row in data:
        print row


print_dog_by_person_id(11111)