a = 5

try:
    print(a/0)
except ZeroDivisionError:
    print(a/2)
