import pandas as pd
import funcoes

def pegar_websites(df_input):
    # BASE WHOIS
    caminho_websites_whois = 'G:\\Drives compartilhados\\PS ITB\\Repositório do BI\\Repositório do BI - Documentos\\Bases auxiliares\\DB - Websites WhoIs\\'
    arquivo_websites_whois = 'domain_cnpj_total.csv'

    db_websites_whois = pd.read_csv(caminho_websites_whois + arquivo_websites_whois, converters={ 'cnpj': lambda x: str(x)})

    db_websites_whois['cnpj'] = db_websites_whois['cnpj'].str[0:2] + "." + db_websites_whois['cnpj'].str[2:5] + "." + db_websites_whois['cnpj'].str[5:8] + "/" + db_websites_whois['cnpj'].str[8:12] + "-" + db_websites_whois['cnpj'].str[12:14]

    # BASE EMPRESAS NACIONAIS EMPILHADAS
    caminho_websites_bases_empilhadas = 'G:\\Drives compartilhados\\PS ITB\\Repositório do BI\\Repositório do BI - Documentos\\Bases auxiliares\\DB - Bases Empilhadas\\'
    arquivo_websites_bases_empilhadas = 'Empresas Nacionais - Empilhamento.xlsx'

    db_websites_bases_empilhadas = pd.read_excel(caminho_websites_bases_empilhadas + arquivo_websites_bases_empilhadas)

    # BASE WEBSITES PARA CNPJ
    caminho_website_cnpj = 'G:\\Drives compartilhados\\PS ITB\\Repositório do BI\\Repositório do BI - Documentos\\Bases auxiliares\\DB - Website Para CNPJ\\'
    arquivo_website_cnpj = 'Websites para CNPJs.xlsx'
    arquivo_website_cnpj_banco = 'Websites Banco - 16-08-21 - 877k.xlsx'

    db_website_cnpj = pd.read_excel(caminho_website_cnpj + arquivo_website_cnpj)
    db_website_cnpj_banco = pd.read_excel(caminho_website_cnpj + arquivo_website_cnpj_banco)

    # LISTA DE NOMES PARA RETIRAR
    retirar = ['facebook', 'youtube']

    db_websites_bases_empilhadas = db_websites_bases_empilhadas.filter(items=['CNPJ', 'WEBSITE 1'])
    db_websites_bases_empilhadas.rename(columns={'WEBSITE 1':'Website'}, inplace=True)

    db_website_cnpj = db_website_cnpj.filter(items=['CNPJ','Website'])
    db_websites_whois = db_websites_whois.filter(items=['CNPJ','Website'])
    db_website_cnpj_banco.rename(columns={'cnpj':'CNPJ','site':'Website'}, inplace=True)
    db_website_cnpj_banco = db_website_cnpj_banco.filter(items=['CNPJ','Website'])

    df_todos = pd.concat([db_website_cnpj, db_websites_whois, db_website_cnpj_banco, db_websites_bases_empilhadas])
    df_todos = df_todos.drop_duplicates()

    df_input = df_input.merge(df_todos, on='CNPJ', how='left')
    df_input = df_input.filter(items=['CNPJ', 'Website'])

    df_input = df_input.reset_index(drop=True)

    for i in len(retirar):
        df_input['Website'] = df_input['Website'].replace(retirar[i], '')

    return df_input

if(__name__ == "__main__"):

  pasta_import = "caminho"
  arquivo_import = "arquivo"

  df = pd.read_csv(pasta_import + arquivo_import + ".csv")

  pegar_websites(df)

  arquivo_export = 'Output ' + arquivo_import + '.xlsx'
  df.to_excel(pasta_import + arquivo_export, index = False)