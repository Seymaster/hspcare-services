""" generates random numner to be used as booking ID """

from random import random
from random import randint
import math

def generate_random_number():
    r = random.randint(300, 900000)
    return r
print(generate_random_number())