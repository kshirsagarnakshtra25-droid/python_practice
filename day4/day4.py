
# ============================================================
# PYTHON LISTS - PRACTICE & PROBLEM SOLVING
# Q1 to Q20
# ============================================================


# ============================================================
# Q1. List Creation & Element Insertion
# ============================================================

print("\n========== Q1 ==========")

numbers = []

numbers.append(10)
numbers.append(20)
numbers.append(30)
numbers.insert(1, 15)
numbers.extend([40, 50])

print("Final List:", numbers)


# ============================================================
# Q2. Element Removal & Retrieval
# ============================================================

print("\n========== Q2 ==========")

items = ["Python", "Java", "C++", "JavaScript", "Ruby"]

items.remove("C++")
last_item = items.pop()

print("Modified List:", items)
print("Last Item:", last_item)


# ============================================================
# Q3. Element Frequency & Index Lookup
# ============================================================

print("\n========== Q3 ==========")

scores = [85, 92, 75, 92, 88, 92, 70]

count_92 = scores.count(92)
index_88 = scores.index(88)

print("Count of 92:", count_92)
print("Index of 88:", index_88)


# ============================================================
# Q4. Sorting & Reversing
# ============================================================

print("\n========== Q4 ==========")

marks = [45, 89, 12, 67, 95, 34]

marks.sort()
print("Ascending:", marks)

marks.reverse()
print("Descending:", marks)


# ============================================================
# Q5. List Slicing Challenge
# ============================================================

print("\n========== Q5 ==========")

arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print("First 5 elements:", arr[:5])
print("Last 3 elements:", arr[-3:])
print("Every second element from index 1 to 8:", arr[1:9:2])
print("Reverse order:", arr[::-1])


# ============================================================
# Q6. Sum and Average of List Elements
# ============================================================

print("\n========== Q6 ==========")

numbers = []

for i in range(5):
    num = int(input("Enter number " + str(i + 1) + ": "))
    numbers.append(num)

total = 0

for num in numbers:
    total = total + num

average = total / len(numbers)

print("Numbers:", numbers)
print("Sum:", total)
print("Average:", average)


# ============================================================
# Q7. Find Largest and Smallest Number
# ============================================================

print("\n========== Q7 ==========")


def find_min_max(numbers):
    maximum = numbers[0]
    minimum = numbers[0]

    for num in numbers:
        if num > maximum:
            maximum = num

        if num < minimum:
            minimum = num

    return maximum, minimum


numbers = [34, 12, 89, 5, 67]

maximum, minimum = find_min_max(numbers)

print("Max =", maximum)
print("Min =", minimum)


# ============================================================
# Q8. Remove Duplicates (Preserve Order)
# ============================================================

print("\n========== Q8 ==========")

numbers = [1, 3, 2, 3, 4, 1, 5, 2]

unique_list = []

for num in numbers:
    if num not in unique_list:
        unique_list.append(num)

print("Unique List:", unique_list)


# ============================================================
# Q9. Separate Even and Odd Numbers
# ============================================================

print("\n========== Q9 ==========")

numbers = [10, 15, 22, 33, 40, 55, 60]

even_list = []
odd_list = []

for num in numbers:
    if num % 2 == 0:
        even_list.append(num)
    else:
        odd_list.append(num)

print("Even List:", even_list)
print("Odd List:", odd_list)


# ============================================================
# Q10. Second Largest Element
# ============================================================

print("\n========== Q10 ==========")

numbers = [10, 45, 20, 99, 80, 99]

largest = float("-inf")
second_largest = float("-inf")

for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

print("Second Largest:", second_largest)


# ============================================================
# Q11. List Comprehension - Square Odds
# ============================================================

print("\n========== Q11 ==========")

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

result = [num ** 2 for num in nums if num % 2 != 0]

print("Square of Odd Numbers:", result)


# ============================================================
# Q12. Rotate List Elements Left by K Positions
# ============================================================

print("\n========== Q12 ==========")


def rotate_left(lst, k):
    k = k % len(lst)
    return lst[k:] + lst[:k]


lst = [1, 2, 3, 4, 5]
k = 2

result = rotate_left(lst, k)

print("Rotated List:", result)


# ============================================================
# Q13. Merge Two Sorted Lists
# ============================================================

print("\n========== Q13 ==========")

list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8, 10]

merged = []

i = 0
j = 0

while i < len(list1) and j < len(list2):

    if list1[i] < list2[j]:
        merged.append(list1[i])
        i += 1
    else:
        merged.append(list2[j])
        j += 1

while i < len(list1):
    merged.append(list1[i])
    i += 1

while j < len(list2):
    merged.append(list2[j])
    j += 1

print("Merged List:", merged)


# ============================================================
# Q14. Flatten a Nested List
# ============================================================

print("\n========== Q14 ==========")


def flatten(nested_list):
    result = []

    for item in nested_list:

        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)

    return result


nested_list = [1, [2, 3], [4, [5, 6]], 7]

print("Flattened List:", flatten(nested_list))


# ============================================================
# Q15. Pair Sum Target
# ============================================================

print("\n========== Q15 ==========")


def find_pairs(nums, target):
    pairs = []

    for i in range(len(nums)):

        for j in range(i + 1, len(nums)):

            if nums[i] + nums[j] == target:

                pair = (nums[i], nums[j])

                if pair not in pairs:
                    pairs.append(pair)

    return pairs


nums = [2, 4, 3, 5, 7, 8, 9]
target = 7

print("Pairs:", find_pairs(nums, target))


# ============================================================
# Q16. Longest Consecutive Subsequence
# ============================================================

print("\n========== Q16 ==========")


def longest_consecutive(nums):
    numbers = set(nums)
    longest = 0

    for num in numbers:

        if num - 1 not in numbers:

            current = num
            length = 1

            while current + 1 in numbers:
                current += 1
                length += 1

            if length > longest:
                longest = length

    return longest


numbers = [100, 4, 200, 1, 3, 2]

print("Longest Consecutive Length:", longest_consecutive(numbers))


# ============================================================
# Q17. Group Anagrams
# ============================================================

print("\n========== Q17 ==========")

words = ["eat", "tea", "tan", "ate", "nat", "bat"]

groups = {}

for word in words:

    key = "".join(sorted(word))

    if key not in groups:
        groups[key] = []

    groups[key].append(word)

result = list(groups.values())

print("Grouped Anagrams:", result)


# ============================================================
# Q18. Shallow Copy vs Reference
# ============================================================

print("\n========== Q18 ==========")

a = [1, 2, [3, 4]]

b = a.copy()

b[0] = 99
b[2][0] = 77

print("a:", a)
print("b:", b)


# ============================================================
# Q19. Debugging - Remove Negative Numbers
# ============================================================

print("\n========== Q19 ==========")

numbers = [-5, -2, 3, -4, -1, 6, 8]

numbers = [num for num in numbers if num >= 0]

print("After Removing Negative Numbers:", numbers)


# ============================================================
# Q20. Matrix Transposition
# ============================================================

print("\n========== Q20 ==========")

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transpose = [
    [matrix[j][i] for j in range(len(matrix))]
    for i in range(len(matrix[0]))
]

print("Transposed Matrix:", transpose)


# ============================================================
# END OF PROGRAM
# ============================================================

print("\n========== ALL 20 QUESTIONS COMPLETED ==========")

