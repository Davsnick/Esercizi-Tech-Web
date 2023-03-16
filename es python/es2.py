print('devi scrivere 3 numeri interi')

a = input('scrivi a: ')
b = input('scrivi b: ')
c = input('scrivi c: ')

try:
    a=int(a)
    b=int(b)
    c=int(c)
except:
    print('non hai inserito dei numeri')
    exit()

if a == b:
    #almeno 2 sono uguali
    if a == c:
        #tutti e 3 sono uguali
        print('a,b,c sono tutti uguali')
        print((2*a)**a)
    else:
        #solo 2 sono uguali: a e b
        print('a e b sono uguali')
        print((a+b)/c)
else:
    #a e b sono sicuramente diversi
    if a == c:
        #solo 2 sono uguali: a e c
        print('a e c sono uguali')
        print((a+c)/b)
    else:
        if b == c:
            #solo 2 sono uguali: b e c
            print('b e c sono uguali')
            print((b+c)/a)
        else:
            #sono tutti diversi
            print('sono tutti diversi')
            print(a+b+c)
        