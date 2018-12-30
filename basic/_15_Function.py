def function_name(a, b):
    print(a + b)


function_name(a=int(input('Input 1st number: ')), b=int(input('Input 2nd number: ')))


def addition(a, b):
    print('Addition of {} and {} is {}'.format(a, b, (a+b)))


def subtraction(a, b):
    print('Addition of {} and {} is {}'.format(a, b, (a-b)))


def multiplication(a, b):
    print('Addition of {} and {} is {}'.format(a, b, (a+b)))


def division(a, b):
    print('Addition of {} and {} is {}'.format(a, b, (a/b)))


def calculator():
    print('Input two number (separated by (,)): ')
    a, b = input().split(",")

    addition(int(a), int(b))
    subtraction(int(a), int(b))
    multiplication(int(a), int(b))
    division(int(a), int(b))


if __name__ == "__main__":
    calculator()

