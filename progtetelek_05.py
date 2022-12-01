szavak:list[str] = []

for n in range(20):
    szo:str = input(f'{n+1}. szó: ')
    if len(szo) == 0: break
    szavak.append(szo)

maxi:int = 0
for i in range(1, len(szavak)):
    if len(szavak[i]) > len(szavak[maxi]):
        maxi = i
print(f'a leghosszabb szó: {szavak[maxi]}')

osszhossz:int = 0
for szo in szavak:
    osszhossz += len(szo)
print(f'szaval átlagos hossza: {osszhossz/len(szavak)}')