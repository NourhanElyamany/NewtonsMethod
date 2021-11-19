import matplotlib.pyplot as plt

def f(x):
    return x ** 6 - 5 * x - 2

def fprime(x):
    return 6 * x**5 - 5

guess = 3
x=list(range(1,7))
y=[]

for val in x:
    nextGuess = guess - f(guess) / fprime(guess)
    guess = nextGuess
    print(nextGuess)
    y.append(nextGuess)

plt.figure()
plt.plot(x, y)
plt.show()