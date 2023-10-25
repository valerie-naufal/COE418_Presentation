import PySimpleGUI as sg 
import json, time
import mysql.connector
from mysql.connector import errorcode
import utils
sg.set_options(font = ('Avenir Next',12))
menu_def = [["Menu",["Registrar" ,"Registration" ,"List"]]]

header = ["Student Full Name", "Course Registered"]
table_data=[]

#registrar page layout 
left_side = sg.Column([
    [sg.Text("First Name: "), sg.Input(key="firstname", do_not_clear=False)],
    [sg.Text("Last Name: "), sg.Input(key="lastname", do_not_clear=False)],
    [sg.Text("Student ID: "), sg.Input(key="id", do_not_clear=False)],
    [sg.Button("Add Student")],  
    [sg.Button("Remove Student")] 
], element_justification='l', expand_x=True, expand_y=True)

right_side = sg.Column([
    [sg.Text("Course Name: "), sg.Input(key="coursename", do_not_clear=False)],
    [sg.Text("Course ID: "), sg.Input(key="CRN", do_not_clear=False)],
    [sg.Button("Add Course")],
    [sg.Button("Remove Course")]
], element_justification='r', expand_x=True, expand_y=True)

layout1 = [
    [sg.Text("Registrar - Insert Students and Courses ", font = ('Avenir Next',12, 'bold'))],
    [left_side, right_side],
    [sg.Button("Exit")]
]

#registration page layout 
layout2 = [
    [sg.Text("Registration", font = ('Avenir Next',12, 'bold'))],
    [sg.Text("Course ID: "), sg.Input(key="CRN_2", do_not_clear=False)],
    [sg.Text("Student ID: "), sg.Input(key="id_2", do_not_clear=False)],
    [sg.Button("Register Course")]
]

#list page layout 
layout3 = [
    [sg.Text("List Students and Courses", font = ('Avenir Next',12, 'bold'))],
    [sg.Table(key="table",values = table_data, headings = header, display_row_numbers=True, justification="center", alternating_row_color="#0b3c61", expand_x=True, expand_y=True,
               auto_size_columns=True)],
    [sg.Button("Load Students")]
]

#main application layout
layout =[
    [sg.MenubarCustom(menu_def, tearoff= False)],
    [sg.Column(layout1, key="layout1"), sg.Column(layout2, key="layout2", visible= False), sg.Column(layout3, key="layout3", visible= False)]
]

window = sg.Window("Banner", layout, resizable=True)
col = 1

while True:

    try:
        cnx = mysql.connector.connect(user='root', password='root',
                                host='127.0.0.1',
                                database='Project_db')
        
        cursor = cnx.cursor()
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)

    event, values = window.read()
    print(event, values)
    if event in (sg.WINDOW_CLOSED, "Exit"):
        break 
    if event == "Registrar" and col != 1:
        col = 1
        window["layout1"].update(visible=True)
        window["layout2"].update(visible=False)
        window["layout3"].update(visible=False)

    elif event == "Registration" and col != 2:
        col = 2
        window["layout1"].update(visible=False)
        window["layout2"].update(visible=True)
        window["layout3"].update(visible=False)

    elif event == "List" and col != 3:
        col = 3
        window["layout1"].update(visible=False)
        window["layout2"].update(visible=False)
        window["layout3"].update(visible=True)

    if event == "Add Student":
        user = {"id": values['id'], "firstname": values['firstname'], "lastname": values['lastname']}
        utils.add_student_to_db(user,cursor,cnx)

    if event == "Remove Student":
        user = {"id": values['id'], "firstname": values['firstname'], "lastname": values['lastname']}
        utils.remove_student_from_db(user,cursor,cnx)

    if event == "Remove Course":
        course = {"CRN": values['CRN'], "coursename": values['coursename']}
        utils.remove_course_from_db(course,cursor,cnx)

    if event == "Add Course":
        course = {"coursename": values['coursename'], "CRN": values['CRN']}
        utils.add_course_to_db(course,cursor,cnx)

    if event == "Register Course":
        user = {"CRN_2": values['CRN_2'], "id_2": values['id_2']}
        utils.register_course_in_db(user,cursor,cnx)
        
    if event == "Load Students":
        table_data = utils.get_students_from_db(cursor)
        window["table"].update(values=table_data)
        
window.close()
