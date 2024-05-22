import os
import time

# contador

contador = int(input('informe um numero inteiro:')) 
os.system('cls')

while contador >= 0:
    print(f'contagem regressiva:{contador}')
    time.sleep(1)
    os.system('cls')
    contador -= 1
