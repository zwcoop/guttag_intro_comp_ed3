# Reimplements the algo from fig2-7.py but using a for loop to calculate
# the squaring of an integers

x = -12
ans = 0
for num_iterations in range(abs(x)) :
    ans = ans + abs(x)
print(f'{x}*{x} = {ans}')
