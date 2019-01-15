print("Enter 0 to end.")
print("Input numbers: ")

sum = 0

while True:
    number = int(input())

    if number == 0:
        break
    else:
        sum += number

print("Sum =", sum)
