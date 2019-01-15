def large_number_checker(value1, value2):
    large_number = str(value1) + " is large number." if value1 > value2 else str(value2) + " is large number."
    return large_number


if __name__ == '__main__':
    value1, value2 = map(int, input("Input 2 number seperated by comma(,): ").split(','))
    large_number = large_number_checker(value1, value2)
    print(large_number)
