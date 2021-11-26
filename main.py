# inputs : equation function and 1 point
import sympy as sp
from prettytable import PrettyTable 
import matplotlib.pyplot as plt
    
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

# inits for later use
x = sp.Symbol('x')

# getting the input fx and cleaning it
inputText = input("Enter the fx: ")
inputText = inputText.replace('^', '**')

xk = int(input("Initial point of starting: "))
iterations = int(input("How many iterations do you need: "))


# deriving the functions
fx = eval(inputText, {'x': x, 'sin': sp.sin, 'cos': sp.cos, 'e': sp.E})
fxDash = sp.diff(fx, x)

for i in range(iterations):
    # substituting the values in the functions to get a numerical answer and rounding it
    fxAns = sp.N(fx.subs(x, xk))
    fxDashAns = sp.N(fxDash.subs(x, xk))
    roundedFX = "%.4f" % fxAns
    roundedFXDash = "%.4f" % fxDashAns

    if roundedFX == '0.0000':
        print(f"achieved root with @ x = {xk} after {i+1} iterations")
        break
    elif roundedFXDash == '0.0000':
        print(f"Newton's method cannot deal with flat spots, slope is 0 @ x = {xk} and iteration {i+1}")
        break
    # still need to handle runaway and cyclic

    # getting the new point
    xk = xk - (fxAns / fxDashAns)
    xk = round(xk, 4)

    print(xk)

# # Specify the Column Names while initializing the Table 
# myTable = PrettyTable(["Iteration (I) ", "Xi", "F(Xi)", "F'(Xi)", "Xi+1", "Error"]) 

# # arrays for x and y axis of function(x) and d(x)
# funcY = []
# funcX = []
# dfuncY = []
# dfuncX = []




# for i in range(iterations):
#     first_point = initial_point
#     initial_point = round(newtonEq(input_expr,first_point),4)
#     dfuncY.append([func(input_expr,first_point),0])
#     dfuncX.append([first_point,initial_point])
    
    
#     myTable.add_row([i, first_point, func(input_expr,first_point), deriv(input_expr, first_point), initial_point, abs(round(initial_point - first_point,4))])
   
# print(myTable)

# last_point = int(initial_point)

# steps = abs(tempFirst - last_point) + 4 # for seen range of the curve " 2 before the root and 2 after"

# for i in range(int(steps) * 2 ):  # 2 for smoothing of the curve

#     funcY.append(func(input_expr,(last_point-2)+(i/2))) # y axis starting 2 points before the root and increment by 0.5 for smoother curve
#     funcX.append((last_point-2)+(i/2)) # x axis


# # plot
# plot(funcX,funcY,dfuncX,dfuncY)
