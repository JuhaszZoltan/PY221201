szavak:list[str] = []

c:int = 0
szo:str = '_'
while c < 20 and len(szo) != 0:
    c += 1
    szo = input(f'{c}. szó: ')
    if len(szo) != 0: szavak.append(szo)