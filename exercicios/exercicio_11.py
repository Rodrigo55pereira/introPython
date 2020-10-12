""" palavra = input('Entre com o texto: ')

for letra in palavra:
    if 'a' == letra:
        print(letra)
        print('Rodrigo')
    elif 'e' == letra:
        print(letra)
        print('Rodrigo')
    elif 'i' == letra:
        print(letra)
        print('Rodrigo')
    elif 'o' == letra:
        print(letra)
        print('Rodrigo')
    elif 'u' == letra:
        print(letra)
        print('Rodrigo')
    else:
        print(letra)
"""

palavra = input('Entre com o texto: ')
vogais = 'aeiou'
for letra in palavra:
    if letra in vogais:
        print('Eduardo')
    else:
        print(letra)
