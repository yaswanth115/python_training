class Student:
    def __init__(self, roll_number, name, marks):
        self.roll_number = roll_number
        self.name = name

        for mark in marks:
            if not 0 <= mark <= 100:
                raise ValueError("Marks must be between 0 and 100.")

        self.marks = marks.copy()

    def calculate_total(self):
        return sum(self.marks)

    def calculate_average(self):
        if len(self.marks) == 0:
            return 0
        return self.calculate_total() / len(self.marks)

    def calculate_grade(self):
        average = self.calculate_average()

        if average >= 90:
            return "A"
        elif average >= 75:
            return "B"
        elif average >= 60:
            return "C"
        elif average >= 40:
            return "D"
        else:
            return "F"

    def display_report(self):
        print("\n--- Student Report ---")
        print("Roll Number:", self.roll_number)
        print("Name:", self.name)
        print("Marks:", self.marks)
        print("Total Marks:", self.calculate_total())
        print("Average:", round(self.calculate_average(), 2))
        print("Grade:", self.calculate_grade())


s1 = Student(101, "Ravi", [90, 85, 80, 85, 80])
s2 = Student(102, "Priya", [95, 92, 96, 90, 97])
s3 = Student(103, "Arun", [70, 75, 68, 72, 65])
s4 = Student(104, "Sneha", [55, 60, 50, 58, 62])
s5 = Student(105, "Kiran", [35, 40, 30, 38, 42])

students = [s1, s2, s3, s4, s5]

for student in students:
    student.display_report()

topper = max(students, key=lambda student: student.calculate_total())

print("\n--- Class Topper ---")
print("Name:", topper.name)
print("Roll Number:", topper.roll_number)
print("Total Marks:", topper.calculate_total())
print("Average:", round(topper.calculate_average(), 2))
print("Grade:", topper.calculate_grade())