import random as rd


def random_password():
    for i in range(0,10):
        print("--------password generator!--------""\n")
        numbers = str(rd.randrange(1, 100))
        letters = rd.choice('qwertyuiop[]asdfghjklzxcvbnm')
        special = rd.choice('!@#$%^&*()_+;[]./')
        password = numbers + letters + letters + special + special
        print(password)
random_password()
