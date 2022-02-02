import pandas as pd
import funcoes

def ddplus_dados_cadastrais_autodesk(df):
    df['ESTADO'] = ''
    df['SOCIO 1'] = ''
    df['SOCIO 2'] = ''
    df['SOCIO 3'] = ''
    df['KEYWORDS'] = ''
    df['SEO DESCRIPTION'] = ''
    df['COMPANY LINKEDIN URL'] = ''
    df['FACEBOOK URL'] = ''
    df['TWITTER URL'] = ''
    df['TECHNOLOGIES'] = ''

    df['CEP'] = df['CEP'].str[0:2] + "." + df['CEP'].str[2:5] + "-" + df['CEP'].str[5:]

    df['DDD'] = df['DDD'].str.replace('0', '')
    df['DDD ADMINISTRADOR'] = df['DDD ADMINISTRADOR'].str.replace('0', '')
    df['TELEFONE'] = '+55' + df['DDD'] + df['TELEFONE']
    df['TELEFONE ADMINISTRADOR'] = '+55' + df['DDD ADMINISTRADOR'] + df['TELEFONE ADMINISTRADOR']

    df['SOCIO 1'] = df['SOCIOS'].str.split(',', expand=True).get(0)
    df['SOCIO 2'] = df['SOCIOS'].str.split(',', expand=True).get(1)
    df['SOCIO 3'] = df['SOCIOS'].str.split(',', expand=True).get(2)

    df['CNPJ'] = df['QUERY']

    df['WEBSITE'] = df['WEBSITE'].str.replace('http://', '').str.replace('https://', '').str.replace('www4.', '').str.replace('www2.', '').str.replace('www1.', '').str.replace('wwwa.', '').str.replace('www7.', '').str.replace('wwwt.', '').str.replace('wwws.', '').str.replace('www3.', '').str.replace('www5.', '')
    df['WEBSITE'] = df['WEBSITE'].str.replace('www.', '')
    df['WEBSITE'] = df['WEBSITE'].str.split('/', expand=True).get(0)

    df_website = df.filter(items=['CNPJ','WEBSITE'])
    df_website.dropna(subset=['WEBSITE'], inplace=True)

    Vazios = df_website[ df_website['WEBSITE'] == '' ].index
    df_website.drop(Vazios , inplace=True)

    df.loc[df['UF'] == 'AC', 'ESTADO'] = 'ACRE'
    df.loc[df['UF'] == 'AL', 'ESTADO'] = 'ALAGOAS'
    df.loc[df['UF'] == 'AP', 'ESTADO'] = 'AMAPA'
    df.loc[df['UF'] == 'AM', 'ESTADO'] = 'AMAZONAS'
    df.loc[df['UF'] == 'BA', 'ESTADO'] = 'BAHIA'
    df.loc[df['UF'] == 'CE', 'ESTADO'] = 'CEARA'
    df.loc[df['UF'] == 'ES', 'ESTADO'] = 'ESPIRITO SANTO'
    df.loc[df['UF'] == 'GO', 'ESTADO'] = 'GOIAS'
    df.loc[df['UF'] == 'MA', 'ESTADO'] = 'MARANHAO'
    df.loc[df['UF'] == 'MT', 'ESTADO'] = 'MATO GROSSO'
    df.loc[df['UF'] == 'MS', 'ESTADO'] = 'MATO GROSSO DO SUL'
    df.loc[df['UF'] == 'MG', 'ESTADO'] = 'MINAS GERAIS'
    df.loc[df['UF'] == 'PA', 'ESTADO'] = 'PARA'
    df.loc[df['UF'] == 'PB', 'ESTADO'] = 'PARAIBA'
    df.loc[df['UF'] == 'PR', 'ESTADO'] = 'PARANA'
    df.loc[df['UF'] == 'PE', 'ESTADO'] = 'PERNAMBUCO'
    df.loc[df['UF'] == 'PI', 'ESTADO'] = 'PIAUI'
    df.loc[df['UF'] == 'RJ', 'ESTADO'] = 'RIO DE JANEIRO'
    df.loc[df['UF'] == 'RN', 'ESTADO'] = 'RIO GRANDE DO NORTE'
    df.loc[df['UF'] == 'RS', 'ESTADO'] = 'RIO GRANDE DO SUL'
    df.loc[df['UF'] == 'RO', 'ESTADO'] = 'RONDONIA'
    df.loc[df['UF'] == 'RR', 'ESTADO'] = 'RORAIMA'
    df.loc[df['UF'] == 'SC', 'ESTADO'] = 'SANTA CATARINA'
    df.loc[df['UF'] == 'SP', 'ESTADO'] = 'SAO PAULO'
    df.loc[df['UF'] == 'SE', 'ESTADO'] = 'SERGIPE'
    df.loc[df['UF'] == 'TO', 'ESTADO'] = 'TOCANTINS'
    df.loc[df['UF'] == 'DF', 'ESTADO'] = 'DISTRITO FEDERAL'

    df.loc[df['NUMERO FUNCIONARIOS EMPRESA'] == '0', 'NUMERO FUNCIONARIOS EMPRESA'] = '1 a 5'

    df_DQ = pd.DataFrame()
    df_DQ = pd.DataFrame(columns=['BigNumbers', 'Valores'])
    df_DQ.loc[0] = 'Empresas', df['CNPJ'].count()
    df_DQ.loc[1] = 'Qtd Empresas sem Telefone', df['CNPJ'].count() - df['TELEFONE'].count()
    df_DQ.loc[2] = 'Qtd Empresas sem Website', df['CNPJ'].count() - df['WEBSITE'].count()
    df_DQ.loc[3] = 'Qtd Empresas sem Socios', df['CNPJ'].count() - df['SOCIO 1'].count()
    df_DQ.loc[4] = 'Contatos', ''
    df_DQ.loc[5] = 'E-mails', ''
    df_DQ.loc[6] = 'Assertividade dos e-mails', ''

    df = df.filter(items=[
        'CNPJ',
        'RAZAO SOCIAL',
        'NOME FANTASIA',
        'STATUS',
        'DATA ABERTURA',
        'TIPO LOGRADOURO',
        'LOGRADOURO',
        'NUMERO',
        'COMPLEMENTO',
        'BAIRRO',
        'CEP',
        'UF',
        'ESTADO',
        'MUNICIPIO',
        'TELEFONE',
        'EMAIL',
        'CNAE PRINCIPAL CODIGO',
        'CNAE PRINCIPAL DESCRICAO',
        'SETOR',
        'CAPITAL SOCIAL',
        'RECEITA ESTIMADA EMPRESA',
        'NUMERO FUNCIONARIOS EMPRESA',
        'SOCIO 1',
        'SOCIO 2',
        'SOCIO 3',
        'NOME DO ADMINISTRADOR',
        'TELEFONE ADMINISTRADOR',
        'WEBSITE',
        'KEYWORDS',
        'SEO DESCRIPTION',
        'COMPANY LINKEDIN URL',
        'FACEBOOK URL',
        'TWITTER URL',
        'TECHNOLOGIES'
    ])

    df_tecnologias = pd.DataFrame()
    COLUNAS = [
        'CNPJ',
        'RAZÃO SOCIAL',
        'CATEGORIA',
        'NOME'
    ]
    df_tecnologias = pd.DataFrame(columns=COLUNAS)

    df_contatos = pd.DataFrame()
    COLUNAS = [
        'CNPJ',
        'RAZAO SOCIAL',
        'FIRST NAME',
        'LAST NAME',
        'JOB TITLE',
        'EMAIL',
        'PERSON LINKEDIN URL',
        'FIRST PHONE'
    ]
    df_contatos = pd.DataFrame(columns=COLUNAS)

    df_socios = pd.DataFrame()
    COLUNAS = [
        'CNPJ',
        'RAZAO SOCIAL',
        'NOME',
        'CARGO'
    ]
    df_socios = pd.DataFrame(columns=COLUNAS)

    df.sort_values(by='RAZAO SOCIAL', axis=0, inplace=True)

    return(df_DQ, df, df_socios, df_website, df_contatos, df_tecnologias)

if(__name__ == "__main__"):

    caminho = "caminho"
    arquivo = "arquivo"

    df = pd.read_excel(caminho + arquivo + '.xlsx')

    df, df_DQ, df_socios, df_website, df_contatos, df_tecnologias = ddplus_dados_cadastrais_autodesk(df)

    #Cria um excel writer usando xlsxwriter como engine;
    # Enriquecimento
    # Extração
    # Estudo
    writer = pd.ExcelWriter(caminho + 'Enriquecimento' + ' - ' + arquivo + ' - DB - Cortex' + '.xlsx', engine='xlsxwriter')

    #Escreve os dataframes em diferentes sheets dentro do arquivo final;
    df_DQ.to_excel(writer, sheet_name='DQ', index=False)
    df.to_excel(writer, sheet_name='Dados Cadastrais', index=False)
    df_socios.to_excel(writer, sheet_name='Dados Sócios', index=False)
    df_website.to_excel(writer, sheet_name='Matriz CNPJ Website', index=False)
    df_contatos.to_excel(writer, sheet_name='Dados Contatos B2B', index=False)
    df_tecnologias.to_excel(writer, sheet_name='Dados Tecnologias Cloud', index=False)

    #Fecha o arquivo e salva no diretório;
    writer.save()