# inputs : equation function and 1 point
from sympy import Symbol, Derivative
import sympy as sym
from prettytable import PrettyTable 

def func(expr, x):
    return eval(expr)

def deriv(expr,point):
    x = sym.Symbol('x')
    
    deriv= Derivative(expr, x)
    derivVal = deriv.doit().subs({x:point})
    return derivVal

def newtonEq(input_expr,initial_point):

    second_point = initial_point - (func(input_expr, initial_point) / deriv(input_expr, initial_point))

    return second_point
    


input_expr = input('Enter an expression in x: ')
initial_point = float(input('Enter the initial point: '))
iterations = int(input('Enter number of iterations: '))

# Specify the Column Names while initializing the Table 
myTable = PrettyTable(["Iteration (I) ", "Xi", "F(Xi)", "F'(Xi)", "Xi+1", "Error"]) 

for i in range(iterations):
    first_point = initial_point
    initial_point = newtonEq(input_expr,first_point)
    myTable.add_row([i, first_point, func(input_expr,first_point), deriv(input_expr, first_point), initial_point, initial_point - first_point])
    # print(f"\nIteration {iterations} \n second point = {first_point}")


  
  

  
print(myTable)




