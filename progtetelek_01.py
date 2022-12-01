from random import randint

szamok:list[int] = []
for x in range(200):
    szamok.append(randint(10, 99))
print(szamok)

osszeg:int = 0
for szam in szamok:
    osszeg += szam
atlag:int = osszeg/len(szamok)
print(f'számok átlaga: {atlag}')

szamlalo:int = 0
for szam in szamok:
    if szam > atlag:
        szamlalo += 1
print(f'átlagon felüli számok száma: {szamlalo}')

szamlalo = 0
for szam in szamok:
    if szam % 10 == 0:
        szamlalo += 1
print(f'nullára végződő számok száma: {szamlalo}')

maxi:int = 0
for i in range(1, len(szamok)):
    if szamok[i] > szamok[maxi]:
        maxi = i
maxv:int = szamok[maxi]
print(f'a legnagyobb szám: {maxv}')
szamlalo = 0
for szam in szamok:
    if szam == maxv:
        szamlalo += 1
print(f'a {maxv} összesen {szamlalo}x szerepel a listában')

mini:int = 0
for i in range(1, len(szamok)):
    if szamok[i] < szamok[mini]:
        mini = i
minv:int = szamok[mini]
print(f'a legkisebb szám: {minv}')
szamlalo = 0
for szam in szamok:
    if szam == minv:
        szamlalo += 1
print(f'a {minv} összesen {szamlalo}x szerepel a listában')

ln0:int = -1
for szam in szamok:
    if ln0 == -1 and szam % 10 == 0:
        ln0 = szam
    elif szam % 10 == 0 and ln0 < szam:
        ln0 = szam
if ln0 != -1: print(f'legnagyobb 0ra végződő szám: {ln0}')
else: print(f'nincs 0ra végződő szám a listában')
if ln0 != -1:
    szamlalo = 0
    for szam in szamok:
        if szam == ln0:
            szamlalo += 1
    print(f'a {ln0} összesen {szamlalo}x szerepel a listában')

nullara_vegzodok:list[int] = []
for szam in szamok:
    if szam % 10 == 0:
        nullara_vegzodok.append(szam)
if len(nullara_vegzodok) != 0:
    print(f'összes 0ra végződő szám: {nullara_vegzodok}')
    maxi = 0
    for i in range(1, len(nullara_vegzodok)):
        if nullara_vegzodok[i] > nullara_vegzodok[maxi]:
            maxi = i
    print(f'legnagyobb 0-ra végződő szám: {nullara_vegzodok[maxi]}')

i:int = 0
while i < len(szamok) and szamok[i] % 15 != 0:
    i += 1
if i < len(szamok):
    print(f'van a számok közt 15 többszöröse, az első ilyen: {szamok[i]}')
else: print('nincs a listában 15 többszöröse.')