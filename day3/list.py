# # 1. Create a list of five fruits and print the complete list
# fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]
# print(fruits)


# # 2. Print the first and last item of a list
# fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]

# print("First item:", fruits[0])
# print("Last item:", fruits[-1])


# # 3. Change the second item in a list
# fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]

# fruits[1] = "Pineapple"

# print(fruits)


# # 4. Add a new item using append()
# fruits = ["Apple", "Banana", "Mango"]

# fruits.append("Orange")

# print(fruits)


# # 5. Add an item at a specific position using insert()
# fruits = ["Apple", "Banana", "Mango"]

# fruits.insert(1, "Orange")

# print(fruits)


# # 6. Remove a specific item using remove()
# fruits = ["Apple", "Banana", "Mango", "Orange"]

# fruits.remove("Banana")

# print(fruits)


# # 7. Remove the last item using pop()
# fruits = ["Apple", "Banana", "Mango", "Orange"]

# fruits.pop()

# print(fruits)


# # 8. Find the total number of items in a list
# fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]

# print("Total items:", len(fruits))


# # 9. Print every item in a list using a for loop
# fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]

# for fruit in fruits:
#     print(fruit)


# # 10. Check whether a specific item exists in a list
# fruits = ["Apple", "Banana", "Mango", "Orange"]

# item = input("Enter fruit name: ")

# if item in fruits:
#     print("Item exists in the list")
# else:
#     print("Item does not exist in the list")


# # 11. Create a list of student names and add a new student
# students = ["Rahul", "Priya", "Amit", "Sneha"]

# new_student = input("Enter new student name: ")

# students.append(new_student)

# print("Students:", students)


# # 12. Remove a student name from the student list
# students = ["Rahul", "Priya", "Amit", "Sneha"]

# student = input("Enter student name to remove: ")

# if student in students:
#     students.remove(student)
#     print("Student removed")
# else:
#     print("Student not found")

# print("Students:", students)


# # 13. Create a list of numbers and print only the even numbers
# numbers = [10, 15, 20, 25, 30, 35, 40]

# for number in numbers:
#     if number % 2 == 0:
#         print(number)


# # 14. Create a list of numbers and find their sum using a loop
# numbers = [10, 20, 30, 40, 50]

# sum = 0

# for number in numbers:
#     sum += number

# print("Sum =", sum)


# # 15. Find the largest number without using max()
# numbers = [10, 25, 5, 40, 15]

# largest = numbers[0]

# for number in numbers:
#     if number > largest:
#         largest = number

# print("Largest number =", largest)


# # 16. Find the smallest number without using min()
# numbers = [10, 25, 5, 40, 15]

# smallest = numbers[0]

# for number in numbers:
#     if number < smallest:
#         smallest = number

# print("Smallest number =", smallest)


# # 17. Count how many even and odd numbers are present in a list
# numbers = [10, 15, 20, 25, 30, 35, 40]

# even_count = 0
# odd_count = 0

# for number in numbers:
#     if number % 2 == 0:
#         even_count += 1
#     else:
#         odd_count += 1

# print("Even numbers:", even_count)
# print("Odd numbers:", odd_count)


# # 18. Create an empty list and take five names from the user using a loop
# names = []

# for i in range(5):
#     name = input("Enter name: ")
#     names.append(name)

# print("Names:", names)


# # 19. Shopping list where the user can add, view and remove items
# shopping_list = []

# while True:
#     print("\nShopping List")
#     print("1. Add Item")
#     print("2. View Items")
#     print("3. Remove Item")
#     print("0. Exit")

#     choice = int(input("Enter your choice: "))

#     if choice == 1:
#         item = input("Enter item: ")
#         shopping_list.append(item)
#         print("Item added")

#     elif choice == 2:
#         print("Shopping List:", shopping_list)

#     elif choice == 3:
#         item = input("Enter item to remove: ")

#         if item in shopping_list:
#             shopping_list.remove(item)
#             print("Item removed")
#         else:
#             print("Item not found")

#     elif choice == 0:
#         print("Program ended")
#         break

#     else:
#         print("Invalid choice")


# 20. Simple student list management program
students = []

while True:
    print("\nStudent Management")
    print("1. Add Student")
    print("2. View Students")
    print("3. Remove Student")
    print("0. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter student name: ")
        students.append(name)
        print("Student added")

    elif choice == 2:
        print("Students:", students)

    elif choice == 3:
        name = input("Enter student name to remove: ")

        if name in students:
            students.remove(name)
            print("Student removed")
        else:
            print("Student not found")

    elif choice == 0:
        print("Program ended")
        break

    else:
        print("Invalid choice")