class Test:
    """ Parent class """
    pass


class Single(Test):
    """ Child class of Parent class- Test """
    pass


class Multilevel(Single):
    """ Child class of Parent class- Single
            Test
              |
            Single
              |
            Multilevel
     """
    pass


class Single2(Test):
    """ Child class of Parent class- Test """
    pass


class Multiple(Multilevel, Single2):
    """ Child class of Parent classes- Multilevel, Single2 """
    pass


print(Multilevel.__doc__)
