empty_set = set()
engineers = set(['John', 'Jane', 'Jack', 'Janice'])
programmers = set(['Jack', 'Sam', 'Susan', 'Janice'])
managers = set(['Jane', 'Jack', 'Susan', 'Zack'])

employees = engineers | programmers | managers              # union
print('01. Employees:', employees)

engineering_management = engineers & managers               # intersection
print('02. Engineer and manager both at a time:', engineering_management)

full_time_management = managers - engineers - programmers   # difference
print('03. Full time management:', full_time_management)

engineers.add('Marvin')                                     # add element
print('04. Engineers:', engineers)

