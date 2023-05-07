from random import choice, shuffle
from file.symbols import *

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


def create(element: int, my_list: list):
    my_mass = []
    for num in range(element):
        elem = choice(my_list)
        my_mass.append(elem)
    return my_mass


create_letters = create(nr_letters, letters)
create_symb = create(nr_symbols, symbols)
create_num = create(nr_numbers, numbers)
password = create_letters + create_symb + create_num
shuffle(password)
password = "".join(password)
print(f"Your password is: {password}")
