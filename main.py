import sympy as sp
from prettytable import PrettyTable # will we need that?
import newtons


inputText, xi, iterations = newtons.getInput()

# deriving the functions
x = sp.Symbol('x')
fx = eval(inputText, {'x': x, 'sin': sp.sin, 'cos': sp.cos, 'e': sp.E})
fxDash = sp.diff(fx, x)

for i in range(iterations):
    # substituting the values in the functions to get a numerical answer and rounding it
    fxAns = sp.N(fx.subs(x, xi))
    fxDashAns = sp.N(fxDash.subs(x, xi))
    roundedFX = "%.4f" % fxAns
    roundedFXDash = "%.4f" % fxDashAns

    if roundedFX == '0.0000':
        print(f"achieved root with @ x = {xi} after {i+1} iterations")
        break
    elif roundedFXDash == '0.0000':
        print(f"Newton's method cannot deal with flat spots, slope is 0 @ x = {xi} and iteration {i+1}")
        break
    # still need to handle runaway and cyclic

    # getting the new point
    xi = xi - (fxAns / fxDashAns)
    xi = round(xi, 4)

    print(xi)












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