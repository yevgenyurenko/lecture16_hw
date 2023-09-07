class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f"Hi, my name is {self.name}, and I am {self.age} years old.")

class Student(Person):
    def __init__(self, name, age, gender, student_id, year_of_study, tuition_fee, marks):
        super().__init__(name, age, gender)
        self.student_id = student_id
        self.year_of_study = year_of_study
        self.tuition_fee = tuition_fee
        self.marks = marks

    def study_cost(self):
        # Calculate the total cost of studying after applying any scholarship
        scholarship = 1000  # For example
        return self.tuition_fee - scholarship

    def add_mark(self, mark):
        self.marks.append(mark)

    def average_mark(self):
        return sum(self.marks) / len(self.marks)

class Teacher(Person):
    def __init__(self, name, age, gender, subject, salary):
        super().__init__(name, age, gender)
        self.subject = subject
        self.salary = salary

    def monthly_bonus(self):
        # Calculate the monthly bonus for the teacher
        return self.salary * 0.1

    def monthly_salary(self):
        # Calculate the total monthly salary, including the bonus if applicable
        return self.salary + self.monthly_bonus()


student1 = Student('John', 20, 'Male', '2023001', 2, 5000, [80, 90, 95])
student1.introduce()
print(f"Student ID: {student1.student_id}")
print(f"Study Cost: {student1.study_cost()}")
print(f"Average Mark: {student1.average_mark()}")

teacher1 = Teacher('Alice', 35, 'Female', 'Math', 5000)
teacher1.introduce()
print(f"Subject: {teacher1.subject}")
print(f"Monthly Salary: {teacher1.monthly_salary()}")

        