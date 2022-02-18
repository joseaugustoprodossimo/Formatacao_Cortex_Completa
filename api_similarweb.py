from ast import Try
from xml import dom
import requests
import pandas as pd
import json
import funcoes

def consulta_SimilarWeb(dominio):
    url = "https://api.dataforseo.com/v3/traffic_analytics/similarweb/live"
    data={
	"Authorization": "Basic bWFydmluLmZpb3JpQGNvcnRleC1pbnRlbGxpZ2VuY2UuY29tOmU0Nzc1MzkzMWIxZWZlNzA=",
	"Content-Type":	"text/plain",
    "target": dominio,
    #"Host"
    #"Accept"
    #"Accept-Encoding": "gzip, deflate, br"
    }
    
    resp = requests.post(url, data=json.dumps(data))
    dados = json.loads(resp.content)
    print(dados)
    

if __name__ == '__main__':
    #pasta_import = "C:\\Projetos\\Python\\API Sintegra\\"
    #arquivo_import = "Empresas"

    #df = pd.read_excel(pasta_import + arquivo_import + ".xlsx")
    #df['IE'] = ''

    #for i in df.index:
    #    df['IE'][i] = consulta_IE(df['CNPJ'][i])
    #    print("CPF: " + df['CNPJ'][i] + " - IE: " + df['IE'][i])

    #arquivo_export = 'Output ' + arquivo_import + '.xlsx'
    #df.to_excel(pasta_import + arquivo_export, index = False)

    consulta_SimilarWeb('magazineluiza.com.br')

    print("Finalizado")