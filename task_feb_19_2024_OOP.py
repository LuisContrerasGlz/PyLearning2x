# Class -Students,Courses, Payments 

class Course:
    def __init__(self, course_code, course_name, credits):
        # Constructor initializes the attributes of the Course class
        self.course_code = course_code
        self.course_name = course_name
        self.credits = credits
        self.students_enrolled = []

    def add_student(self, student):
        # Method to add a student to the list of enrolled students
        self.students_enrolled.append(student)

    def display_info(self):
        # Method to display information about the course
        print(f"Course: {self.course_code} - {self.course_name}")
        print(f"Credits: {self.credits}")
        print("Enrolled Students:")
        for student in self.students_enrolled:
            print(f"  {student.name}")

class Student:
    def __init__(self, student_id, name, age):
        # Constructor initializes the attributes of the Student class
        self.student_id = student_id
        self.name = name
        self.age = age
        self.courses_enrolled = []

    def enroll_in_course(self, course):
        # Method to enroll a student in a course and add the student to the course's list
        self.courses_enrolled.append(course)
        course.add_student(self)

    def display_info(self):
        # Method to display information about the student
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print("Enrolled Courses:")
        for course in self.courses_enrolled:
            print(f"  {course.course_code} - {course.course_name}")

class Payment:
    def __init__(self, payment_id, amount, date):
        # Constructor initializes the attributes of the Payment class
        self.payment_id = payment_id
        self.amount = amount
        self.date = date

    def process_payment(self, student):
        # Method to process a payment for a student
        # Add payment processing logic here
        print(f"Payment of ${self.amount} processed for student {student.name} on {self.date}")

    def display_info(self):
        # Method to display information about the payment
        print(f"Payment ID: {self.payment_id}")
        print(f"Amount: ${self.amount}")
        print(f"Date: {self.date}")

# Example usage
course_math = Course("MATH101", "Introduction to Mathematics", 3)
course_physics = Course("PHYS101", "Physics for Beginners", 4)

student_john = Student(1, "John Doe", 20)
student_jane = Student(2, "Jane Smith", 22)

course_math.add_student(student_john)
course_physics.add_student(student_jane)

payment1 = Payment(1, 500, "2024-02-27")
payment2 = Payment(2, 750, "2024-03-05")

payment1.process_payment(student_john)

course_math.display_info()
course_physics.display_info()

student_john.display_info()
student_jane.display_info()

payment1.display_info()
payment2.display_info()
