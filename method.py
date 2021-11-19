# inputs : equation function and 1 point
from sympy import Symbol, Derivative
import sympy as sym
from prettytable import PrettyTable 
import matplotlib.pyplot as plt


def func(expr, x):
    return round(eval(expr),4)

def deriv(expr,point):
    x = sym.Symbol('x')
    
    deriv= Derivative(expr, x)
    derivVal = deriv.doit().subs({x:point})
    return round(derivVal,4)

def newtonEq(input_expr,initial_point):

    second_point = initial_point - (func(input_expr, initial_point) / deriv(input_expr, initial_point))

    return round(second_point,4)
    

def plot(x,y):

    plt.figure('Newton Graph')
    plt.ylabel('F(x)')
    plt.xlabel('Iterations')
    plt.plot(x, y, label='F(x)')
    plt.legend(loc='upper right')
    plt.show()







input_expr = input('Enter an expression in x: ')
initial_point = float(input('Enter the initial point: '))
iterations = int(input('Enter number of iterations: '))

# Specify the Column Names while initializing the Table 
myTable = PrettyTable(["Iteration (I) ", "Xi", "F(Xi)", "F'(Xi)", "Xi+1", "Error"]) 

# arrays for x and y axis
y=[]
x=[]

for i in range(iterations):
    first_point = initial_point
    initial_point = round(newtonEq(input_expr,first_point),4)
    y.append(func(input_expr,first_point))
    x.append(i)
    
    
    myTable.add_row([i, first_point, func(input_expr,first_point), deriv(input_expr, first_point), initial_point, abs(round(initial_point - first_point,4))])
    # print(f"\nIteration {iterations} \n second point = {first_point}")
print(myTable)



# plot
plot(x,y)

