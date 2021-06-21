# Write a program that asks the user to enter an integer and prints
# two integers, root and pwr, such that 1 < pwr < 6 and root**pwr is
# equal to the integer entered by the user. If no such pair exists,
# it should print a message to that effect.

inp = int(input('Enter an integer: '))
pwr = None
root = None

for guess1 in range(inp):
    for guess2 in range(1,6):
        if guess1**guess2 == inp:
            root = guess1
            pwr = guess2
            break
if pwr != None:
    print(inp, '=', root, 'raised to the power of', pwr)
else:
    print('No pair exists such that 1<pwr<6 and root**pwr = ', inp)
