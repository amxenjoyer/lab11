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
    return math.hypot(a, b)

# First example
def add(a, b): 
    return a+b

def subtract(a, b):
    return a-b
def mul(a, b):
    return a*b
def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Division by zero.")
    return b / a
def logarithm(a,b):
    if a <= 0:
        raise ValueError("Logarithm base 'a' must be greater than 0.")
    if a == 1:
        raise ValueError("Logarithm base 'a' cannot be 1.")
    if b<=0:
        raise ValueError("The number 'b' must be greater than 0 for a logarithm.")
    return math.log(b, a)
def exp(a,b):
    return a**b


