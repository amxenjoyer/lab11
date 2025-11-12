"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

# https://github.com/amxenjoyer/lab11.git
# Partner 1: Dimitri Svetahor
# Partner 2: Daniel

import math

def square_root(a):
    if a < 0:
        raise ValueError
    else:
        return math.sqrt(a)

def hypotenuse(a, b):
    math.hypot(a, b)

# First example
def add(a, b): 
    return a+b

def sub(a, b):
    return a-b
def mul(a, b):
    return a*b
def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    else:
        return b/a
def log(a, b):
    if a < 1 or b < 1:
        raise ValueError
    else:
        return math.log(b, a)
def exp(a, b):
    return a**b


