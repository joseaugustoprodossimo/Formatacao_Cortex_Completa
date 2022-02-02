import pandas as pd

def ddplus_contatos_empresas(df_Contatos_Empresas):
  df_Contatos_Empresas = df_Contatos_Empresas.filter(items=['QUERY', 'keywords'])

  df_Contatos_Empresas['Company Phone'] = ''
  df_Contatos_Empresas['# Employees'] = ''
  df_Contatos_Empresas['Industry'] = ''
  df_Contatos_Empresas['Company Address'] = ''
  df_Contatos_Empresas['Company City'] = ''
  df_Contatos_Empresas['Company State'] = ''
  df_Contatos_Empresas['Company Country'] = ''
  df_Contatos_Empresas['SEO Description'] = ''
  df_Contatos_Empresas['Technologies'] = ''
  df_Contatos_Empresas['Annual Revenue'] = ''
  df_Contatos_Empresas['Company Linkedin Url'] = ''
  df_Contatos_Empresas['Facebook Url'] = ''
  df_Contatos_Empresas['Twitter Url'] = ''

  df_Contatos_Empresas.rename(columns={'QUERY':'Website', 'keywords':'Keywords'}, inplace=True)

  df_Contatos_Empresas = df_Contatos_Empresas.filter(items=['Website', 'Company Phone', '# Employees', 'Industry', 'Company Address', 'Company City', 
                                                            'Company State', 'Company Country', 'Keywords', 'SEO Description', 'Technologies', 
                                                            'Annual Revenue', 'Company Linkedin Url', 'Facebook Url', 'Twitter Url'])

  return df_Contatos_Empresas

if(__name__ == "__main__"):

  pasta_import = "caminho"
  arquivo_import = "arquivo"

  df = pd.read_csv(pasta_import + arquivo_import + ".csv")

  ddplus_contatos_empresas(df)

  arquivo_export = 'Output ' + arquivo_import + '.xlsx'
  df.to_excel(pasta_import + arquivo_export, index = False)