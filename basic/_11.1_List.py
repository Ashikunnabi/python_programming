from builtins import print

empty_list = []
triangle = [1, 5, 7]
rectangle = [2, 4, 8, 6]
various_type = [1, 'a', "asdfg"]

print('1. Triangle:', triangle)
print('2. Rectangle:', rectangle)

triangle_rectangle = triangle + rectangle
print('3. Triangle and Rectangle:', triangle_rectangle)

triangle_rectangle = triangle_rectangle + [0000]
print('4.', triangle_rectangle)

print()
print('5. Triangle =', triangle)
triangle.remove(5)
print('6. After removing 5, Triangle=', triangle)

triangle.append(6)
print('7. After adding 6 Triangle=', triangle)

triangle.reverse()
print('8. After Reversing, Triangle=', triangle)

triangle.sort()
print('9. After ascending sort, Triangle=', triangle)

triangle.sort(reverse=True)
print('10. After descending sort, Triangle=', triangle)

triangle.pop(2)
print('11. After removing/popping index 2, Triangle=', triangle)

triangle.insert(2, 55)
print('12. After inserting 55 in index 2, Triangle =', triangle)

triangle.clear()
print('13. Triangle =', triangle)

duplicate_value_list = [1, 2, 21, 5, 4, 2, 3, 8]
print('14. "1" is duplicating only', duplicate_value_list.count(1), 'time.')
print('15. "2" is duplicating only', duplicate_value_list.count(2), 'times.')

# Square numbers from 1 to 10 in a list
square = []

for i in range(1, 11):
    square.append(i**2)
print('16. Square number of 1 to 10 are', square)

























