# Write code that asks the user to enter their birthday in the form
# mm/dd/yyyy, and then prints a string of the form
# 'You were born in the year yyyy.'

bday = input('Enter your birthday in the form mm/dd/yyyy: ')
byear = bday[-4:]
print(f'You were born in the year {byear}.')
