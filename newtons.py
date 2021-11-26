import matplotlib.pyplot as plt

def getInput():
    inputText = input("Enter the fx: ")
    inputText = inputText.replace('^', '**')

    xi = int(input("Initial point of starting: "))
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