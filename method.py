# inputs : equation function and 1 point
def func(expr, x):
    return eval(expr)

input_expr = input('Enter an expression in x: ')
val = 5
print(func(input_expr, val))