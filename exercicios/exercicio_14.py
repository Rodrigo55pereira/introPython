n = int(input('Entre com o tamanho da lista: '))
lista = []
somatorio = 0
i = 0

while i < n:
    valor = int(input(f'Entre com o valor {i} da lista: '))
    lista.append(valor + somatorio)
    for number in lista:
        somatorio = somatorio + number
    i += 1

print(lista)

