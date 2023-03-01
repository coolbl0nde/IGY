from random import randint
from utilities import *

numbers = []
for i in range(1, 15):
    numbers.append(randint(1, 50))

print_hello()
print(calculation(3, 5, "mult"))
print(get_even_numbers(numbers))
