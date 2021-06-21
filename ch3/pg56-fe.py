# What would code in fig3-5.py do if x = -25?
# The answer is that it enters an infinite loop

# Option 1: If we don't want to deal with imaginary numbers we can simply not
# accept negative inputs
"""x = float(input('Enter a number to find the approximate sqrt of: '))
if x < 0:
    print('Must enter positive number.')
else:
    epsilon = 0.01
    num_guesses, low = 0, 0
    #high = max(1, x)
    high = max(1, x)
    ans = (high + low)/2
    while abs(ans**2 - x) >= epsilon:
        print('low =', low, 'high =', high, 'ans =', ans)
        num_guesses += 1
        if ans**2 < x:
            low = ans
        else:
            high = ans
        ans = (high + low)/2
    print('number of guesses =', num_guesses)
    print(ans, 'is close to the square root of', x)"""

# Option 2: Find the sqrt of the positive number and then give the
# result concatenated with i
x = float(input('Enter a number to find the approximate sqrt of: '))
pos_x = abs(x)
epsilon = 0.01
num_guesses, low = 0, 0
high = max(1, pos_x)
ans = (high + low)/2
while abs(ans**2 - pos_x) >= epsilon:
    print('low =', low, 'high =', high, 'ans =', ans)
    num_guesses += 1
    if ans**2 < pos_x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2
print('number of guesses =', num_guesses)
if x > 0:
    print(ans, 'is close to the square root of', pos_x)
else:
    print(str(ans) + 'i', 'is close to the square root of', x)
