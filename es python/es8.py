n = input('scrivi n: ')

try:
    n = int(n)
except:
    print('non hai scritto un intero')
    exit()
    
if (n%2) == 1:
    print('bizzarro')
    
else:
    if 2 <= n <= 5:
        print('non bizzarro')
        
    elif 6 <= n <= 20:
        print('bizzarro')
        
    else:
        print('non bizzarro')