# What would have to be changed to make the code in fig3-5.py work for
# finding an approximation to the cube root of both negative and positive
# numbers? Hint: think about changing low to ensure that the answer lies
# within the region being searched.

x = float(input('Enter a number to find the approximate sqrt of: '))
pos_x = abs(x)
epsilon = 0.01
num_guesses, low = 0, 0
high = max(1, pos_x)
ans = (high + low)/2
while abs(ans**3 - pos_x) >= epsilon:
    print('low =', low, 'high =', high, 'ans =', ans)
    num_guesses += 1
    if ans**3 < pos_x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2
print('number of guesses =', num_guesses)
if x > 0:
    print(ans, 'is close to the square root of', pos_x)
else:
    print('-' + str(ans), 'is close to the square root of', x)
