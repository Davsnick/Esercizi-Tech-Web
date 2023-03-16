print('devi scrivere una stringa')

s1 = input()
print(s1)

#print(s1[:4:])
if s1[:4:] != 'Sono':
    s1 = 'Sono' + s1

print(s1)