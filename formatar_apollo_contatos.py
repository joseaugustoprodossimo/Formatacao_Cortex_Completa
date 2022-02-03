import pandas as pd
import funcoes

def apollo_contatos(df):
    df = df.filter(items=['Website','First Name', 'Last Name', 'Title','Email', 'Industry', 'Person Linkedin Url','Technologies','Keywords', 'SEO Description', 'Company Linkedin Url','Facebook Url', 'Twitter Url', 'Technologies', 'First Phone'])
    df.rename({'Website':'WEBSITE','First Name':'PRIMEIRO NOME','Last Name':'ULTIMO NOME','Title':'CARGO B2B','Email':'E-MAIL','Person Linkedin Url':'LINKEDIN URL','Technologies':'TECNOLOGIAS'}, axis = 1, inplace = True)
    df['WEBSITE'] = df['WEBSITE'].apply(funcoes.Formatar_sites)
    df['LINKEDIN URL'] = df['LINKEDIN URL'].apply(funcoes.Formatar_sites)
    df['Facebook Url'] = df['Facebook Url'].apply(funcoes.Formatar_sites)
    df['Twitter Url'] = df['Twitter Url'].apply(funcoes.Formatar_sites)
    df['Company Linkedin Url'] = df['Company Linkedin Url'].apply(funcoes.Formatar_sites)
    df['CARGO B2B'] = df['CARGO B2B'].str.title()
    
    for i in df.index:
      if df['PRIMEIRO NOME'][i] == "":
        df['PRIMEIRO NOME'][i] = df['ULTIMO NOME'][i]
        df['ULTIMO NOME'][i] = ""

    return df

if(__name__ == "__main__"):

  pasta_import = "C:\\Projetos\\Python\\Apollo\\"
  arquivo_import = "apollo-contacts-export"

  df = pd.read_csv(pasta_import + arquivo_import + ".csv")

  df = apollo_contatos(df)

  writer = pd.ExcelWriter(pasta_import + 'Output_' + arquivo_import + '.xlsx', engine='xlsxwriter',options={'strings_to_urls': False})
  df.to_excel(writer)
  writer.close()
  print('Finalizado')

  #arquivo_export = 'Output ' + arquivo_import + '.xlsx'
  #df.to_excel(pasta_import + arquivo_export, index = False)