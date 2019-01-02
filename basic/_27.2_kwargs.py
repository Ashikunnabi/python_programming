# This function can take unlimited numbers of arguments by the help of **kwargs


def phone_book(**b):     # Traditionally it is written as def phone_book(**kwargs)
    print("Name \t Number")
    for person, number in b.items():
        print(person, "\t".expandtabs(4), number)


phone_book(X="018XXXXXXXX",
           Y="017XXXXXXXX",
           Z="016XXXXXXXX",)
