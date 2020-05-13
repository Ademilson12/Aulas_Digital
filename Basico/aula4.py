"""
Listas - Sempre vai estar em colchetes
Tuplas - Sempre vai estar em parenteses  - Não pode ser alterada
Aplicabilidade de listas e tuplas 
"""

lista = [1, 3, 5, 7]
lista_animais = ['Cachorro','Gato', 'Elefante']

if 'Lobo' in lista_animais:
    print('Existe um lobo na lista')
else:
    lista_animais.append('Lobo')
    print(lista_animais)

#lista_animais.pop() - Remove o ultimo elemento da lista
lista_animais.remove('Lobo')
print(lista_animais)

tupla = (1, 10, 12, 14)
print(tupla)
tupla.append(15)
print(tupla)

