import pandas as pd

# df_matriz_cnpj_website deve ter as colunas: Website, CNPJ
# df_tecnologias deve ter as colunas: QUERY, category, name
# df_dados_cadastrais deve ter as colunas: CNPJ, RAZÃO SOCIAL

def juntar_tec(df_matriz_cnpj_website, df_tecnologias, df_dados_cadastrais):
    df_tecnologias = df_tecnologias.merge(df_matriz_cnpj_website, left_on='QUERY', right_on='Website', how = 'inner')
    df_tecnologias= df_tecnologias.filter(items=['CNPJ', 'category', 'name'])
    df_tecnologias = df_tecnologias.merge(df_dados_cadastrais, on='CNPJ', how='inner')
    df_tecnologias = df_tecnologias.filter(items=['CNPJ', 'RAZÃO SOCIAL', 'category', 'name'])
    df_tecnologias.rename(columns={'category': 'CATEGORIA', 'name': 'NOME'}, inplace=True)
    return df_tecnologias