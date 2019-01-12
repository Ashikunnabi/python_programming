"""
 This is the most preferable method to work with file
    'with' keyword is used in this system
 no need to use finally step as because 'with' helps to close file automatically.
 """
with open('02.new_method.txt', 'w') as file:
    file.write('New file method introduced.')

with open('02.new_method.txt', 'a', encoding='UTF-8') as file: #Default encoding is UTF-8
    file.write('Write another language except English\n')
    file.write('Bengali: আলজাজিরা নিউজপেপার')
    
