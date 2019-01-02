# This function can take unlimited numbers of arguments by the help of *args
# which works as tuple


def add(a, *b):     # Traditionally it is written as def add(a, *args)
    result = 0
    print("*b works like tuple: ", b)
    for value in b:
        result = result + value
    print(result+a)


add(5,6,1)