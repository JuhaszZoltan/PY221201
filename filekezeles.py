from random import randint, choice

filmek:list[str] = []
file = open(file='filmek.txt', encoding='utf-8')

for sor in file:
    filmek.append(sor.strip())

print(choice(filmek))