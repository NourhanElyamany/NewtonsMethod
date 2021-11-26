import sympy as sp

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

print(fx)
print(fxDash)

for _ in range(iterations):
    # substituting the values in the functions to get a numerical answer and rounding it
    fxAns = sp.N(fx.subs(x, xk))
    fxDashAns = sp.N(fxDash.subs(x, xk))

    # getting the new point
    xk = xk - (fxAns / fxDashAns)
    xk = round(xk, 4)

    print(xk)

