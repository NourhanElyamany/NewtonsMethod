import sympy as sp

x = sp.Symbol('x')
inputText = input("Enter the fx: ")
expr = eval(inputText, {'x': x, 'sin': sp.sin, 'cos': sp.cos, 'e': sp.E})

print(expr)