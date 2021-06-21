# Newton-Raphson Method for finding the square root of a number
# Finds x such that x**2 - k is within epsilon of 0

k = float(input('Enter number to find square root of: '))
epsilon = 0.01
guess = k/2

while abs(guess**2 - k) >= epsilon:
    guess = guess - (((guess**2) - k)/(2*guess))
print('Square root of', k, 'is about', guess)
