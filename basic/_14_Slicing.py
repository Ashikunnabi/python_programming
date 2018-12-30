lists = ['start', 1, 2, 3, 4, 5, 6, 7, 8, 9, 'end']

print(lists[:])
print(lists[0:5])
print(lists[6:8])
print(lists[:6])
print(lists[5:])
print(lists[-1])
print(lists[-6:-1])
print(lists[0:10:2])        # [starting_index : ending_index : increment]
print(lists[::-1])          # reverse showing

print("\nString Slicing:")

string = 'Python is a great language.'

print(string[:])
print(string[0:5])
print(string[6:8])
print(string[:6])
print(string[5:])
print(string[-1])
print(string[-6:-1])
print(string[0:10:2])        # [starting_index : ending_index : increment]
print(string[::-1])          # reverse showing


print('\nUsing Slice object')
pyString = 'Python'
# contains indices (-1, -2, -3)
# i.e. n, o and h
sObject = slice(-1, -4, -1)
print(pyString[sObject])
