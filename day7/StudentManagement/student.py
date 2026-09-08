def add_student():

    roll = input("Enter Roll Number: ")

    name = input("Enter Name: ")

    course = input("Enter Course: ")

    with open("data.txt", "a") as file:

        file.write(f"{roll},{name},{course}\n")

    print("Student added successfully.")


def view_students():

    try:

        with open("data.txt", "r") as file:

            data = file.readlines()

        if len(data) == 0:
            print("No students found.")
            return

        print("\n===== STUDENT LIST =====")

        for line in data:

            data = line.strip().split(",")

            print(
                "Roll:",
                data[0],
                "| Name:",
                data[1],
                "| Course:",
                data[2]
            )

    except FileNotFoundError:

        print("No student data found.")


def search_student(roll):

    try:

        with open("data.txt", "r") as file:

            for line in file:

                data = line.strip().split(",")

                if data[0] == roll:

                    print("\nStudent Found")

                    print("Roll:", data[0])
                    print("Name:", data[1])
                    print("Course:", data[2])

                    return

        print("Student not found.")

    except FileNotFoundError:

        print("No student data found.")


def delete_student(roll):

    try:

        with open("data.txt", "r") as file:

            lines = file.readlines()

        found = False

        with open("data.txt", "w") as file:

            for line in lines:

                if line.startswith(roll + ","):

                    found = True

                else:

                    file.write(line)

        if found:

            print("Student deleted successfully.")

        else:

            print("Student not found.")

    except FileNotFoundError:

        print("No student data found.")