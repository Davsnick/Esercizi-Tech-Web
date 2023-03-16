a = input('scrivi a: ')

print(a)
print(type(a))

try:
    a = int(a)
    print(type(a))
    b = a**2
    print(b)
except:
    print('a non numero')