cidades = ['brasília','taguatinga','gama','sobradinho']

indice = int(input('informe uma posição a ser deletada'))

if indice>0:
    indice -= 1
else:
    indice = ''


try:
    del(cidades[indice])
except:
    print('não possível deletar!')