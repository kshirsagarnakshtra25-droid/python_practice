from student import add_student
from student import view_students
from student import search_student
from student import delete_student

from result import calculate_result

from validation import valid_marks


while True:

    print("\n===== STUDENT MANAGEMENT SYSTEM =====")

    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Calculate Result")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")


    # ADD STUDENT
    if choice == "1":

        add_student()


    # VIEW STUDENTS
    elif choice == "2":

        view_students()


    # SEARCH STUDENT
    elif choice == "3":

        roll = input("Enter Roll Number: ")

        search_student(roll)


    # CALCULATE RESULT
    elif choice == "4":

        marks = []

        for i in range(5):

            while True:

                try:

                    mark = float(
                        input(f"Enter marks {i + 1}: ")
                    )

                    if valid_marks(mark):

                        marks.append(mark)

                        break

                    else:

                        print(
                            "Marks must be between 0 and 100."
                        )

                except ValueError:

                    print("Please enter a valid number.")


        total, percentage, grade = calculate_result(marks)

        print("\n===== RESULT =====")

        print("Total:", total)

        print("Percentage:", percentage)

        print("Grade:", grade)


    # DELETE STUDENT
    elif choice == "5":

        roll = input("Enter Roll Number: ")

        delete_student(roll)


    # EXIT
    elif choice == "6":

        print("Thank you!")

        break


    else:

        print("Invalid choice.")