import sqlite3

class StudentManagementSystem:
    def __init__(self):
        self.__conn = sqlite3.connect('students.db')
        self.__c = self.__conn.cursor()
        try:
            self.__c.execute("""CREATE TABLE students(
                        Id INTEGER PRIMARY KEY AUTOINCREMENT,
                        Name TEXT NOT NULL,
                        Age INTEGER,
                        Program TEXT,
                        Grade REAL)""")

        except sqlite3.OperationalError:
            None

    @property
    def system_connection(self):
        return self.__conn
    
    def add_student(self, name:str, age:int=None, program:str=None, grade:int|float=None):
        if age == "":
            age = None

        if grade == "":
            grade = None
            
        if age != None:
            try:
                age = int(age)
            except ValueError:
                return "Age must be a type int or None. Back to main menu."
            else:
                if age < 1 or age > 150:
                    raise ValueError("age must be realistic")
        if grade != None:
            try:
                grade = float(grade)
            except ValueError:
                return "grade must be a type float or None. Back to main menu."
            else:
                if grade < 0 or grade > 100:
                    raise ValueError("grade must be strictly between 0 and 100 inclusively")
        if name.strip() == '':
            return 'Student name must not be empty.'
        if program.strip() == '':
            return 'Program must not be empty.'

        with self.__conn:
            self.__c.execute("INSERT INTO students(Name, Age, Program, Grade) VALUES (:name, :age, :program, :grade)", {"name":name.strip(), "age":age, "program":program.strip(), "grade":grade})

        return "Student has been added to the system."

    def view_students(self):
        self.__c.execute("SELECT * FROM students")
        return self.__c.fetchall()
           

    def search_student(self, student_name:str=None, student_id:int=None):
        with self.__conn:
            if student_name:
                self.__c.execute("SELECT * FROM students WHERE Name LIKE :name", {'name':student_name})
                return self.__c.fetchall()
            elif student_id:
                self.__c.execute("SELECT * FROM students WHERE Id = :student_id", {'student_id': student_id})
                return self.__c.fetchall()
            else:
                return None
            
    def update_student(self, column_name:int, value:str|int|float, student_id:int=None):
        if column_name ==  2:
            if value == "":
                value = None
            if value != None:
                try:
                    value = int(value)
                except ValueError:
                    return "Age must be an int. Back to main menu."
                else:
                    if int(value) < 1 or int(value) > 150:
                        raise ValueError("age must be realistic")

        if column_name == 4:
            if value == "":
                value = None
            if value != None:
                try:
                    value = float(value)
                except ValueError:
                    return "Grade must be a float. Back to main menu."
                if float(value) < 0 or float(value) > 100:
                    raise ValueError("grade must be strictly between 0 and 100 inclusively")
                
        with self.__conn:
            answer = None
            if student_id != None:
                if column_name == 1:
                    self.__c.execute("UPDATE students SET Name = :value WHERE Id = :student_id", {'value':value, 'student_id':student_id})
                elif column_name == 2:
                    self.__c.execute("UPDATE students SET Age = :value WHERE Id = :student_id", {'value':value, 'student_id':student_id})
                elif column_name == 3:
                    self.__c.execute("UPDATE students SET Program = :value WHERE Id = :student_id", {'value':value, 'student_id':student_id})
                elif column_name == 4:
                    self.__c.execute("UPDATE students SET Grade = :value WHERE Id = :student_id", {'value':value, 'student_id':student_id})
                else:
                    return "No choice was made. Back to main menu."
                updated_rows = self.__c.rowcount
                if updated_rows == 0:
                    return "Student id is not in the system." 
                else: 
                    return "The student information has been updated."

            else:
                return "No choice was made. Back to main menu."

    def delete_student(self, student_id:int=None):
        with self.__conn:
            answer = None
            if student_id != None:
                self.__c.execute("DELETE FROM students WHERE Id = :student_id", {'student_id':student_id})
                updated_rows = self.__c.rowcount
                if updated_rows == 0:
                    return "Student id is not in the system."
                else:
                    return "The student has been deleted."

            else:
                return "No choice was made. Back to main menu."

    def calculate_statistic(self):
        with self.__conn:
            self.__c.execute("SELECT COUNT(Id) FROM students")
            total_students = self.__c.fetchall()
            self.__c.execute("SELECT AVG(Grade) FROM students")
            class_avg =  self.__c.fetchall()
            self.__c.execute("SELECT MAX(Grade) FROM students")
            max_grade = self.__c.fetchall()
            self.__c.execute("SELECT MIN(Grade) FROM students")
            min_grade = self.__c.fetchall()

            return f"Number of students: {total_students[0][0]}\nClass average: {class_avg[0][0]}\nHighest grade: {max_grade[0][0]}\nLowest grade: {min_grade[0][0]}"

    def sort_students(self, choice:int):
        if not isinstance(choice, int):
            raise TypeError("choice must be strictly int")

        with self.__conn:
            if choice == 1:
                self.__c.execute("SELECT * FROM students ORDER BY Name ASC")
                return self.__c.fetchall()
            
            elif choice == 2:
                self.__c.execute("SELECT * FROM students ORDER BY Name DESC")
                return self.__c.fetchall()
            
            elif choice == 3:
                self.__c.execute("SELECT * FROM students ORDER BY Grade, Name")
                return self.__c.fetchall()
            
            elif choice == 4:
                self.__c.execute("SELECT * FROM students ORDER BY Grade DESC, Name")
                return self.__c.fetchall()
            
            elif choice == 5:
                self.__c.execute("SELECT * FROM students ORDER BY Age ASC")
                return self.__c.fetchall()
            
            elif choice == 6:
                self.__c.execute("SELECT * FROM students ORDER BY Age DESC")
                return self.__c.fetchall()

            else:
                return"Sorry! Options not choosen."

def menu_display():
    return "\n============================\n| Student Management System |\n============================\n1. Add students\n2. View students\n3. Search students\n4. Update students\n5. Delete students\n6. Calculate class statistics\n7. Sort student\n8. Exit program"

def sort_students_menu():
    return "\n====================\n| Sort students by: |\n====================\n1. Name A -> Z\n2. Name Z -> A\n3. Grade lowest to highest\n4. Grade highest to lowest\n5. Age lowest to highest\n6. Age highest to lowest"

def update_students_menu():
    return "\n==========================\n| Choose data to update: |\n==========================\n1. Name \n2. Age \n3. Program \n4. Grade"
