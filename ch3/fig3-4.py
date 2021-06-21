# Prints an approximation to the square root of x. As opposed the the previous
# methods, this algo works with floats instead of ints and uses epsilon
# too determine a close enough solution. Because of the step sizes required
# this pushes the limit of exhaustive enumeration algos.

epsilon = 0.01
step = epsilon**2
num_guesses = 0
ans = 0.0

x = float(input('Enter an integer: '))
# 2nd condition is ans*ans not ans to detect 0<x<1
while abs(ans**2 - x) >= epsilon and ans*ans <= x:
    ans += step
    num_guesses += 1
print('number of guesses =', num_guesses)
if abs(ans**2 - x) >= epsilon:
    print('Failed on square root of', x)
else:
    print(ans, 'is close to the square root of', x)
