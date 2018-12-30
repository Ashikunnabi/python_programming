print("12".zfill(7))
print("121236522265".count('2'))
print("121236522265".count('2', 7, 9))
print("asdfg".capitalize())
print("ASDFG".casefold())
print("asdf".upper())
print("This is Python".encode())
print("This is Python".endswith("python"))
print("This is \tPython".expandtabs(40))
print("This is Python".find('s', 0, 7))

print('-'*40)

dictionary = {
    'x': 5,
    'y': 6
}
print("x = {x}, y = {y}".format_map(dictionary))
print("y = {y}".format_map(dictionary))
print("x = {x}, y = {y}".format(**dictionary))
print("y = {y}".format(**dictionary))

print(':'*40)

print("This is Python".index('s', 0, 7))
print("This is Python".isalnum())
print("This is Python".isalpha())
print("This is Python".isdecimal())
print("This is Python".isidentifier())
print("This is Python".islower())
print("This is Python".isnumeric())
print("This is Python".isprintable())
print("This is Python".isspace())
print("This is Python".istitle())
print("This is Python".isupper())

print("-"*40)

s = ['Python', 'Java', 'HTML']
print(", ".join(s))


print("This is Python".lower())
print("It is Python".partition("is"))
print("This is Python".replace("Python", "Django"))

s = "This is Python"
print(s[::-1])


