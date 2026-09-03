import string_utils

print("\n===== STRING UTILITIES =====")

text = "madam"

print("Original:", text)

print("Reverse:", string_utils.reverse_string(text))

print("Vowels:", string_utils.count_vowels(text))

print("Palindrome:", string_utils.is_palindrome(text))

print("Words:", string_utils.count_words("Python is easy"))