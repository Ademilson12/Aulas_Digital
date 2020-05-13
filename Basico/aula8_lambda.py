"""
Função anonima
"""
contador_letras = lambda lista: [len(x) for x in lista]

lista_animais = ['Cachorro', 'Gato', 'Elefante']

print(contador_letras(lista_animais))

soma = lambda a,b: a + b
print(soma(5,5))

calculadora = {
    'soma': lambda a,b: a + b ,
    'subtracao': lambda a,b: a - b,
    'divisao': lambda a,b: a / b,
    'multiplicacao': lambda a,b: a * b
    
}

print(type(calculadora))
soma = calculadora['soma']
# soma = lambda a,b: a + b
# print(soma(5,5))
print(soma(5,5))