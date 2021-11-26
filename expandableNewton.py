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

