# PYTHON PROGRAMS

# TUPLE, SET AND DICTIONARY

# ============================================================

# TUPLE

# ============================================================

# Q1. Create a tuple containing five numbers.

# numbers = (10, 20, 30, 40, 50)

# print("Tuple:", numbers)

# ============================================================

# Q2. Print the first and last element.

# numbers = (10, 20, 30, 40, 50)

# print("First element:", numbers[0])
# print("Last element:", numbers[-1])

# # ============================================================

# # Q3. Find the length of a tuple.

# numbers = (10, 20, 70, 60, 50)

# print("Length of tuple:", len(numbers))

# # ============================================================

# # Q4. Count a particular value.

# numbers = (10, 20, 10, 30, 10, 40, 50)

# print("Number of times 10 occurs:", numbers.count(10))

# # ============================================================

# # Q5. Find the index of a value.

# numbers = (10, 20, 30, 40, 50)

# print("Index of 30:", numbers.index(30))

# # ============================================================

# # Q6. Unpack a tuple into variables.

# student = ("Bhumika", 21, "MCA")

# name, age, course = student

# print("Name:", name)
# print("Age:", age)
# print("Course:", course)

# # ============================================================

# # Q7. Create a student information tuple.

# student = ("Bhumika", 21, "MCA", "Pune", 85)

# print("Student Information:")
# print("Name:", student[0])
# print("Age:", student[1])
# print("Course:", student[2])
# print("City:", student[3])
# print("Marks:", student[4])

# # ============================================================

# # SET

# # ============================================================

# # Q1. Create a set of five numbers.

# numbers = {10, 20, 30, 40, 50}

# print("Set:", numbers)

# # ============================================================

# # Q2. Add an element to a set.

# numbers = {10, 20, 30, 40, 50}

# numbers.add(60)

# print("Set after adding 60:", numbers)

# # ============================================================

# # Q3. Remove an element.

# numbers = {10, 20, 30, 40, 50}

# numbers.remove(30)

# print("Set after removing 30:", numbers)

# # ============================================================

# # Q4. Remove duplicate values from a list using a set.

# numbers = [10, 20, 10, 30, 20, 40, 30, 50]

# unique_numbers = set(numbers)

# print("Original list:", numbers)
# print("After removing duplicates:", unique_numbers)

# # ============================================================

# # Q5. Find union of two sets.

# set1 = {10, 20, 30, 40}
# set2 = {30, 40, 50, 60}

# union = set1.union(set2)

# print("Union:", union)

# # ============================================================

# # Q6. Find intersection of two sets.

# set1 = {10, 20, 30, 40}
# set2 = {30, 40, 50, 60}

# intersection = set1.intersection(set2)

# print("Intersection:", intersection)

# # ============================================================

# # Q7. Find difference between two sets.

# set1 = {10, 20, 30, 40}
# set2 = {30, 40, 50, 60}

# difference = set1.difference(set2)

# print("Difference:", difference)

# # ============================================================

# # DICTIONARY

# # ============================================================

# # Q1. Create a student dictionary.

# student = {
# "name": "Bhumika",
# "age": 21,
# "course": "MCA",
# "city": "Pune"
# }

# print("Student Dictionary:", student)

# # ============================================================

# # Q2. Access values using keys.

# student = {
# "name": "Bhumika",
# "age": 21,
# "course": "MCA"
# }

# print("Name:", student["name"])
# print("Age:", student["age"])
# print("Course:", student["course"])

# # ============================================================

# # Q3. Add a new key.

# student = {
# "name": "Bhumika",
# "age": 21,
# "course": "MCA"
# }

# student["city"] = "Pune"

# print("After adding city:", student)

# # ============================================================

# # Q4. Update an existing value.

# student = {
# "name": "Bhumika",
# "age": 21,
# "course": "MCA"
# }

# student["age"] = 22

# print("After updating age:", student)

# # ============================================================

# # Q5. Delete a key.

student = {
"name": "Bhumika",
"age": 21,
"course": "MCA",
"city": "Pune"
}

del student["city"]

print("After deleting city:", student)

# # ============================================================

# # Q6. Use keys(), values() and items().

# student = {
# "name": "Bhumika",
# "age": 21,
# "course": "MCA"
# }

# print("Keys:", student.keys())
# print("Values:", student.values())
# print("Items:", student.items())

# # ============================================================

# # Q7. Check whether a key exists.

# student = {
# "name": "Bhumika",
# "age": 21,
# "course": "MCA"
# }

# if "name" in student:
#   print("Name key exists.")
# else:
  
#   print("Name key does not exist.")

# # ============================================================

# # Q8. Create a dictionary containing student marks.

# marks = {
# "Maths": 85,
# "English": 80,
# "Science": 90,
# "Computer": 95
# }

# print("Student Marks:", marks)

# # ============================================================

# # Q9. Create a list of dictionaries for five students.

# students = [
# {"name": "Bhumika", "age": 21, "marks": 85},
# {"name": "Rahul", "age": 22, "marks": 90},
# {"name": "Priya", "age": 21, "marks": 88},
# {"name": "Amit", "age": 23, "marks": 78},
# {"name": "Sneha", "age": 22, "marks": 92}
# ]

# print("Five Students:")

# for student in students:
#   print(student)
