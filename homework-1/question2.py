from statistics import mean


# I have chosen to include the functions within the Student class so these are able to
# be accessed by both subclasses that I have created to represent students
# on the software and data stream. These functions are now able to be for both subclasses.

class Student():
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id
        self.subjects = {}

    def view_student_details(self):
        """This function lists student details
        so the user would be able to know who's subjects and grades
        are being views"""
        print(f"Student Name: {self.name}\nStudent Age: {self.age}\nStudent ID: {self.id}")

    def add_subject_and_grade(self, subject_and_grade):
        """This function allows subject and grade to be added
        to the students record within a dict"""
        self.subjects.update(subject_and_grade)

    def view_specialisation(self):
        """This function is linked to the subclasses and allows
        the user to view the students specialisation"""
        print(f"Student Specialisation is {self.specialisation}")

    def remove_subject_and_grade(self, subject):
        """This function allows subject and grade to be removed
        from the students record"""
        self.subjects.pop(subject)

    def view_all_subjects(self):
        """This function allows you to view all subjects and grades
        on a students record"""
        for subject, grade, in self.subjects.items():
            print(f"Subject: {subject}\n Grade: {grade}")

    def view_student_overall_mark(self):
        """This function uses a new variable to calculate the students
        overall grade (average) from all their subject grades"""
        overall_grade = mean(self.subjects.values())
        print(f"Students overall grade is {overall_grade:.2f}")


# I have created a subclass for the SoftwareStudents and specified the specialisation

class SoftwareStudent(Student):
    def __init__(self, name, age, id, specialisation="Software"):
        super().__init__(name, age, id)
        self.specialisation = specialisation


# I have created a subclass for the DataStudent and specified the specialisation

class DataStudent(Student):
    def __init__(self, name, age, id, specialisation="Data"):
        super().__init__(name, age, id)
        self.specialisation = specialisation


# To show how the code works, student_1 is myself, and I have inputted my grades. I then used the functions
# to view my student details, view my specialisation, view my subjects and grades, and my overall AVG grade.

student_1 = SoftwareStudent('Nikita', 23, 2)

student_1.add_subject_and_grade({'Homework 1': 97})
student_1.add_subject_and_grade({'Homework 3': 98})
student_1.add_subject_and_grade({'Assessment 2': 100})

student_1.view_student_details()
student_1.view_specialisation()
student_1.view_all_subjects()
student_1.view_student_overall_mark()

# This also works for the DataStudents, and I have done the same as above for a made up data student:

student_2 = DataStudent('Jane', 34, 3)

student_2.add_subject_and_grade({'Homework 1': 99})
student_2.add_subject_and_grade({'Homework 3': 80})
student_2.add_subject_and_grade({'Assessment 2': 95})

student_2.view_student_details()
student_2.view_specialisation()
student_2.view_all_subjects()
student_1.view_student_overall_mark()
