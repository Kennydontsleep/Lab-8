 n = int(input('Enter year to check if it is leap year.'))
if n % 4 == 0 and n%100 != 0:
    leap = 'True'
elif n % 100 == 0 and n%400==0:
    leap = 'True'
else:
    leap = 'False'

print('the entered year is,'+leap)
