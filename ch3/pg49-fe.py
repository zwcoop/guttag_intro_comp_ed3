# Change the code in fig3-2.py so that it returns the largest
# rather than the smallest divisor.
# Hint: if y*z = x and y is the smallest divisor of x, z is the
# largest divisor.

x = int(input('Enter an integer greater than 2: '))
smallest_divisor = None
largest_divisor = None

for guess in range(2, x):
    if x % guess == 0:
        smallest_divisor = guess
        largest_divisor = x//guess
        break
if largest_divisor != None:
    print('Largest divisor of', x, 'is', largest_divisor)
else:
    print(x, 'is a prime number')
