import sympy as sp

# inits for later use
x = sp.Symbol('x')

# getting the input fx
inputText = input("Enter the fx: ")
fx = eval(inputText, {'x': x, 'sin': sp.sin, 'cos': sp.cos, 'e': sp.E})
fxDash = sp.diff(fx, x)

print(fx)
print(fxDash)