"""
Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that
reads the same forwards and backwards.)

"""

string = input("Input any text: ")

text_list = list(string)
if text_list[:] == text_list[::-1]:
    print(string, "is a PALINDROME.")
else:
    print(string, "is not a PALINDROME.")
