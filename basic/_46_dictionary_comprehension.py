dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

new_dict_key = {k*2: v for (k, v) in dict.items()}
print(new_dict_key)

new_dict_value = {k: v*3 for (k, v) in dict.items()}
print(new_dict_value)

## Using dictionary as a alternative of for loop
# dict = {}
# for i in range(10):
#     if i%2 == 0:
#         dict[i] = i**2
# print(dict)
## Alternatively

dict = {i: i**2 for i in range(10) if i%2==0}
print(dict)
