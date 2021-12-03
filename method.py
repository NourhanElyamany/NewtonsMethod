from sympy import Symbol, Derivative, diff, sin, cos, E
import matplotlib.pyplot as plt
from string import ascii_letters
from helpers import cleanInput


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

    plt.figure('Newton Graph')
    plt.ylabel('F(x)')
    plt.xlabel('X')
    plt.plot(x, y, label='F(x)')

    # plotting the d(x) tangent
    for i in range (len(dx)): # to skip last point " as the function stopped "
        plt.plot(dx[i], dy[i], '--', color = "red")
  
    plt.legend(["F(x)" , "F'(x)"],loc='upper left')

def plotTable(tableData):
    table = plt.table(cellText=tableData, loc='center')
    table.set_fontsize(14)
    table.scale(1,4)
    plt.axis('off')

def start(input_expr, initial_point, iterations, errorGiven,tableD,graphD):
    plt.close('all')
    input_expr, initial_point, iterations, errorGiven = cleanInput(input_expr, initial_point, iterations, errorGiven)
    alphabets = ascii_letters.replace('x', '')
    if any(x in input_expr for x in alphabets):
        # ERROR
        print("Can't have any symbol other than x")
        return

    x = Symbol('x') #to define that from now on x is a symbol for the equation
    fx = eval(input_expr,{'x': x, 'sin': sin, 'cos': cos, 'e': E}) #turns that string into a function with understandable trig
    fxDash = diff(fx, x)

    if fxDash == 0 :
        # ERROR
        print("Can't proceed with Newton Method with a constant function")
        return

    tempFirst = initial_point

    # Specify the Column Names while initializing the Table 
    table_data = [
        ["Iteration (I) ", "Xi", "F(Xi)", "F'(Xi)", "Xi+1", "Error"],
    ]

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
        errorIt = round(initial_point - first_point,4)
        if errorIt >= errorGiven: #error of iterations compared to given error
            break
        
        table_data.append([i+1, "%.4f" %first_point,
                        "%.4f" %func(input_expr,first_point),
                        "%.4f" %deriv(input_expr, first_point),
                        "%.4f" %initial_point,
                        "%.4f" %abs(errorIt)]
        )

    last_point = int(initial_point)

    steps = abs(tempFirst - last_point) + 4 # for seen range of the curve " 2 before the root and 2 after"

    for i in range(int(steps) * 2 ):  # 2 for smoothing of the curve

        funcY.append(func(input_expr,(last_point-2)+(i/2))) # y axis starting 2 points before the root and increment by 0.5 for smoother curve
        funcX.append((last_point-2)+(i/2)) # x axis

    # plot & table
    if tableD:
        plotTable(table_data)
    if graphD:
        plotGraph(funcX,funcY,dfuncX,dfuncY)

    if graphD or tableD:
        plt.show()