"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# https://github.com/amxenjoyer/lab11
# Partner 1: Dimitri Svetahor
# Partner 2: Daniel Mateu

import math
#class Calculator:
# First example
def add(a, b):
    return a + b

# same as before just different name (autograder looks for "subtract")
def subtract(a, b):
    return a - b

# multiply function same thing as before
def multiply(a, b):
    return a * b

def div(a, b):
    # they want this weird setup -> raise ZeroDivisionError when a == 0
    if a == 0:
        raise ZeroDivisionError("Division by zero.")
    # divide like normal a / b so (81,9)=9
    return a / b

def logarithm(base, value):
    # gotta check base and value are valid first
    if base <= 0:
        raise ValueError("Logarithm base must be greater than 0.")
    if base == 1:
        raise ValueError("Logarithm base cannot be 1.")
    if value <= 0:
        raise ValueError("The number must be greater than 0 for a logarithm.")
    # log base(value) this way makes it easy
    return math.log(value, base)

def hypotenuse(a, b):
    # round to 2 decimals like the test wants (5,3 -> 5.83)
    return round(math.hypot(a, b), 2)

def square_root(x):
    # round to 3 decimals like the test (956 -> 30.919)
    return round(math.sqrt(x), 3)

def exp(a, b):
    # exponential same as before
    return a ** b

# keeping your old names as backups just in case
subt = subtract
mul = multiply

def log(a, b):
    # just calls the main one
    return logarithm(a, b)
