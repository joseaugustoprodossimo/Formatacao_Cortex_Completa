import pandas as pd
import funcoes

def ddplus_linkedin(df_Linkedin):
    df_Linkedin['PRIMEIRO NOME'] = ''
    df_Linkedin['ULTIMO NOME'] = ''

    df_Linkedin['PRIMEIRO NOME'] = df_Linkedin['Nome'].str.split(' ', expand=True).get(0)
    df_Linkedin['ULTIMO NOME'] = df_Linkedin['Nome'].apply(funcoes.Retornar_Ultimo_Nome)

    df_Linkedin['Linkedin_contato'] = df_Linkedin['Linkedin_contato'].apply(funcoes.Formatar_sites)

    df_Linkedin = df_Linkedin.filter(items=['Query', 'PRIMEIRO NOME', 'ULTIMO NOME', 'Cargo', 'Email', 'Linkedin_contato'])

    df_Linkedin = df_Linkedin.rename(columns={'Query':'WEBSITE', 'PRIMEIRO NOME':'PRIMEIRO NOME', 'ULTIMO NOME':'ULTIMO NOME', 'Cargo':'CARGO', 'Email':'EMAIL', 'Linkedin_contato':'LINKEDIN_CONTATO'})

    return df_Linkedin

if(__name__ == "__main__"):

  pasta_import = "caminho"
  arquivo_import = "arquivo"

  df = pd.read_csv(pasta_import + arquivo_import + ".csv")

  ddplus_linkedin(df)

  arquivo_export = 'Output ' + arquivo_import + '.xlsx'
  df.to_excel(pasta_import + arquivo_export, index = False)