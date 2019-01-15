"""
    Write a program that prompts a user for a String, counts the number of vowels, consonants and digits(0-9) contained
     in the string and prints their numbers of occurrence and the percentages with 2 decimal digits.

        Enter a String: testing12345
        Number of vowels: 2(16.67%)
        Number of consonants: 5(41.67%)
        Number of digits: 5(41.67%)
"""

user_input = input("Enter a String: ")
digit_count = 0
vowel_count = 0
consonant_count = 0

for value in user_input:
    if value.isdigit():
        digit_count += 1
    elif value == 'a' or value == 'e' or value == 'i' or value == 'o' or value == 'u' or \
            value == 'A' or value == "E" or value == "I" or value == "O" or value == "U":
        vowel_count += 1
    else:
        consonant_count += 1
print(f"Number of vowels: {vowel_count} (", round((100 * vowel_count) / len(user_input), 2), "%)")
print(f"Number of consonant: {consonant_count} (",  round((100 * consonant_count) / len(user_input), 2), "%)")
print(f"Number of digit: {digit_count} (",  round((100 * digit_count) / len(user_input), 2), "%)")

