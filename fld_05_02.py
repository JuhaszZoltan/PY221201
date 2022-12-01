nevek:list[str] = []

for sor in open("FORRAS\\nevsor.txt", encoding='UTF-8'):
    nevek.append(sor.strip())

m = open("m.txt", encoding='utf-8', mode='w')

for i in range(len(nevek)):
    if nevek[i][0] in 'Kk':
        print(f'{i+1}.: {nevek[i]}')
    elif nevek[i][0] in 'Mm':
        m.write(nevek[i]+'\n')