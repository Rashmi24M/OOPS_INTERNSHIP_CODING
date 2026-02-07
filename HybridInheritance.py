#College Management System
class Person:
    def __init__(self,name):
        self.name=name
    def display_person(self):
        print("Name:",self.name)
class Student(Person):              #Hierarchical Inheritance
    def __init__(self,name,student_id):
        Person.__init__(self,name)         #In hybrid inheritance super() cannot be used beacuse it casuses confusion here super means calling next class in mro, means calling its  before one class not parent one like in hierachical in hierrachical super()  works fine  beacuse only one parent 
        self.student_id=student_id
    def display_student(self):
        print("Student name:",self.name,"Student ID:",self.student_id)
        
class SportsPlayer(Person):
    def __init__(self,name,sport_name):
        Person.__init__(self,name)
        self.sport_name=sport_name
    def display_sports_player(self):
        print("The sports player is:",self.name)
        
class CollegeStudent(Student,SportsPlayer):    #Multiple Inheritance
    def __init__(self,name,student_id,sport_name,college_name):
        Student.__init__(self,name,student_id)
        SportsPlayer.__init__(self,name,sport_name)
        self.college_name=college_name
        
    def display_college_student(self):
        print("Student Name:",self.name)
        print("Student ID:",self.student_id)
        print("Sport Name:",self.sport_name)    
        print("College Name:",self.college_name)
        
stud=CollegeStudent("Rashmi",1234,"Badminton","MRIT")
stud.display_college_student()