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
    

def plot(x,y ,z1, z2):

    plt.figure('Newton Graph')
    plt.ylabel('F(x)')
    plt.xlabel('X')
    plt.plot(x, y, label='F(x)')
    for i in range (4):
    
        tmp1 = z1[i]
        tmp2 = z2[i]
        plt.plot(tmp1, tmp2, color="red")
    #plt.plot(z1,z2, color="green")
    plt.legend(loc='upper right')
    plt.show()







input_expr = input('Enter an expression in x: ')
initial_point = float(input('Enter the initial point: '))
iterations = int(input('Enter number of iterations: '))
temp = initial_point

# Specify the Column Names while initializing the Table 
myTable = PrettyTable(["Iteration (I) ", "Xi", "F(Xi)", "F'(Xi)", "Xi+1", "Error"]) 

# arrays for x and y axis
y=[]
x=[]
z1=[[4,3] , [3,2.4375] , [2.4375,2.2130] , [2.2130,2.1756]]
z2=[[33,0] ,[9,0], [2.0369,0], [0.2561,0]]

for i in range(iterations):
    first_point = initial_point
    initial_point = round(newtonEq(input_expr,first_point),4)
    
    
    myTable.add_row([i, first_point, func(input_expr,first_point), deriv(input_expr, first_point), initial_point, abs(round(initial_point - first_point,4))])
    # print(f"\nIteration {iterations} \n second point = {first_point}")
print(myTable)

for i in range(16):
    y.append(func(input_expr,(temp-4+i)/2)) # f
    x.append((temp-4+i)/2) # x

print(x)
print(y)

#z1.append([3,4])
#z2.append([33,0])



# plot
plot(x,y,z1,z2)
