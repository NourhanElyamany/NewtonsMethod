import matplotlib.pyplot as plt
import sympy as sp

def getInput():
    inputText = input("Enter the fx: ")
    inputText = inputText.replace('^', '**')

    xi = float(input("Initial point of starting: "))
    iterations = int(input("How many iterations do you need: "))

    return inputText, xi, iterations


def plotGraph(x,y ,dx, dy):

    plt.figure('Newton Graph')
    plt.ylabel('F(x)')
    plt.xlabel('X')
    plt.plot(x, y, label='F(x)')

    # plotting the d(x) tangent
    for i in range (iterations-1): # to skip last point " as the function stopped "
        plt.plot(dx[i], dy[i], color="red")
  
    plt.legend(["F(x)" , "F'(x)"],loc='upper left')
    plt.show()

def createFX(inputText, xi, iterations):
    x = sp.Symbol('x')
    fx = eval(inputText, {'x': x, 'sin': sp.sin, 'cos': sp.cos, 'e': sp.E}) # log
    fxDash = sp.diff(fx, x)

    for i in range(iterations):
    # substituting the values in the functions to get a numerical answer and rounding it
        y = sp.N(fx.subs(x, xi))
        yDash = sp.N(fxDash.subs(x, xi))