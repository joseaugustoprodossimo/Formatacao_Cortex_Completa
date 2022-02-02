import pandas as pd
import funcoes

def ddplus_contatos(df_Contatos):
    Vazios = df_Contatos[ df_Contatos['location'].isnull() ].index
    df_Contatos.drop(Vazios, inplace=True)

    df_Contatos['Brasil'] = ''

    df_Contatos['location'] = df_Contatos['location'].str.lower()

    df_Contatos.loc[df_Contatos['location'].str.contains('brasil', regex=False), 'Brasil'] = 'Sim'
    df_Contatos.loc[df_Contatos['location'].str.contains('brazil', regex=False), 'Brasil'] = 'Sim'
    df_Contatos.loc[df_Contatos['location'].str.contains('brésil', regex=False), 'Brasil'] = 'Sim'
    df_Contatos.loc[df_Contatos['location'].str.contains('rio de janeiro', regex=False), 'Brasil'] = 'Sim'

    Vazios = df_Contatos[ df_Contatos['Brasil'] == '' ].index

    df_Contatos.drop(Vazios , inplace=True)

    df_Contatos['social_url'] = df_Contatos['social_url'].replace('false', '')

    df_Contatos = df_Contatos.drop(columns=['location'])
    df_Contatos = df_Contatos.drop(columns=['Brasil'])

    df_Contatos['social_url'] = df_Contatos['social_url'].apply(funcoes.Formatar_sites)

    return df_Contatos

if(__name__ == "__main__"):

  pasta_import = "caminho"
  arquivo_import = "arquivo"

  df = pd.read_csv(pasta_import + arquivo_import + ".csv")

  ddplus_contatos(df)

  arquivo_export = 'Output ' + arquivo_import + '.xlsx'
  df.to_excel(pasta_import + arquivo_export, index = False)