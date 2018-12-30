# lambda is called annonimous function which has no name
# yeah it is possible in python to declare a function without name

addition = lambda a, b: a + b
print(addition(6, 6))

squares = list(map(lambda x: x**2, range(10)))
print(squares)
