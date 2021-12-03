authers ="""Nourhan Elyamany
Mohamed Osama
Karim Kohel
Amr Mekki
Omar Tamer
Youssef Saed
Aly Khaled"""

def cleanInput(expr, xi, iterations, errorGiven):
    expr = expr.replace("^", "**")
    expr = expr.replace("X", 'x')
    xi = float(xi)
    iterations = int(iterations)

    if not errorGiven:
        errorGiven=0
    errorGiven = float(errorGiven)
    return expr, xi, iterations, errorGiven