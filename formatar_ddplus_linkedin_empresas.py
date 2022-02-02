import pandas as pd
import funcoes

def ddplus_linkedin_empresas(df_Linkedin_Empresas):
    df_Linkedin_Empresas = df_Linkedin_Empresas.filter(['Query', 'Industria', 'Linkedin', 'Facebook', 'Twitter', 'Tecnologias'])
    df_Linkedin_Empresas['Linkedin'] = df_Linkedin_Empresas['Linkedin'].apply(funcoes.Formatar_sites)
    df_Linkedin_Empresas['Facebook'] = df_Linkedin_Empresas['Facebook'].apply(funcoes.Formatar_sites)
    df_Linkedin_Empresas['Twitter'] = df_Linkedin_Empresas['Twitter'].apply(funcoes.Formatar_sites)

    df_Linkedin_Empresas['Company Phone'] = ''
    df_Linkedin_Empresas['# Employees'] = ''
    df_Linkedin_Empresas['Company Address'] = ''
    df_Linkedin_Empresas['Company City'] = ''
    df_Linkedin_Empresas['Company State'] = ''
    df_Linkedin_Empresas['Company Country'] = ''
    df_Linkedin_Empresas['Keywords'] = ''
    df_Linkedin_Empresas['SEO Description'] = ''
    df_Linkedin_Empresas['Annual Revenue'] = ''

    df_Linkedin_Empresas.rename(columns={'Query':'Website', 'Industria':'Industry', 'Linkedin':'Company Linkedin Url', 'Facebook':'Facebook Url', 'Twitter':'Twitter Url', 'Tecnologias':'Technologies'}, inplace=True)

    df_Linkedin_Empresas = df_Linkedin_Empresas.filter(['Website', 'Company Phone', '# Employees', 'Industry',
       'Company Address', 'Company City', 'Company State', 'Company Country',
       'Keywords', 'SEO Description', 'Technologies', 'Annual Revenue',
       'Company Linkedin Url', 'Facebook Url', 'Twitter Url'])

    return df_Linkedin_Empresas

if(__name__ == "__main__"):

  pasta_import = "caminho"
  arquivo_import = "arquivo"

  df = pd.read_csv(pasta_import + arquivo_import + ".csv")

  ddplus_linkedin_empresas(df)

  arquivo_export = 'Output ' + arquivo_import + '.xlsx'
  df.to_excel(pasta_import + arquivo_export, index = False)