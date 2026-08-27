# # 11. Print numbers divisible by 5 between 1 and 100
# for i in range(1, 101):
#     if i % 5 == 0:
#         print(i)


# # 12. Use a while loop to print numbers from 1 to 20
# i = 1

# while i <= 20:
#     print(i)
#     i += 1


# # 13. Use a while loop to print even numbers from 2 to 20
# i = 2

# while i <= 20:
#     print(i)
#     i += 2


# # 14. Print numbers and stop when the number becomes 5 using break
# for i in range(1, 11):
#     if i == 5:
#         break
#     print(i)


# # 15. Print numbers from 1 to 10 but skip 5 using continue
# for i in range(1, 11):
#     if i == 5:
#         continue
#     print(i)


# # 16. Find the sum of the first N natural numbers
# n = int(input("Enter N: "))

# sum = 0

# for i in range(1, n + 1):
#     sum += i

# print("Sum =", sum)


# # 17. Calculate power without using **
# base = int(input("Enter base: "))
# power = int(input("Enter power: "))

# result = 1

# for i in range(power):
#     result *= base

# print("Answer =", result)


# # 18. Print the first 10 multiples of 3
# for i in range(1, 11):
#     print(3 * i)


# # 19. Count numbers between 1 and 100 divisible by both 2 and 5
# count = 0

# for i in range(1, 101):
#     if i % 2 == 0 and i % 5 == 0:
#         count += 1

# print("Count =", count)


# 20. Simple menu loop until user enters 0
while True:
    print("\nMenu")
    print("1. Hello")
    print("2. Python")
    print("0. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Hello!")
    elif choice == 2:
        print("You selected Python")
    elif choice == 0:
        print("Program ended")
        break
    else:
        print("Invalid choice")