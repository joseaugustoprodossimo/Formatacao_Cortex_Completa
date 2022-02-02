import pandas as pd

# df deve ter as colunas 
# PRIMEIRO NOME
# ULTIMO NOME
# LIKEDIN_URL ou LINKEDIN_CONTATO
# EMAIL

def validar_url_linkedin(df):
  df['Validador Linkedin'] = ''

  df['PRIMEIRO NOME LOWER'] = df['PRIMEIRO NOME'].str.lower()
  df['ULTIMO NOME LOWER'] = df['ULTIMO NOME'].str.lower()

  df.rename(columns={'LIKEDIN_URL':'LINKEDIN_CONTATO'}, inplace=True)

  df['LINKEDIN_CONTATO'] = df['LINKEDIN_CONTATO'].astype(str)
  df['PRIMEIRO NOME'] = df['PRIMEIRO NOME'].astype(str)
  df['ULTIMO NOME'] = df['ULTIMO NOME'].astype(str)
  df['PRIMEIRO NOME LOWER'] = df['PRIMEIRO NOME LOWER'].astype(str)
  df['ULTIMO NOME LOWER'] = df['ULTIMO NOME LOWER'].astype(str)

  for i in df.index:
      if df['PRIMEIRO NOME LOWER'][i] in df['LINKEDIN_CONTATO'][i] or df['ULTIMO NOME LOWER'][i] in df['LINKEDIN_CONTATO'][i]:
          df['Validador Linkedin'][i] = 'Contem'
      else:
          df['LINKEDIN_CONTATO'][i] = ''

  df.loc[df['LINKEDIN_CONTATO'].str.contains('acwaa', regex=False), 'LINKEDIN_CONTATO'] = ''
  df.loc[df['LINKEDIN_CONTATO'].str.contains('pub', regex=False), 'LINKEDIN_CONTATO'] = ''
  df.loc[df['LINKEDIN_CONTATO'].str.contains('sales/people', regex=False), 'LINKEDIN_CONTATO'] = ''

  try:
    df['EMAIL'] = df['EMAIL'].str.lower()
  except:
    print("Problema ao colocar o email em minusculo")

  return df


if(__name__ == "__main__"):

  pasta_import = "C:\\Projetos\\Python\\Validador_Linkedin\\"
  arquivo_import = "Output_Contatos_Empresas_Linkedin_Apollo" + ".xlsx"

  df = pd.read_excel(pasta_import + arquivo_import)

  validar_url_linkedin(df)

  arquivo_export = 'Output ' + arquivo_import + '.xlsx'
  df.to_excel(pasta_import + arquivo_export, index = False)