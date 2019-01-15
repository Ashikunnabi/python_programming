import random

__author__ =" Md. Ashikunnabi "
__copyright__ = " Protected, take permission to use. "


chars = 'as{dfg;hj&kl?poi[uy`tr\ew(qz%xcv~bnm.QA-ZW#SXC+DE=RFV:BG!TYH}NM/JUI<KL_OP147]85$236@9*|\'"> ,^)'

passwords = int(input("Number of passwords? "))
password_length = int(input("Password length: "))
password = ''

for i in range(passwords):
    for j in range(password_length):
        password += random.choice(chars)
    print(password)
    password = ''
