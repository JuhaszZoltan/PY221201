forras = open('szoveges_01.txt', mode='r', encoding='utf-8')
cel = open('szoveges_02.txt', mode='w', encoding='utf-8')
for sor in forras: cel.write(f'{sor.upper()}')