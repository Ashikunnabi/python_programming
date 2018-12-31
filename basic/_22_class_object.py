class Calculator:
    """ Calculator class used to do some simple arithmatic operation among two numbers. """

    def addition(self, value_one, value_two):
        """ Adding two numbers """
        value_one = int(value_one)
        value_two = int(value_two)
        return value_one + value_two

    def subtraction(self, value_one, value_two):
        """ Subtract two numbers """
        value_one = int(value_one)
        value_two = int(value_two)
        return value_one - value_two

    def multiplication(self, value_one, value_two):
        """ Multiply two numbers """
        value_one = int(value_one)
        value_two = int(value_two)
        return value_one * value_two

    def division(self, value_one, value_two):
        """ Divide two numbers """
        value_one = int(value_one)
        value_two = int(value_two)
        return value_one / value_two


def main():
    value_one, value_two = input("Inter two number (separated by SPACE): ").split(" ")
    calculator = Calculator()

    addition = calculator.addition(value_one, value_two)
    subtraction = calculator.subtraction(value_one, value_two)
    multiplication = calculator.multiplication(value_one, value_two)
    division = calculator.division(value_one, value_two)

    print(
        'Addition: {}, Subtraction: {}, Multiplication: {}, Division: {}'.format(addition, subtraction, multiplication,
                                                                                 division))


if __name__ == '__main__':
    main()
