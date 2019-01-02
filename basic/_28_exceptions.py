a = 0
b = 5

try:
    print(b / a)

except ZeroDivisionError as e:
    print("Number can't be divided by zero.", e)
