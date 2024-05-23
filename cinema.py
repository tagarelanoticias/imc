nome = input('qual seu nome?')
idade = input('qual a sua idade?')

print('1 - falcão negro - sala 1 - 12')
print('2 - tocaia - sala 2 - 14')
print('3 - um sonho de liberdade -sala 3 - 16')
print('4 - dumbo - sala 4 - l')
print('5 - cinquenta tons de cinza - sala 5 - 18')

sala = input('qual sala deseja?')

match sala:
    case 1:
        if idade > 12:
            print('esta liberado bom filme')
        else:
            print('idade não permitida ')
    case 2:
        if idade > 14:
            print('entrada permitida bom filme')
        else:
            print('idade não permitida')
    case 3:
        if idade > 16:
            print('entrada permitida bom filme')
    case 4:
        print('entrada permitida bom filme ')
    case 5:
        if idade > 18:
            print('entrada permitida bom filme')
        else:
            print(' entrada não permitida')
     