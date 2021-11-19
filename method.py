# inputs : equation function and 1 point
from sympy import Symbol, Derivative
import sympy as sym


def func(expr, x):
    return eval(expr)

def deriv(expr,point):
    x = sym.Symbol('x')
    
    deriv= Derivative(expr, x)
    derivVal = deriv.doit().subs({x:point})
    return derivVal

def newtonEq(input_expr,first_point):

    second_point = first_point - (func(input_expr, first_point) / deriv(input_expr, first_point))

    return second_point
    


input_expr = input('Enter an expression in x: ')
first_point = float(input('Enter the initial point: '))
iterations = int(input('Enter number of iterations: '))

for i in range(iterations):
    first_point = newtonEq(input_expr,first_point)
    print(f"\nIteration {iterations} \n second point = {first_point}")






