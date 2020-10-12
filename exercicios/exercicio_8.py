data = input('Insira a data de nascimento: ')

if '/' in data:
    dia, mes, ano = data.split('/')
    print(f'Você nasceu em {dia} do {mes} de {ano}')
else:
    print('Data não é valida, segue exemplo de data válida 00/00/0000')

