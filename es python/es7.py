x = input('scrivi un numero')

try:
    x = int(x)
except:
    print('non hai scritto un numero, hai scirtto: ', x)
    exit()
    
r = x - 17
if x < 17:
    print(abs(r))
    