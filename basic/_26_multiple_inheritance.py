""" A class can be derived from more than one base classes in Python. This is called multiple inheritance """


class Father:
    """ Here all the information about Parent class. """
        
    def father(self):
        name = "Mr. ABC"
        return name
        
        
class Mother:
    """ Here all the information about Parent class. """

    def mother(self):
        self.name = "Mrs. DEF"
        return name


class Son(Father, Mother):
    """ Here all the information about Child class. """

    def __init__(self):
        self.name = "ijk"


if __name__ == '__main__':
    student = Son()
    print('Teacher is asking student in school: ')
    print('Teacher: What is your name?')
    print('Student: My name is', student.name)
    print('Teacher: What is your father\'s name?')
    print('Student: My father\'s name is', student.father())
    print('Teacher: What is your mother\'s name?')
    print('Student: My mother\'s name is', student.father())
    
    
    
