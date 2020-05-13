"""
Entender o que são pacotes 
Aprender a instalar e utilizar pacotes
Aprender a fazer requisições http(chamada de APIs)
- O que são pacotes
- O que é o instalador de pacotes do Python(PIP)
- Como instalar o pacote no Python
- Como listar pacotes instalados no Python
- Como utilizar um pacote 
- Instalar nosso primeiro pacote(Request)
- Realizar uma requisição http com requests
"""
import requests


def retorna_cep(cep):
    response = requests.get(f'http://viacep.com.br/ws/{cep}/json/')    
    #print(response.status_code) # 200 OK, 400 Not found
    #print(response.text)
    #print(response.json())
    dados_cep = response.json()
    print(dados_cep['logradouro'])
    print(dados_cep['bairro'])
    return dados_cep

def retorna_pokemon(pokemon):
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon}/')
    #response1 = request.get('https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon))
    dados_pokemon = response.json()
    return dados_pokemon

def retorna_response(url):
    response = requests.get(url)
    return response.text

if __name__ == '__main__':
    #retorna_cep('04856060')
    #----------------------------------------
    #teste = input('Digite um pokemon:')
    #dados_pokemon = retorna_pokemon(teste)
    #print(dados_pokemon['sprites']['front_shiny'])
    #-----------------------------------------
    response = retorna_response('https://digitalinnovation.one/')
    print(response)
    
    

