# More efficient version of code in fig3-2.py.
# Tests if an int >2 is a prime number. If not, it prints the snallest divisor
# First tests if divisible by 2. If not, does not test the remaining even #s

x = int(input('Enter an intger greater than 2: '))
smallest_divisor = None

if x % 2 == 0:
    smallest_divisor = 2
else:
    for guess in range(3, x, 2):
        if x % guess == 0:
            smallest_divisor = guess
            break
if smallest_divisor != None:
    print('Smallest divisor of ', x, 'is', smallest_divisor)
else:
    print(x, 'is a prime number.')
