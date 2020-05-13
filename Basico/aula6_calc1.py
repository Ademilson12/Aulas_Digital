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
    def __init__(self, a, b):
        self.a = a 
        self.b = b
    
    def soma(self): # Metodo
        return self.a + self.b

    def subtracao(self):
        return self.a - self.b

    def multiplicacao(self):
        return self.a * self.b

    def divisao(self):
        return self.a / self.b

calculadora = Calculadora(10,2)
print(calculadora.soma())
print(calculadora.subtracao())
print(calculadora.multiplicacao())
print(calculadora.divisao())
