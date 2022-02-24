from xml import dom
import requests
import pandas as pd
import json
import funcoes

def consulta_email(primeiro_nome, ultimo_nome, dominio):
    url = "https://primeleads.itb360.com.br/api-product/incoming-webhook/find-emails-first-last"
    data={
	"api_key": "W9J8J1A2-M5D9P1N8-F2Z9M9X1-V0N4U0L5",
	"first_name" : primeiro_nome,
	"last_name" : ultimo_nome,
	"domain" : dominio
    }
    
    try:
        resp = requests.post(url, data=json.dumps(data))
        dados = json.loads(resp.content)
        if dados['email'] != None:
            print(dados['email'])
            return(dados['email'])
        else:
            print(f"Não encontrado o email do {primeiro_nome} {ultimo_nome}")
            return ""
    except:
        print(f"Deu erro para buscar o email do {primeiro_nome} {ultimo_nome}")

if __name__ == '__main__':
    pasta_import = "C:\\Projetos\\Python\\Pegar email anyleads\\"
    arquivo_import = "socios"

    df = pd.read_excel(pasta_import + arquivo_import + ".xlsx")

    df['PRIMEIRO NOME'] = ''
    df['ULTIMO NOME'] = ''

    df.rename(columns={'NOME DO SÓCIO':'NOME'}, inplace=True)

    df['PRIMEIRO NOME'] = df['NOME'].str.split(' ', expand=True).get(0)
    df['ULTIMO NOME'] = df['NOME'].apply(funcoes.Retornar_Ultimo_Nome)
    df['EMAIL'] = ''
    #df['CARGO'] = df['CARGO'].str.title()
    #df['Qualificação sócio'] = df['Qualificação sócio'].apply(funcoes.Retornar_Cargo)
    #df['qualificacao'] = df['qualificacao'].str.title()

    tamanho_total = len(df)

    for i in df.index:

        print( "Percentual: " + str(int(i / tamanho_total * 100)) + '%')

        primeiro_nome = str(df['PRIMEIRO NOME'][i]).strip()
        ultimo_nome = str(df['ULTIMO NOME'][i]).strip()
        website = str(df['Website'][i]).strip()

        #print(str(len(primeiro_nome)) + " - " + primeiro_nome)
        #print(str(len(ultimo_nome)) + ' - ' + ultimo_nome)
        #print(str(len(website)) + ' - ' + website)

        if (len(primeiro_nome) > 0) and (len(ultimo_nome) > 0) and (len(website) > 0) and (primeiro_nome != 'nan') and (ultimo_nome != 'nan') and (website != 'nan'):
            df['EMAIL'][i] = consulta_email(df['PRIMEIRO NOME'][i].title(), df['ULTIMO NOME'][i].title(), df['Website'][i].lower())

    arquivo_export = 'Output ' + arquivo_import + '.xlsx'
    df.to_excel(pasta_import + arquivo_export, index = False)
    print("Finalizado")