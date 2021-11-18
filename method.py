# inputs : equation function and 1 point
from sympy import Symbol, Derivative
import sympy as sym


def func(expr, x):
    return eval(expr)

def deriv():
    
    deriv= Derivative(function, x)
    derivVal = deriv.doit().subs({x:4})
    return derivVal

    


input_expr = input('Enter an expression in x: ')
first_point = float(input('Enter the initial point: '))

# print(func(input_expr, val))



# x = sym.Symbol('x')
# function = input_expr
# derivitive = sym.diff(function,2)
# print(derivitive)



