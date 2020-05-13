"""
Personalizando excecao
"""
class Error(Exception):
    pass

class InputError(Error):
    def __init__(self, message):
        self.message = message

while True:
    try:
        nota1 = int(input('Entre com uma nota de 0 a 10: '))
        print(f'Nota: {nota1}')
        if nota1 > 10:
            raise InputError('Nota não pode ser maior que 10!')
        elif nota1 < 0:
            raise InputError('Nota não pode ser menor que 0!')
        break
    except ValueError as erro:
        print('Valor invalido, digite apenas número entre 0 e 10!')
    except InputError as error:
        print(error)

