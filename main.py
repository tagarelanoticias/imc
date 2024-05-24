nomes = ['brasil', 'paraguai','uruguai','venezuela','chile','argentina']

nome = input('digite o nome a ser pesquisado: ')

indice = nomes.index(nome)

if nome in nomes:
    print(f'nome encontrado: {nome} no indice {indice}')
else:
    print(f'{nome} não encontrado na lista')