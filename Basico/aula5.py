"""
Conjuntos
Manipulação de conjuntos 
Aplicabilidade de conjuntos 
- O é um conjunto
- Metodo de união
- Metodo de intersecçao
- Metodo de diferença
- Metodo de diferença simétrica
- Remoçao de duplicidade de listas utilizando conjuntos
"""
#print(type(conjunto)) # Set - Conjunto
# conjunto = {1,2,3}
# conjunto.add(4)
# conjunto.discard(4)
# print(conjunto)

conjunto_a = {1,2,3}
conjunto_b = {1,2,3,4,5}
conjunto1 = {1,2,3,4,5}
conjunto2 = {4,5,6,7}
conjunto_uniao = conjunto1.union(conjunto2) # Une os valores dos conjuntos
conjunto_interseccao = conjunto1.intersection(conjunto2) # Imprime o que tem de igual nos conjuntos
conjunto_diferenca = conjunto1.difference(conjunto2) # O que tem de diferente no conjunto 1 do 2
conjunto_diff_simetrica = conjunto1.symmetric_difference(conjunto2)
conjunto_subset = conjunto_a.issubset(conjunto_b) # conjunto a é um subconjunto de b
print(f'Uniao: {conjunto_uniao}')
print(f'Interseccao: {conjunto_interseccao}')
print(f'Diferenca: {conjunto_diferenca}')
print(f'Diferenca simetrica: {conjunto_diff_simetrica}')
print(f'Subconjunto: {conjunto_subset}') # Verdadeiro ou Falso