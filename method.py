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

    


input_expr = input('Enter an expression in x: ')
first_point = float(input('Enter the initial point: '))

print( f"The original function with substitution  {func(input_expr, first_point)}")
print(f"The derrivative function after substitution {deriv(input_expr, first_point)}")



# x = sym.Symbol('x')
# function = input_expr
# derivitive = sym.diff(function,2)
# print(derivitive)



