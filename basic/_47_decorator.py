__pname__    = 'Decorator'
__author__   = 'Md. Ashikun Nabi'
__email__    = 'ashikunnabituhin@gmail.com'


role='Teacher'
access_role = ['Teacher', 'Admin']

def decorator(function):
    def wrapper():
        if role in access_role:
            return function()
    return wrapper()

    
@decorator
def add_grade():
    student_xyz = input('Grade = ')
    print('Grade added successfully.')

    
    
if __name__=="__main__":
    print(f'{__pname__},{__author__},{__email__}')
    add_grade()
