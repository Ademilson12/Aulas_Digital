class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 5
        
    def power(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True
    
    def aumenta_canal(self):
        if self.ligada:
            self.canal += 1
        
    def diminui_canal(self):
        if self.ligada:
            self.canal -=1
            
if __name__ == '__main__':                
    tv = Televisao()
    print(tv.ligada)
    tv.power()
    print(tv.ligada)
    tv.power()
    print(tv.ligada)
    tv.aumenta_canal()
    print(f'Canal: {tv.canal}')
    tv.diminui_canal()
    print(f'Canal: {tv.canal}')