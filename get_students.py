'''
Python class to demostrate getting data from the Database, and using the Student class 
'''

import mysql.connector
from mysql.connector import errorcode
from student import Student

# Global Variable Definition
get_students = ("SELECT studentId,firstName,lastName FROM students")

students = []

def get_students_from_db():
    cursor.execute(get_students)
    for(studentId, firstname, lastname) in cursor:
        #save each entry in a Student object
        student = Student(studentId, firstname, lastname)
        #save objects in students array
        students.append(student)  

if __name__ == "__main__":
    try:
        cnx = mysql.connector.connect(user='root', password='root',
                                host='127.0.0.1',
                                database='Project_db')
        cursor = cnx.cursor()

        get_students_from_db()
        print("Students Found in DB: ")
        
        for student in students:
            # Function belonging to Student Class
            print(student.get_full_name())

        cnx.close()
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)

    
