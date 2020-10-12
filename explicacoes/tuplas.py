
minha_tupla = ('Eduardo', 27, '91294652', 'R. dos Bobos', 0)

nome, idade, *coisas_que_nao_quero = minha_tupla

# tupla invertida
nome, idade = idade, nome

def minha_func():
    return 1, 2, 3


