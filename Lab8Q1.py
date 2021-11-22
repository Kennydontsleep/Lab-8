def equ(x, y):
    return len(x) == len(y)

x = input ("enter first string :")
y = input("enter second string :")
print('length of', x, ' is equal to length of' ,y, 'is', equ(x, y))