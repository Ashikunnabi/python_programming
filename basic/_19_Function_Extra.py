def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        print(a, end=" ")
        a, b = b, a + b


def factorial(value):
    j = 1
    for i in range(1, (value + 1)):
        j *= i
    print(j)


def reverse(value):
    for i in range((len(value)), -1, -1):
        print(value[i:i + 1], end="")


def star(value):
    row = value + 1
    for i in range(1, row):
        for j in range(1, row):
            if i == 1 or i == (row - 1):
                if j == row // 2:
                    print("x ", end="")
                else:
                    print("  ", end="")
            elif i == row // 2:
                if j == row // 2:
                    print("  ", end="")
                else:
                    print("x ", end="")
            else:
                if j % 2 == 0:
                    print("x ", end="")
                else:
                    print("  ", end="")
        print()


if __name__ == "__main__":
    # fibonacci(100)
    # print()
    # factorial(5)
    # reverse("123456")
    # print()
    star(5)
