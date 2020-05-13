class Carro:
    def __init__(self):
        self.motor = 'desligado'
        self.movimento = False

    def ligar(self):
        self.motor = 'ligado'
    
    def acelerar(self):
        if self.motor == 'ligado':
            self.movimento = True

    def carro_em_movimento(self):
        return self.movimento

carro = Carro()
carro.acelerar()
carro_em_movimento = carro.carro_em_movimento()
print(carro_em_movimento)