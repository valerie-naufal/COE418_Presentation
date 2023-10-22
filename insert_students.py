import json, time
import mysql.connector
from mysql.connector import errorcode

# Global Variable Definition

insert_student = ("INSERT INTO students "
               "(studentId, firstname, lastname) "
               "VALUES (%s, %s, %s)")

get_students = ("SELECT * FROM students")

students = []

def add_student_to_db(user):
    # Sample User : { "firstname": "Valerie", "lastname": "Naufal", "id": "382761819" }
    cursor.execute(insert_student, (user.get("id"), user.get("firstname"),user.get("lastname")))
    cnx.commit()

if __name__ == "__main__":
    try:
        cnx = mysql.connector.connect(user='root', password='root',
                                host='127.0.0.1',
                                database='Project_db')
        
        cursor = cnx.cursor()

        # Python File Interaction
        with open("users.json") as f:
            # Read File Content --> str
            file_data = f.read()
            # Convert str file data into python obj
            users = json.loads(file_data)
            
            #Adding the Students to MySQL DB
            for user in users:
                add_student_to_db(user);
        
        print("STUDENTS INSERTED INTO DB")
        cnx.close()
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)

    
