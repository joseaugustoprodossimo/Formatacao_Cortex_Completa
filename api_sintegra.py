from ast import Try
from xml import dom
import requests
import pandas as pd
import json
import funcoes

def consulta_IE(cnpj):
    url = "https://www.sintegraws.com.br/api/v1/execute-api.php"

    querystring = {"token":"98E3981F-29AC-41AE-B603-2A03F232F2D7","cnpj":cnpj,"plugin":"ST"}

    try:
        response = requests.request("GET", url, params=querystring)
    except:
        "Falha ao buscar o CNPJ: " + cnpj

    return(response.json()['inscricao_estadual'])
    

if __name__ == '__main__':
    pasta_import = "C:\\Projetos\\Python\\API Sintegra\\"
    arquivo_import = "Empresas"

    df = pd.read_excel(pasta_import + arquivo_import + ".xlsx")
    df['IE'] = ''

    for i in df.index:
        df['IE'][i] = consulta_IE(df['CNPJ'][i])
        print("CPF: " + df['CNPJ'][i] + " - IE: " + df['IE'][i])

    arquivo_export = 'Output ' + arquivo_import + '.xlsx'
    df.to_excel(pasta_import + arquivo_export, index = False)
    print("Finalizado")