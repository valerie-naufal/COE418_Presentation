from student import Student

insert_student = ("INSERT INTO students "
               "(studentId, firstname, lastname) "
               "VALUES (%s, %s, %s)")

insert_course = ("INSERT INTO courses "
               "(CRN, courseName) "
               "VALUES (%s, %s)")

register_course = ("UPDATE students SET courseId=%s WHERE studentId=%s")

get_students = ("SELECT students.firstName,students.lastName, courses.courseName "
                "from students INNER JOIN courses ON students.courseId=courses.CRN")

remove_student = ("DELETE from students WHERE studentId=%s AND firstname=%s AND lastname=%s")

table_data = []


def add_student_to_db(user,cursor, cnx):
    # Sample User : { "firstname": "Valerie", "lastname": "Naufal", "id": "382761819" }
    cursor.execute(insert_student, (user.get("id"), user.get("firstname"),user.get("lastname")))
    cnx.commit()

def add_course_to_db(course,cursor, cnx):
    # Sample Course : { "coursename": "database", "CRN": "1234"}
    cursor.execute(insert_course, (course.get("CRN"), course.get("coursename")))
    cnx.commit()

def register_course_in_db(user,cursor,cnx):
    # Sample registartion : { "coursename": "database", "CRN": "1234"}
    cursor.execute(register_course, (user.get("CRN_2"), user.get("id_2")))
    cnx.commit()

def get_students_from_db(cursor): 
    cursor.execute(get_students)
    for(firstname, lastname, coursename) in cursor:
        table_data.append([firstname +" "+ lastname, coursename])
    return table_data

def remove_student_from_db(user,cursor,cnx):
    cursor.execute(remove_student, (user.get("id"),user.get("firstname"),user.get("lastname")))
    cnx.commit()

