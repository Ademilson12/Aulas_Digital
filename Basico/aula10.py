"""
Aprenda a manipular datas
Realizar conversao de texto para data e vice-versa
realizar soma e subtracao em datas
- Como recuperar a data atual(DATE)
- Como trabalhar com a data, alterando sua formatação
- Como gerar um horário(TIME)
- Retornar data e hora atual(DATETIME)
- Alterar formação do DATETIME
- Realizar soma e subtracao de datas com TIMEDELTA
"""

from datetime import date, time, datetime, timedelta

def trabalhando_date():
    data_atual = date.today()
    print(data_atual.strftime('%d/%m/%Y')) # Dia - número, m - Mês, - Y - Ano com 4 digitos # strftime - vira string
    print(data_atual.strftime('%A %B %Y')) # Dia - nome, m - Mês, Y - Ano com 4 digitos # strftime - vira string
    
def trabalhando_time():
    time_atual = time(hour=15, minute=10, second=30)
    print(time_atual)
    print(time_atual.strftime('%H:%M:%S')) # H - Hora, M - Minuto, S - segundo # strftime - vira string
    
def trabalhando_datetime():
    data_atual = datetime.now()
    print(data_atual)
    print(data_atual.strftime('%d/%m/%Y - %H:%M:%S')) # d - Dia número, m - Mês numero, Y - Ano numero # strftime - vira string
    print(data_atual.strftime('%c')) # c - Dia da semana nome, Mês nome, Dia numero, Hora:minuto:segundos, ano 4 digitos  # strftime - vira string
    tupla = ('Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sabado', 'Domingo')
    print(tupla[data_atual.weekday()])
    data_string = '01/01/2019 12:20:25'
    data_convertida = datetime.strptime(data_string, '%d/%m/%Y %H:%M:%S')
    print(data_convertida)
    nova_data = data_convertida - timedelta(days=365)
    print(nova_data)


if __name__ == '__main__':
    trabalhando_date()
    trabalhando_time()
    trabalhando_datetime()
    