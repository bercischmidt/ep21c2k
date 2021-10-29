print('1. feladat: Az adatok beolvasása.')

f = open('valaszok.txt', 'r')

adatok11 = []
valaszok = ''
x = f.readline()
x = x.strip()
valaszok += x
for sor in f:
    sor = sor.strip()
    sor = sor.split()
    adatok11.append(sor)

n = len(adatok11)

print('2. feladat: A versenyen', n, 'versenyző indult. ')

print('3. feladat: Kérem adja meg a versenyző azonosítóját!')

valt = input()
for val in adatok11:
    if val[0] == valt:
        print(val[1], '\t')
        valasz3 = val[1]

print('4. feladat: A helyes megoldás:')

valasz = valaszok
print(valasz)

valasz4 = ''
n4 = len(valaszok)
for i in range(n4):
    if valaszok[i] == valasz3[i]:
        valasz4 += '+'
    else:
        valasz4 += ' '

print('{0}\t'.format(valasz4))

print('5. feladat: Kérem adja meg a feladat sorszámát:')
n5 = int(input())
db5 = 0
for valasz5 in adatok11:
    if valasz5[1][n5] == valaszok[n5]:
        db5 += 1

print('A feladatra {0} fő, a versenyzők {1} %-a adott helyes választ.'.format(db5, round(db5/n*100, 2)))

print('6. feladat: A versenyzők pontszámának meghatározása.')



g = open('pontok.txt', 'w')
osszesp = []
for valasz6 in adatok11:
    pont6 = 0
    for i in range(14):
        if i <= 5 and valasz6[1][i] == valaszok[i]:
            pont6 += 3
        if 6 <= i <= 10 and valasz6[1][i] == valaszok[i]:
            pont6 += 4
        if 11 <= i <= 13 and valasz6[1][i] == valaszok[i]:
            pont6 += 5
        if i == 14 and valasz6[1][i] == valaszok[i]:
            pont6 += 6
    osszesp.append(pont6)
for i6 in range(len(adatok11)):
    ki6 = adatok11[i6][0] + ' ' + str(osszesp[i6]) + '\n'
    g.write(ki6)
g.close()

print('7. feladat: A verseny legjobbjai:')


pontok7 = []
for i in range(n):
    x = osszesp[i]
    y = adatok11[i][0]
    adat7 = [x, y]
    pontok7.append(adat7)
pont_rend = sorted(pontok7, reverse = True)
db = 1
i = 0
while db <= 3:
    print(db, '\b. díj', '(', '\b', pont_rend[i][0], 'pont):', pont_rend[i][1])
    while pont_rend[i+1][0] == pont_rend[i][0]:
        i += 1
        print(db, '\b. díj', '(', '\b', pont_rend[i][0], 'pont):', pont_rend[i][1])
    db += 1
    i += 1