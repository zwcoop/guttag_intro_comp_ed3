# Figure 2-7 Squaring an integer the hard way
# The abs(x) is essential for the code not to enter an infinite loop

x = int(input('Enter a positive or negative integer: '))
ans = 0
num_iterations = 0
while (num_iterations < abs(x)):
    ans = ans + abs(x)
    num_iterations = num_iterations + 1
print(f'{x}*{x} = {ans}')
