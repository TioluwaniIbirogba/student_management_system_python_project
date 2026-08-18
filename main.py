from student_management_system import StudentManagementSystem, sort_students_menu, menu_display, update_students_menu

student_management_system = StudentManagementSystem()
while True:
    print(menu_display())
    try:
        choice = int(input('Enter here: '))

    except ValueError:
        print(('Write a number here:') + (menu_display()))

    else:
        if choice == 1:
            info_name = input('Name: ')
            info_age = input('Age: ')
            info_program = input('Program: ')
            info_grade = input('Grade: ')
            print(student_management_system.add_student(info_name, info_age, info_program, info_grade))

        elif choice == 2:
                student_info = student_management_system.view_students()
                if len(student_info) == 0:
                    print("No students in the system yet.")
                else:
                    for i in range(len(student_info)):
                        student_id = student_info[i][0]
                        student_name = student_info[i][1]
                        student_age = student_info[i][2]
                        student_program = student_info[i][3]
                        student_grade = student_info[i][4]
                        print(f"| ID: {student_id} | Name:  {student_name} | Age: {student_age} | Program: {student_program} | Grade: {student_grade}")

        elif choice == 3:
            search_choice = input("Choose student name or id: ")
            if search_choice.lower() == 'student id' or search_choice.lower() == 'id':
                try:
                    id_choice = int(input('Write student id: '))
                except ValueError:
                    print("Id is an integer. Back to main menu.")
                else:
                    student_info = student_management_system.search_student(student_id=id_choice)
                    if student_info != None:
                        if len(student_info) > 0:
                            print(f"| ID: {student_info[0][0]} | Name:  {student_info[0][1]} | Age: {student_info[0][2]} | Program: {student_info[0][3]} | Grade: {student_info[0][4]}")
                        elif len(student_info) == 0:
                            print("Nothing. Validate if there are student in system or the student name is in the system and correctly inputed.")
                        else:
                            print("Invalid student id.")
                    else:
                        print("No choice was made back to main menu")
                 
            elif search_choice.lower() == 'student name' or search_choice == 'name':
                name_choice = input('Write student name: ')
                student_info = student_management_system.search_student(student_name=name_choice)
                if student_info != None:
                    if len(student_info) > 0:
                        print(f"| ID: {student_info[0][0]} | Name:  {student_info[0][1]} | Age: {student_info[0][2]} | Program: {student_info[0][3]} | Grade: {student_info[0][4]}")
                    elif len(student_info) == 0:
                        print("Nothing. Validate if there are student in system or the student name is in the system and correctly inputed.")
                    else:
                        print("Invalid student id.")
                else:
                    print("No choice was made back to main menu")
                 
            else:
                print("Invalid choice. Back to menu")

        elif choice == 4:
            print(update_students_menu())
            try:
                column_name = int(input('Enter here: '))
            except ValueError:
                print("Column choice must be an integer. Back to main menu.")
            else:
                try:
                    update_id_choice = int(input('Write student id: '))
                except ValueError:
                    print("Id must be an integer. Back to main menu.")
                else:
                    value_choice = input('Write the value: ')
                    print(student_management_system.update_student(column_name, value_choice, update_id_choice))

        elif choice == 5:
            try:
                delete_id_choice = int(input('Write student id: '))
            except ValueError:
                print("Id is an integer. Back to main menu.")
            else:
                print(student_management_system.delete_student(student_id=delete_id_choice))

        elif choice == 6:
            print(student_management_system.calculate_statistic())

        elif choice == 7:
            print(sort_students_menu())
            try:
                sort_choice = int(input('Write your option number: '))
            except ValueError:
                print('Invalid option. Back to main menu.')
            else:
                students_values = student_management_system.sort_students(sort_choice)
                if students_values == 'Sorry! Options not choosen.':
                    print(students_values)
                else:
                    if len(students_values) == 0:
                        print("No students in the system yet.")
                    else:
                         for i in range(len(students_values)):
                            student_id = students_values[i][0]
                            student_name = students_values[i][1]
                            student_age = students_values[i][2]
                            student_program = students_values[i][3]
                            student_grade = students_values[i][4]
                            print(f"| ID: {student_id} | Name:  {student_name} | Age: {student_age} | Program: {student_program} | Grade: {student_grade}")          

        elif choice == 8:
            print("See you later! System closed.")
            student_management_system.system_connection.close()
            break