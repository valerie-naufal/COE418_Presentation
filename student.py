class Student:
    def __init__(self, studentId, firstname, lastname):
        self.studentId=studentId
        self.firstname=firstname
        self.lastname=lastname

    def get_full_name(self):
        return self.firstname + " " + self.lastname
    
    def get_student_entry(self):
        return self.firstname + "_" + self.lastname + "_" + str(self.studentId)
