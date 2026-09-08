#1.Even or Odd
# num = int(input("Enter a number: "))

# if num % 2 == 0:
#     print("Even")
# else:
#     print("Odd")


#2.Positive, Negative or Zero
# num = int(input("Enter a number: "))

# if num > 0:
#     print("Positive")
# elif num < 0:
#     print("Negative")
# else:
#     print("Zero")


#3.Largest of Three Numbers
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))

# if a >= b and a >= c:
#     print("Largest =", a)
# elif b >= a and b >= c:
#     print("Largest =", b)
# else:
#     print("Largest =", c)

#4.leap year
# year = int(input("Enter year: "))

# if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
#     print("Leap Year")
# else:
#     print("Not a Leap Year")


#5.Student Grading System
# marks = int(input("Enter marks: "))

# if marks >= 90:
#     print("Grade A+")
# elif marks >= 75:
#     print("Grade A")
# elif marks >= 60:
#     print("Grade B")
# elif marks >= 40:
#     print("Grade C")
# else:
#     print("Fail")


#6.Voting Eligibility
# age = int(input("Enter your age: "))

# if age >= 18:
#     print("Eligible to Vote")
# else:
#     print("You have", 18 - age, "years left to vote")



#7.Discount Calculator
# bill = float(input("Enter bill amount: "))

# if bill > 1000:
#     discount = bill * 20 / 100
# elif bill >= 500:
#     discount = bill * 10 / 100
# else:
#     discount = 0

# final_amount = bill - discount

# print("Discount =", discount)
# print("Final Payable Amount =", final_amount)