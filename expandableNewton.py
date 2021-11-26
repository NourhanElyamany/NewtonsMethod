import sympy as sp

# inits for later use
x = sp.Symbol('x')

# getting the input fx and cleaning it
inputText = input("Enter the fx: ")
inputText = inputText.replace('^', '**')

xk = int(input("Initial point of starting: "))
iterations = input("How many iterations do you need: ")


# deriving the functions
fx = eval(inputText, {'x': x, 'sin': sp.sin, 'cos': sp.cos, 'e': sp.E})
fxDash = sp.diff(fx, x)

print(fx)
print(fxDash)