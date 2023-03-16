print('devi scrivere 2 numeri interi')

a = input('scrivi a: ')
b = input('scrivi b: ')

try:
    a=int(a)
    b=int(b)
except:
    print("l'input deve essere un numero")
    exit()

if (a == 5 and b == 5) or (a+b == 5) or (a-b == 5) or (b-a == 5):
    print(True)
else:
    print(False)