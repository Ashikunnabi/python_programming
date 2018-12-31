class Gmail:
    """ Here all the information about Parent class. """
        
    def __init__(self):
        print("Welcome to Gmail. You are able to send email.")
        
        
class Login(Gmail):
    """ Here all the information about Child class. """

    def __init__(self):
        self.username = "person@gmail.com"
        self.password = "abc456xyz"
            
    def authenticaton(self, username, password): 
        if (self.username == username and self.password == password):
            print("Login Successfull...")
            super().__init__()
        else:
            print("Login failed.")
    
    

class Person(Login):
    """ Here all the information about Child class. """

    def __init__(self, username, password):
        super().__init__()   # You have to call __init__ as because you are not creating object of Login class 
        super().authenticaton(username, password)


if __name__ == '__main__':
    person = Person("person@gmail.com", "abc456xyz")
    
    
    
