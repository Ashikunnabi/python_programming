print("Welcome to the GPA calculator.")
print("Please enter all your letter grades, one per line.")
print("Enter a blank line to designate the end.")

points = {'A': 4.0,
          'B+': 3.7, 'B': 3.4, 'B-': 3.0,
          'C+': 2.7, 'C': 2.4, 'C-': 2.0,
          'D+': 1.7, 'D': 1.4, 'D-': 1.0,
          'F': 0.0}
num_courses = 0
total_points = 0
done = False

while not done:
    grade = input()
    if grade == '':
        done = True
    elif grade not in points:
        print("Unknown grade '{0}' being ignored.".format(grade))
    else:
        num_courses += 1
        total_points += points[grade]
if num_courses > 0:
    print("Your GPA is {0:.3}".format(total_points / num_courses))