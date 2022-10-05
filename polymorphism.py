class Person: # parent class called "Person"
    name = 'Not Provided'
    age = 'Unknown'
    school = 'Terry High School'

    def information(self):
        msg = "\nName: {}, \nAge: {}, \nSchool: {}".format(self.name,self.age,self.school)
        return msg

class Student(Person): # child class
    grade = '11th'
    elective = 'Choir'
    name = "Hannah"

    def information(self): # altered the information() by adding "Grade" and "Elective"
        msg = "\nName: {}, \nAge: {}, \nSchool: {}, \nGrade: {}, \nElective: {}".format(self.name,self.age,self.school,self.grade,self.elective)
        return msg


class Teacher(Person): # child class
    subject = 'Math'
    roomNumber = 'J105'
    age = 32
    name = "Maria"

    def information(self): # altered the information() by adding "Subject" and "Room Number"
        msg = "\nName: {}, \nAge: {}, \nSchool: {}, \nSubject: {}, \nRoom Number: {}".format(self.name,self.age,self.school,self.subject,self.roomNumber)
        return msg


if __name__ == "__main__":
    student = Student()
    print(student.information())

    teacher = Teacher()
    print(teacher.information())
