""" Single inheritance made by only two Class. One will be Parent and another will be Child. """


class Parent:
    """ Here all the information about Parent class. """

    def __init__(self, b):
        self.a = 5
        self.b = b


class Child(Parent):
    """ Here all the information about Child class. """

    def __init__(self):
        super().__init__(6)
        print(self.a)
        print(self.b)


if __name__ == '__main__':
    child = Child()
