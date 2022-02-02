import pandas as pd
import funcoes

def apollo_empresas(df):
  df = df.filter(items=['Website', 'Keywords','SEO Description',  'Company Linkedin Url', 'Facebook Url', 'Twitter Url', 'Technologies'])
  df['Website'] = df['Website'].apply(funcoes.Formatar_sites)
  df['Facebook Url'] = df['Facebook Url'].apply(funcoes.Formatar_sites)
  df['Twitter Url'] = df['Twitter Url'].apply(funcoes.Formatar_sites)
  df['Company Linkedin Url'] = df['Company Linkedin Url'].apply(funcoes.Formatar_sites)

  df['Company Phone'] = df['Company Phone'].str.replace("'", "").str.replace('-', '').str.replace('/', '').str.replace(' ', '').str.replace('(', '').str.replace(')', '')

  df['Company Phone'] = df['Company Phone'].str.replace("\+55", "")

  df.loc[ df['Company Phone'].str.len() > 0, 'Company Phone'] = "+55" + df['Company Phone']

  return df

if(__name__ == "__main__"):

  pasta_import = "caminho"
  arquivo_import = "arquivo"

  df = pd.read_csv(pasta_import + arquivo_import + ".csv")

  apollo_empresas(df)

  arquivo_export = 'Output ' + arquivo_import + '.xlsx'
  df.to_excel(pasta_import + arquivo_export, index = False)