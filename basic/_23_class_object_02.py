class Calculator:
    """ Calculator class used to do some simple arithmetic operation among two numbers. """

    def __init__(self, value_one, value_two):
        """ Initial method that always used to refer objects. """
        self.value_one = int(value_one)
        self.value_two = int(value_two)

    def addition(self):
        """ Adding two numbers """
        return self.value_one + self.value_two

    def subtraction(self):
        """ Subtract two numbers """
        return self.value_one - self.value_two

    def multiplication(self):
        """ Multiply two numbers """
        return self.value_one * self.value_two

    def division(self):
        """ Divide two numbers """
        return self.value_one / self.value_two


def main():
    value_one, value_two = input("Inter two number (separated by SPACE): ").split(" ")
    calculator = Calculator(value_one, value_two)

    addition = calculator.addition()
    subtraction = calculator.subtraction()
    multiplication = calculator.multiplication()
    division = calculator.division()

    print(
        'Addition: {}, Subtraction: {}, Multiplication: {}, Division: {}'.format(addition, subtraction, multiplication,
                                                                                 division))


if __name__ == '__main__':
    main()
