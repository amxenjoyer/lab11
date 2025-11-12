"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

# https://github.com/amxenjoyer/lab11.git
# Partner 1: Dimitri Svetahor
# Partner 2: Daniel Mateu

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
        raise ValueError("Division by zero.")
    return b / a
def log(a,b):
    if a <= 0:
        raise ValueError("Logarithm base 'a' must be greater than 0.")
    if a == 1:
        raise ValueError("Logarithm base 'a' cannot be 1.")
    if b<=0:
        raise ValueError("The number 'b' must be greater than 0 for a logarithm.")
    return math.log(a,b)
def exp(a,b):
    return a**b


