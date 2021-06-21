# Finger exercise: Write a program that asks the user to input 10
# integers, and then prints the largest odd number that was entered.
# If no odd number was entered, it should print a message to that effect.

oddlst = []
evenlst = []
i = 0
while (i < 10) :
    num = int(input('Enter an integer: '))
    if num % 2 != 0 :
        oddlst = oddlst + [num]
        i+=1
    else :
        evenlst = evenlst + [num]
        i+=1
if oddlst == [] :
    print('You did not enter any odd integers')
else :
    print(f'The max odd entered was {max(oddlst)}')
