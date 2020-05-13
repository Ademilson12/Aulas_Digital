import requests
response = request.get('https://loja.com.br/frete/04856060/json/')
print(response.json())
#dados = response.json()
#print('A entrega deve ser feita para {}, RG: {}, CPF: {}, nascido em {}, residente no CEP {}, na cidade de {}'.format())
