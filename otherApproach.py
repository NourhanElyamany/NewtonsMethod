# inputs : equation function and 1 point
from turtle import color
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
    

def plot(x,y ,dx, dy):

    plt.figure('Newton Graph')
    plt.ylabel('F(x)')
    plt.xlabel('X')
    plt.plot(x, y, label='F(x)')

    # plotting the d(x) tangent
    for i in range (iterations-1): # to skip last point " as the function stopped "
        plt.plot(dx[i], dy[i], color="red")
  
    plt.legend(["F(x)" , "F'(x)"],loc='upper left')
    plt.show()


input_expr = input('Enter an expression in x: ')
initial_point = float(input('Enter the initial point: '))
iterations = int(input('Enter number of iterations: '))
tempFirst = initial_point

# Specify the Column Names while initializing the Table 
myTable = PrettyTable(["Iteration (I) ", "Xi", "F(Xi)", "F'(Xi)", "Xi+1", "Error"]) 

# arrays for x and y axis of function(x) and d(x)
funcY = []
funcX = []
dfuncY = []
dfuncX = []




for i in range(iterations):
    first_point = initial_point
    initial_point = round(newtonEq(input_expr,first_point),4)
    dfuncY.append([func(input_expr,first_point),0])
    dfuncX.append([first_point,initial_point])
    
    
    myTable.add_row([i, first_point, func(input_expr,first_point), deriv(input_expr, first_point), initial_point, abs(round(initial_point - first_point,4))])
   
print(myTable)

last_point = int(initial_point)

steps = abs(tempFirst - last_point) + 4 # for seen range of the curve " 2 before the root and 2 after"

for i in range(int(steps) * 2 ):  # 2 for smoothing of the curve

    funcY.append(func(input_expr,(last_point-2)+(i/2))) # y axis starting 2 points before the root and increment by 0.5 for smoother curve
    funcX.append((last_point-2)+(i/2)) # x axis


# plot
plot(funcX,funcY,dfuncX,dfuncY)