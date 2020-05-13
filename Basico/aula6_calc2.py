"""
Metodos
Funcoes
Classes
- O que são metodos e funções
- Como declarar métodos e funções
- Vantagens de se utilizar métodos e funções
- Como implementar class
- Vantagens de se utilizar classes
"""

class Calculadora: # Classe em python      
    #def __init__(self):
    #    pass
        
    
    def soma(self,a,b): # Metodo
        return a + b

    def subtracao(self,a,b):
        return a - b

    def multiplicacao(self,a,b):
        return a * b

    def divisao(self,a,b):
        return a / b

calculadora = Calculadora()
print(calculadora.soma(10, 2))
print(calculadora.subtracao(10,2))
print(calculadora.multiplicacao(10,5))
print(calculadora.divisao(10,2))