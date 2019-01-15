class Circle:
    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        if self.__radius >= 0:
            area = 3.1459 * (self.__radius ** 2)
            print(area)
        else:
            raise ValueError("Value should not NEGATIVE.")


circle = Circle(5)
circle.area() 

# circle_negative = Circle(-5)              # Negative value is nor allowed
# circle_negative.area()
# print(circle_negative.__radius)           # __radius is a private variable
