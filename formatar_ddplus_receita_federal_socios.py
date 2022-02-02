import pandas as pd
import funcoes

def ddplus_receita_deferal_socios(df):
    df.rename(columns={'Nome':'NOME'}, inplace=True)
    df['NOME_FORMATADO'] = df['NOME'].str.replace(" LTDA", "").str.replace(" EIRELI", "").str.replace(" S/A", "").str.replace(" SA", "").str.replace("S.A.", "").str.replace(" INC", "")
    df['NOME_FORMATADO'] = df['NOME_FORMATADO'].apply(funcoes.Remover_Caracteres_Especiais)
    df['NOME_FORMATADO'] = df['NOME_FORMATADO'].str.strip()
    df['PRIMEIRO NOME'] = df['NOME'].str.split(' ', expand=True).get(0)
    df['ULTIMO NOME'] = df['NOME_FORMATADO'].apply(funcoes.Retornar_Ultimo_Nome)
    df['Cargo'] = df['Cargo'].apply(funcoes.Retornar_Cargo)
    df['NOME'] = df['NOME'].str.title()
    return df

if(__name__ == "__main__"):

  pasta_import = "caminho"
  arquivo_import = "arquivo"

  df = pd.read_csv(pasta_import + arquivo_import + ".csv")

  ddplus_receita_deferal_socios(df)

  arquivo_export = 'Output ' + arquivo_import + '.xlsx'
  df.to_excel(pasta_import + arquivo_export, index = False)