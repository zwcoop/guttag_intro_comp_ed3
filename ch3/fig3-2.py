# Tests if an int >2 is a prime number. If not, it prints the snallest divisor

x = int(input('Enter an integer greater than 2: '))
smallest_divisor = None

for guess in range(2, x):
    if x % guess == 0:
        smallest_divisor = guess
        break
if smallest_divisor != None:
    print('Smallest divisor of', x, 'is', smallest_divisor)
else:
    print(x, 'is a prime number')
