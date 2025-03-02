class Person:
    def init(self, name, nid, phone, faculty, program, semester, year):
        self.name = name
        self.__nid = nid
        self.phone = phone
        self.faculty = faculty
        self.program = program
        self.semester = semester
        self.year = year

    def print_account_details(self):
        print("Account Details:")
        print("Name:", self.name)
        print("NID:", self.__nid)
        print("Phone:", self.phone)
        print("Faculty:", self.faculty)
        print("Program:", self.program)
        print("Semester:", self.semester)
        print("Year:", self.year)


class Doctor(Person):
    def __init__(self, name, nid, phone, faculty, program, semester, year, code, course, salary):
        super().init(name, nid, phone, faculty, program, semester, year)
        self.doctor = True
        self.code = code
        self.course = course
        self.salary = salary
        self.hours_worked = 0

    def print_account_details(self):
        super().print_account_details()
        print("Doctor:", self.doctor)
        print("Code:", self.code)
        print("Course:", self.course)
        print("Salary:", self.salary)
        print("Hours Worked:", self.hours_worked)

    def check_course(self):
        return self.course

    def change_course(self, new_course):
        self.course = new_course

    def check_hours_worked(self):
        return self.hours_worked

    def check_salary(self):
        if self.hours_worked > 30:
            overtime = self.hours_worked - 30
            overtime_amount = overtime * (self.salary / 30)
            return self.salary + overtime_amount
        else:
            return self.salary

    def add_hours_worked(self, hours):
        self.hours_worked += hours

    def logout(self):
        print("Logged out.")


class Student(Person):
    def __init__(self, name, nid, phone, faculty, program, semester, year, student_id, email):
        super().init(name, nid, phone, faculty, program, semester, year)
        self.student_id = student_id
        self.university_email = email

    def print_account_details(self):
        super().print_account_details()
        print("Student ID:", self.student_id)
        print("University Email:", self.university_email)

    def check_nid(self):
        return self._Person__nid

    def change_nid(self, new_nid):
        self._Person__nid = new_nid

    def logout(self):
        print("Logged out.")


choice = input("Select login as 'doctor' or 'student': ")

if choice == 'doctor':
    name = input("Enter name: ")
    nid = input("Enter NID: ")
    phone = input("Enter phone number: ")
    faculty = "Medicine"  # Constant value
    program = "Doctorate"  # Constant value
    semester = "Spring"  # Constant value
    year = 2023  # Constant value
    code = input("Enter code: ")
    course = input("Enter course: ")
    salary = float(input("Enter salary: "))
    doctor = Doctor(name, nid, phone, faculty, program, semester, year, code, course, salary)
    print("\nAccount created successfully.")
    doctor.print_account_details()

    choice = ''
    while choice != '8':
        print("\nSelect an option:")
        print("1. Doctor Account Details")
        print("2. Check Course")
        print("3. Change Course")
        print("4. Check Hours Worked")
        print("5. Check Salary")
        print("6. Add Hours Worked")
        print("8. Logout")
        choice = input("Enter your choice: ")

        if choice == '1':
            doctor.print_account_details()
        elif choice == '2':
            print("Course:", doctor.check_course())
        elif choice == '3':
            new_course = input("Enter new course: ")
            doctor.change_course(new_course)
            print("Course changed successfully.")
        elif choice == '4':
            print("Hours Worked:", doctor.check_hours_worked())
        elif choice == '5':
            print("Salary:", doctor.check_salary())
        elif choice == '6':
            hours = float(input("Enter hours worked: "))
            doctor.add_hours_worked(hours)
            print("Hours worked added successfully.")
        elif choice == '8':
            doctor.logout()
        else:
            print("Invalid choice. Please try again.")

elif choice == 'student':
    name = input("Enter name: ")
    nid = input("Enter NID: ")
    phone = input("Enter phone number: ")
    faculty = "Engineering"
    program = "Bachelor"
    semester = "Fall"
    year = 2023
    student_id = input("Enter student ID: ")
    email = input("Enter university email: ")
    student = Student(name, nid, phone, faculty, program, semester, year, student_id, email)
    print("\nAccount created successfully.")
    student.print_account_details()

    choice = ''
    while choice != '5':
        print("\nSelect an option:")
        print("1. Student Account Details")
        print("2. Check NID")
        print("3. Change NID")
        print("5. Logout")
        choice = input("Enter your choice: ")
        if choice == '1':
            student.print_account_details()
        elif choice == '2':
            print("NID:", student.check_nid())
        elif choice == '3':
            new_nid = input("Enter new NID: ")
            student.change_nid(new_nid)
            print("NID changed successfully.")
        elif choice == '5':
            student.logout()
        else:
            print("Invalid choice. Please try again.")
else:
    print("Invalid login selection. Please try again.")