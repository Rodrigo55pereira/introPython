# while = Enquanto
# Break = Para, brecar

resposta = input('Bora dá um rolê [s/n]??  ')

n = 1

while resposta != 's':
    resposta = input(f'Bora{"a" * n} [s/n]??  ')
    n = n + 1
    if 'chato' in resposta:
        break

print(f'Então, bora{"a" * n}!!!!')
