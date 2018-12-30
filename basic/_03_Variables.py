integer = 5
long_integer = 42000000000000000000
float01 = 2.12345
float02 = 3.1415e-10

print("01| Float numbers are %s and %s" % (float01, float02))
print("02| Float numbers are {} and {}".format(float01, float02))
print(f"03| Integer numbers are {integer} and {long_integer}")
print("04| Integer numbers are", integer, "and", long_integer, ".")
print("05| Float numbers are " + str(float01) + " and " + str(float02))



is_bool = True
is_bool = False
print("06| ", is_bool)

complex_number01 = 5 + 3j
complex_number02 = 2 + 4J

print("07| ", complex_number01 - complex_number02)
