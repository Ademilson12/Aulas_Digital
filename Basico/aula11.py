"""
Aprender a utilizar tratamento de exceções
Entender a importância de se utilizar exceções
Aprender a customizar exceções
- Como lançar uma exceção genérica 
- Utilizar exceções específicas 
- Encadeamento de exceções
- Else e Finally
- Criação de exceção customizadas
"""

lista = [1,10]
try:
    arquivo = open('teste.txt', 'a')
    arquivo = open('teste.txt', 'r')
    texto = arquivo.read()
    divisao = 10/1
    print(divisao)
    numero = lista[2]
    print(numero)
    print('Fechando arquivo')
    arquivo.close()
except ZeroDivisionError as error:
    print('Não é possível dividir por 0')
except IndexError as error:
    print('Não é possivel acessar o index')
except BaseException as error: # Base de todos os erros
    print(f'Erro: {error}')
else:
    print('Executa quando não tem nenhuma exceção')
finally:
    print('Sempre executa')
    print('Fechando arquivo')
    arquivo.close()