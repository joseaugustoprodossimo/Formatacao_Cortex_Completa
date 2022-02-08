import pandas as pd
import funcoes
import capturar_email_primeleads

def juntar_output_br2_info_emp_dominio_output_contatos(df, df_socios, df_contatos, df_tecnologias, df_matriz_cnpj_website, df_DQ):
    print("DF Socios")
    df_socios.rename(columns={'Nome':'NOME'}, inplace=True)

    df_socios['NOME_FORMATADO'] = df_socios['NOME'].str.replace(" LTDA", "").str.replace(" EIRELI", "").str.replace(" S/A", "").str.replace(" SA", "").str.replace("S.A.", "").str.replace(" INC", "")
    #df_socios['NOME_FORMATADO'] = df_socios['NOME_FORMATADO'].apply(funcoes.Remover_Caracteres_Especiais)

    df_socios['NOME_FORMATADO'] = df_socios['NOME_FORMATADO'].str.strip()

    df_socios['PRIMEIRO NOME'] = df_socios['NOME'].str.split(' ', expand=True).get(0)
    df_socios['PRIMEIRO NOME'] = df_socios['PRIMEIRO NOME'].apply(funcoes.Remover_Caracteres_Especiais)
    df_socios['ULTIMO NOME'] = df_socios['NOME_FORMATADO'].apply(funcoes.Retornar_Ultimo_Nome)
    df_socios['ULTIMO NOME'] = df_socios['ULTIMO NOME'].apply(funcoes.Remover_Caracteres_Especiais)

    df_socios['Cargo'] = df_socios['Cargo'].apply(funcoes.Retornar_Cargo)

    df_socios['NOME'] = df_socios['NOME'].str.title()

    df_socios = df_socios.merge(df, left_on= 'QUERY', right_on= 'CNPJ', how = 'left')

    df_socios['EMAIL'] = ''

    df_socios.rename(columns={'Cargo':'CARGO'}, inplace=True)

    df_socios = df_socios.filter(items=['CNPJ', 'RAZÃO SOCIAL', 'NOME', 'PRIMEIRO NOME', 'ULTIMO NOME', 'CARGO', 'EMAIL'])

    df_socios_buscar_email = df_socios
    df_socios_buscar_email = df_socios_buscar_email.merge(df_matriz_cnpj_website, on='CNPJ', how = 'inner')

    df_socios_buscar_email['Input_AnyLeads'] = df_socios_buscar_email['PRIMEIRO NOME'].str.lower() + ',' + df_socios_buscar_email['ULTIMO NOME'].str.lower() + ',' + df_socios_buscar_email['Website'].str.lower() + ','

    df_socios_buscar_email = df_socios_buscar_email.filter(items=['CNPJ', 'NOME', 'PRIMEIRO NOME', 'ULTIMO NOME', 'Website', 'Input_AnyLeads', 'EMAIL'])

    for i in df_socios_buscar_email.index:
        if len(df_socios_buscar_email['PRIMEIRO NOME'][i]) > 0 and len(df_socios_buscar_email['ULTIMO NOME'][i]) > 0:
            df_socios_buscar_email['EMAIL'][i] = capturar_email_primeleads.consulta_email(df_socios_buscar_email['PRIMEIRO NOME'][i], df_socios_buscar_email['ULTIMO NOME'][i], df_socios_buscar_email['Website'][i])

    df_socios_buscar_email['Chave'] = df_socios_buscar_email['CNPJ'] + df_socios_buscar_email['PRIMEIRO NOME'] + df_socios_buscar_email['ULTIMO NOME']

    df_socios['Chave'] = df_socios['CNPJ'] + df_socios['PRIMEIRO NOME'] + df_socios['ULTIMO NOME']

    df_socios = df_socios.merge(df_socios_buscar_email, on='Chave', how='left')

    df_socios = df_socios.filter(items=['CNPJ', 'RAZÃO SOCIAL', 'NOME', 'PRIMEIRO NOME', 'ULTIMO NOME', 'CARGO', 'EMAIL'])

    print("DF Tecnologias")

    df_tecnologias = df_tecnologias.merge(df_matriz_cnpj_website, left_on='QUERY', right_on='Website', how = 'inner')

    df_tecnologias= df_tecnologias.filter(items=['CNPJ', 'category', 'name'])

    df_tecnologias = df_tecnologias.merge(df, on='CNPJ', how='inner')

    df_tecnologias = df_tecnologias.filter(items=['CNPJ', 'RAZÃO SOCIAL', 'category', 'name'])

    df_tecnologias.rename(columns={'category': 'CATEGORIA', 'name': 'NOME'}, inplace=True)

    print("DF Contatos")

    df_contatos = df_contatos.merge(df_matriz_cnpj_website, left_on='WEBSITE', right_on='Website', how='inner')

    df_contatos = df_contatos.filter(items=['CNPJ', 'PRIMEIRO NOME', 'ULTIMO NOME', 'CARGO', 'EMAIL', 'LINKEDIN_CONTATO'])

    df_contatos = df_contatos.merge(df, on='CNPJ', how='inner')

    df_contatos = df_contatos.filter(items=['CNPJ', 'RAZÃO SOCIAL', 'PRIMEIRO NOME', 'ULTIMO NOME', 'CARGO', 'EMAIL', 'LINKEDIN_CONTATO'])

    print("DF DQ")

    df_DQ.loc[0] = 'Empresas', df['CNPJ'].count()
    df_DQ.loc[1] = 'Contatos', df_contatos['CNPJ'].count()
    df_DQ.loc[2] = 'E-mails', df_contatos['EMAIL'].count()
    df_DQ.loc[3] = 'Assertividade', ''

    print("Finalizado")

    return df, df_socios, df_contatos, df_tecnologias, df_matriz_cnpj_website, df_DQ

