from xml import dom
import requests
import json

def consulta_email(primeiro_nome, ultimo_nome, dominio):
    url = "https://primeleads.itb360.com.br/api-product/incoming-webhook/find-emails-first-last"
    data={
	"api_key": "W9J8J1A2-M5D9P1N8-F2Z9M9X1-V0N4U0L5",
	"first_name" : primeiro_nome,
	"last_name" : ultimo_nome,
	"domain" : dominio
}
    
    resp = requests.post(url, data=json.dumps(data))
    dados = json.loads(resp.content)

    if dados['email'] != None:
        print(dados['email'])
        return(dados['email'])
    else:
        print(f"Não encontrado o email do {primeiro_nome} {ultimo_nome}")
        return ""

if __name__ == '__main__':
    consulta_email('Jose', 'Prodossimo', 'cortex-intelligence.com')