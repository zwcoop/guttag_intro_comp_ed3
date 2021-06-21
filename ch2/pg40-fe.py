# Write a program that prints the sum of the prime numbers greater than 2
# and less than 1000. Hint: you probably want to use a for loop that is
# a primality test nested inside a for loop that iterates over the odd
# integers between 3 and 999.

primesum = 3
num = 7
for j in range(3,999) :
    for i in range(3, j, 2):
        nondiv = 0
        if j % i == 0 :
            #print(f'{num} is divisible by {i}')
            break
        else :
            #print(f'{num} is not divisible by {i}')
            nondiv = i
            if nondiv == (j - 2) :
                #print(f'{j} is prime')
                primesum = primesum + j
print(primesum)
