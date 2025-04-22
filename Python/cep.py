import requests
import json

url = "https://viacep.com.br/ws/{}/json/"

def procurarCep(cep):
    resposta = requests.get(url.format(cep))
    try:
        dados = resposta.json()
        return dados['logradouro'], dados['bairro'], dados['localidade'], dados['uf']
    except ValueError:
        return "CEP inválido"
    
print(procurarCep(13199362)) # Digitar o CEP aqui dentro do "print" e consultar no console executando-o.