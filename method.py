from os import error
from tkinter import DoubleVar
from tokenize import Double
from sympy import Symbol, Derivative, diff, sin, cos, E
import matplotlib.pyplot as plt
from string import ascii_letters
from helpers import cleanInput
from random import random

def func(expr, x):
    return round(eval(expr,{'x': x, 'sin': sin, 'cos': cos, 'e': E}),4)

def deriv(expr,point):
    x = Symbol('x')
    
    deriv= Derivative(expr, x)
    derivVal = deriv.doit().subs({x:point})
    return round(derivVal,4)

def newtonEq(input_expr,initial_point):

    second_point = initial_point - (func(input_expr, initial_point) / deriv(input_expr, initial_point))

    return round(second_point,4)
    

def plotGraph(x,y ,dx, dy):

    fig = plt.figure('Newton Graph')
    plt.ylabel('F(x)')
    plt.xlabel('X')
    plt.plot(x, y, label='F(x)')
    plt.grid('on')

    # plotting the d(x) tangent
    for i in range (len(dx)): # to skip last point " as the function stopped "
        plt.plot(dx[i], dy[i], '--', color = "red")
  
    plt.legend(["F(x)" , "F'(x)"],loc='upper left')
    return fig

def plotTable(tableData):
    fig = plt.figure('Newton Table')
    table = plt.table(cellText=tableData,
                    loc='center',
                    colLabels=["Iteration (I) ", "Xi", "F(Xi)", "F'(Xi)", "Xi+1", "Error"],
                    colColours=["skyblue"] * 10, 
                )
    table.set_fontsize(14)
    table.scale(1,2)
    plt.axis('off')
    return fig

def start(input_expr, initial_point, iterations, errorGiven,tableD,graphD, holder, messagebox):
    
    try:
        initial_point = float(initial_point)
    except:
        messagebox.showinfo("error","starting point must be number !")
        return

    if not iterations:
        iterations=13

    try:
        iterations = int(iterations)
    except:
        messagebox.showinfo("error","iterations must be a real number !")
        return

    if not errorGiven:
        errorGiven=0

    try:
        errorGiven = float(errorGiven)
    except:
        messagebox.showinfo("error","error must be a number !")
        return    

    plt.close('all')
    input_expr = cleanInput(input_expr)


    # alphabets = ascii_letters.replace(('x', ''))
    # if any(x in input_expr for x in alphabets):
    #     # ERROR
    #     messagebox.showinfo("error","Can't have any symbol other than x")
    #     #print("Can't have any symbol other than x")
    #     return

    figureName =  str("%.4f"%random()).replace('0.', '')
    x = Symbol('x') #to define that from now on x is a symbol for the equation
    fx = eval(input_expr,{'x': x, 'sin': sin, 'cos': cos, 'e': E}) #turns that string into a function with understandable trig
    fxDash = diff(fx, x)
    if fxDash == 0 :
        # ERROR
        messagebox.showinfo("error","Can't proceed with Newton Method with a constant function 'inflection point'")
        #print("Can't proceed with Newton Method with a constant function")
        return

    tempFirst = initial_point

    # Specify the Column Names while initializing the Table 
    table_data = []
    # arrays for x and y axis of function(x) and d(x)
    funcY = []
    funcX = []
    dfuncY = []
    dfuncX = []


    for i in range(iterations):
        first_point = initial_point
        initial_point = round(newtonEq(input_expr,first_point),4) # two times round ?!!!
        dfuncY.append([func(input_expr,first_point),0])
        dfuncX.append([first_point,initial_point])
        errorIt = abs(round(initial_point - first_point,4))
        
        table_data.append([i+1, "%.4f" %first_point,
                        "%.4f" %func(input_expr,first_point),
                        "%.4f" %deriv(input_expr, first_point),
                        "%.4f" %initial_point,
                        "%.4f" %abs(errorIt)]
        )
        if errorIt <= errorGiven: #error of iterations compared to given error
            break

    last_point = int(initial_point)

    steps = abs(tempFirst - last_point) + 4 # for seen range of the curve " 2 before the root and 2 after"

    for i in range(int(steps) * 2 ):  # 2 for smoothing of the curve

        funcY.append(func(input_expr,(last_point-2)+(i/2))) # y axis starting 2 points before the root and increment by 0.5 for smoother curve
        funcX.append((last_point-2)+(i/2)) # x axis

    # plot & table
    if tableD:
        table = plotTable(table_data)
        holder.setTable(table, 'Newton-table-'+figureName+'.png')
    if graphD:
        graph = plotGraph(funcX,funcY,dfuncX,dfuncY)
        holder.setPlot(graph, 'Newton-plot-'+figureName+'.png')

    if graphD or tableD:
        plt.show()

    if not graphD and not tableD:
        messagebox.showwarning("Warning", "you should select output type!!!")    