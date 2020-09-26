texto = input('Digite um texto: ')
vogais = ''
tem_vogais = False

if 'a' in texto or 'e' in texto or 'i' in texto or 'o' in texto or 'u' in texto:
    print('Sim o texto tem vogais!')
else:
    print('Texto não tem vogais!')

if 'a' in texto:
    vogais = vogais + 'a'
if 'e' in texto:
    vogais = vogais + ' e'
if 'i' in texto:
    vogais = vogais + ' i'
if 'o' in texto:
    vogais = vogais + ' o'
if 'u' in texto:
    vogais = vogais + ' u'

if vogais != '':
    vogais = vogais.replace(' ', ',')
    print(f'As vogais do texto são: {vogais}')

if ' ' in texto:
    print('O texto é um frase!')
else:
    print('O texto não é uma frase!')
