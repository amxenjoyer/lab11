"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

import math
#class Calculator:
# First example
def add(a, b): 
    return a + b
def subt(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    if a == 0:
        raise ValueError("Division by zero.")

    return b / a
    return b / a # raise zero division if a == 0
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





    # math.log(number, base) corresponds to log_base(number)
    # So, log_a(b) is math.log(b, a)
    return math.log(b, a)


def exp(a, b):
    """Returns a raised to the power of b (a^b)."""
    return a ** b

#this is for pushing tets 3
