def soma(numero_1, numero_2):
    return numero_1 + numero_2


def media(lista_de_numeros):
    # sun soma, len tamanho
    return sum(lista_de_numeros) / len(lista_de_numeros)


def imprime_relatorio(nome, cpf, telefone):
    return f"""
        Relatório parcial
        
        {nome}, portador do cpf {cpf}, que usa o número {telefone}.

        Está oficialmente de férias.
        Ass. Direção
    """
