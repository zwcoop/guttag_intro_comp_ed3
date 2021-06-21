# What is the decimal equivalent of the binary number 10011?

binary_num = '10011'
ans = 0
n = 1

for i in binary_num[::-1]:
    ans = ans +(int(i)*(2**n))
    n += 1
print(ans)
