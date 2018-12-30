number = int(input("Input a number:"))

if number == 0:
    print("{} is neither even nor odd.".format(number))

elif number % 2 == 0:
    print(number, "is an Even number.")

else:
    print(str(number) + " is an Odd number.")
