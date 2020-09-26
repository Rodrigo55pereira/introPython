data = input('Insira a data de nascimento: ')

if '/' in data:
    nova_data = data.split('/')
    dia = nova_data[0]
    mes = nova_data[1]
    ano = nova_data[2]
    print(f'Você nasceu em {dia} do {mes} de {ano}')
else:
    print('Data não é valida, segue exemplo de data válida 00/00/0000')

