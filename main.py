import sympy as sp
from prettytable import PrettyTable # will we need that?
import newtons
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

inputText, xi, iterations = newtons.getInput()
xfirst = xi
funcY = []
funcX = []
dfuncY = []
dfuncX = []

# deriving the functions
x = sp.Symbol('x')
fx = eval(inputText, {'x': x, 'sin': sp.sin, 'cos': sp.cos, 'e': sp.E}) # log
fxDash = sp.diff(fx, x)

for i in range(iterations):
    y = sp.N(fx.subs(x, xi))
    yDash = sp.N(fxDash.subs(x, xi))
    roundedFX = "%.4f" % y
    roundedFXDash = "%.4f" % yDash
    funcY.append(y)

    funcX.append(xi)
    dfuncY.append([y, 0])

    # if roundedFX == '0.0000':
    #     print(f"achieved root with @ x = {xi} after {i+1} iterations")
    #     break
    # elif roundedFXDash == '0.0000':
    #     print(f"Newton's method cannot deal with flat spots, slope is 0 @ x = {xi} and iteration {i+1}")
    #     break
    # still need to handle runaway and cyclic

    # getting the new point
    xi = xi - (y / yDash)
    xi = round(xi, 4)
    dfuncX.append([funcX[i], xi])
    print(xi)


last_point = int(xi)

steps = abs(xfirst - last_point) + 4 # for seen range of the curve " 2 before the root and 2 after"

for i in range(int(steps) * 2 ):  # 2 for smoothing of the curve

    funcY.append(sp.N(fx.subs(x, (last_point-2)+(i/2)))) # y axis starting 2 points before the root and increment by 0.5 for smoother curve
    funcX.append((last_point-2)+(i/2)) # x axis


plot(funcX,funcY,dfuncX,dfuncY)






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