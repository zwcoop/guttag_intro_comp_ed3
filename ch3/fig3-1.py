# This program prints the integer cube root, if it exists, of an integer
# using exhaustive enumeration

x = int(input('Enter an integer: '))
ans = 0

while ans**3 < abs(x):
    # lines below explicitly tracks decrementing function
    #dec = abs(x) - ans**3
    #print('Decrementing f(): abs(x) - ans**3 = ', dec)
    ans = ans + 1
if ans**3 != abs(x):
    print(x, 'is not a perfect cube')
else:
    if x < 0:
        ans = -ans
    print('Cube root of', x, 'is', ans)
