# # You can import modules
# import math
from math import ceil, floor, sqrt
print(ceil(3.7))   # => 4.0
print(floor(3.7))  # => 3.0
print(sqrt(16))  # => 4.0
# print(math.ceil(3.7))   # => 4.0
# print(math.floor(3.7))  # => 3.0
# print(math.sqrt(16))  # => 4.0
# 
# # You can get specific functions from a module
# from math import ceil, floor
# print(ceil(3.7))   # => 4.0
# print(floor(3.7))  # => 3.0
# 
# # You can import all functions from a module.
# # Warning: this is not recommended
# from math import *
# 
# # You can shorten module names
# import math as m
# math.sqrt(16) == m.sqrt(16)  # => True
# 
# # Python modules are just ordinary Python files. You
# # can write your own, and import them. The name of the
# # module is the same as the name of the file.
# 
# # You can find out which functions and attributes
# # are defined in a module.
# import math
# dir(math)

# import random
from random import randint, choice, random

dice_roll = randint(1, 6)
print(f'You rolled a {dice_roll}')

raffle = ['Jim', 'Jane', 'Steve', 'Phil']
winner = choice(raffle)
print(f'The winner is {winner}')

print(random())

# random.choice(seq)
# random.random()

import my_module

my_module.say_hello()