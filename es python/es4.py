print('devi scrivere nome e cognome')

s1 = input()

pari = s1[::2]
dispari = s1[1::2][::-1]

s2 = ''
for i in range(len(s1)):
    if i % 2 == 0:
        s2 += pari[int(i/2)]
    else:
        s2 += dispari[int(i/2)]
print(s2)