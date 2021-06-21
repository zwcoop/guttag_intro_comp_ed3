# This program compares the number of guesses needed to find an approximate
# square roots of a number using 1) exhaustive enumeation 2) bisection
# 3) Newton-Raphson Method

x = float(input('Enter an integer: '))

# Exhaustive Enumeration
epsilon = 0.01
step = epsilon**2
num_guesses = 0
ans = 0.0

# 2nd condition is ans*ans not ans to detect 0<x<1
while abs(ans**2 - x) >= epsilon and ans*ans <= x:
    ans += step
    num_guesses += 1
if abs(ans**2 - x) >= epsilon:
    print('Failed on square root of', x)
else:
    print('Enumeration approx: ', ans)
print('Enumeration guesses =', num_guesses)

# Bisection method
epsilon = 0.01
num_guesses, low = 0, 0
high = max(1, x)
ans = (high + low)/2
while abs(ans**2 - x) >= epsilon:
    #print('low =', low, 'high =', high, 'ans =', ans)
    num_guesses += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2
print('Bisection approx: ', ans)
print('Bisection guesses =', num_guesses)

# Newton-Raphson method
epsilon = 0.01
guess = x/2
num_guesses = 0

while abs(guess**2 - x) >= epsilon:
    num_guesses += 1
    guess = guess - (((guess**2) - x)/(2*guess))
print('Newton-Raphson approx: ', guess)
print('Newton-Raphson guesses =', num_guesses)