if(__name__ == "__main__"):

    caminho = 'C:\\Projetos\\Python\\Juntar Dados Cadastrais e Contatos\\'

    DadosCadastrais = 'BR2 - Enriquecimento Cliente - DB - Cortex'
    SociosReceita = 'Receita Federal'
    Contatos = 'Output_Contatos_Empresas_Linkedin_Apollo'
    Tecnologias = 'Informações de Empresas Domínios'

    df = pd.read_excel(caminho + DadosCadastrais + '.xlsx', sheet_name='Dados Cadastrais - Cortex', converters={ 'TELEFONE 1': lambda x: str(x), 'TELEFONE 2': lambda x: str(x), 'TELEFONE 3': lambda x: str(x), 'TELEFONE 4': lambda x: str(x), 'TELEFONE 5': lambda x: str(x)})
    df_socios = pd.read_excel(caminho + SociosReceita + '.xlsx', sheet_name='Adicionais')
    df_contatos = pd.read_excel(caminho + Contatos + '.xlsx', sheet_name='Contatos')
    df_tecnologias = pd.read_excel(caminho + Tecnologias + '.xlsx', sheet_name='Adicionais')
    df_matriz_cnpj_website = pd.read_excel(caminho + DadosCadastrais + '.xlsx', sheet_name='Matriz CNPJ Website')
    df_DQ = pd.read_excel(caminho + DadosCadastrais + '.xlsx', sheet_name='DQ')

    df, df_socios, df_contatos, df_tecnologias, df_matriz_cnpj_website, df_DQ = juntar_output_br2_info_emp_dominio_output_contatos(df, df_socios, df_contatos, df_tecnologias, df_matriz_cnpj_website, df_DQ)

    arquivo = 'PSNEW-9999'
    cliente = 'Teste'
    writer = pd.ExcelWriter(caminho + arquivo + ' - Enriquecimento ' + cliente + ' - DB - Cortex' + '.xlsx', engine='xlsxwriter')

    #Escreve os dataframes em diferentes sheets dentro do arquivo final;
    df_DQ.to_excel(writer, sheet_name='DQ', index=False)
    df.to_excel(writer, sheet_name='Dados Cadastrais - Cortex', index=False)
    df_matriz_cnpj_website.to_excel(writer, sheet_name='Matriz CNPJ Website', index=False)
    df_socios.to_excel(writer, sheet_name='Dados Sócios - Cortex', index=False)
    df_contatos.to_excel(writer, sheet_name='Contatos B2B - Cortex', index=False)
    df_tecnologias.to_excel(writer, sheet_name='Tecnologias Cloud - Cortex', index=False)

    #Fecha o arquivo e salva no diretório;
    writer.save()