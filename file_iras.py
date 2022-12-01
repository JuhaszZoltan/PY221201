file = open('file.txt', mode='a', encoding='utf-8')

nev:str = input('hogy hívnak? ')

file.write(f'Hello {nev}!\n')