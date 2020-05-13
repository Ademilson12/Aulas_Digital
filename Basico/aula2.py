nota1 = float(input('Entre com a nota: '))
while nota1 > 10:
    nota1 = float(input('Nota invalida. Entre com a nota correta: '))
nota2 = float(input('Entre com a segunda nota: '))
while nota2 > 10:
    nota2 = float(input('Nota invalida. Entre com a nota correta: '))
nota3 = float(input('Entre com a terceira nota: '))
while nota3 > 10:
    nota3 = float(input('Nota invalida. Entre com a nota correta: '))
nota4 = float(input('Digite a quarta nota: '))
while nota4 > 10:
    nota4 = float(input('Nota invalida. Entre com a nota correta: '))

media = (nota1 + nota2 + nota3 + nota4) / 4
print(f'Media: {media}')


#a = int(input('Digite um número:'))

#div = 0

#for i in range(1, a+1):
#    resto = a % i
#    if resto == 0:
#        div += 1
        
#if div == 2:
#    print(f'Número {a} é primo')
#else:
#    print('Número não é primo')