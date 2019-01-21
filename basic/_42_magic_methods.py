"""

   +     __add__(self, other)         Add
   -     __sub__(self, other)         Sub
   *     __mul__(self, other)         Mul
   /     __div__(self, other)         Div
   %     __floordiv__(self, other)    Floor
   **    __mod__(self, other)         Mod
   <<    __pow__(self, other)         Power
   >>    __lshift__(self, other)      Left Shift
   &     __rshift__(self, other)      Right Shift
   //    __and__(self, other)         AND
   ^     __xor__(self, other)         XOR
   |     __or__(self, other)          OR

"""


class Calculation:
    def __init__(self, *args):
        if len(args) == 0:
            self.numbers = (0, 0)
        else:
            self.numbers = args

    def __add__(self, other):
        add = [x + y for x, y in zip(self.numbers, other.numbers)]
        return add

    def __sub__(self, other):
        sub = tuple(x - y for x, y in zip(self.numbers, other.numbers))
        return sub

    def __mul__(self, other):
        mul = [x * y for x, y in zip(self.numbers, other.numbers)]
        return mul


obj1 = Calculation(2, 3)
obj2 = Calculation(2, 3)

print("Addition          :", (obj1 + obj2))
print("Subtraction       :", (obj1 - obj2))
print("Multiplication    :", (obj1 * obj2))
