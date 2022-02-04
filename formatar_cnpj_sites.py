import pandas as pd
import re

pasta_import = 'C:\\Projetos\\UiPath\Teste\\'
arquivo_import = 'Extracao'

df = pd.read_excel(pasta_import + arquivo_import+ '.xlsx')

def retornaUltimos14(item):
    tamanho = len(item)
    return item[tamanho-14:]

def Tirar_CNPJ_Scopo(scopo, cnpj):
    str(cnpj)
    str(scopo)
    urlformatado = cnpj.replace(".", '').replace("/", '').replace("-", '')
    scopo = scopo.replace(urlformatado, "")
    return scopo

def Tirar_CNPJ_Int_Scopo(scopo, cnpj):
    cnpj = str(cnpj)
    scopo = str(scopo)
    urlformatado = cnpj.replace(".", '').replace("/", '').replace("-", '')
    urlformatadoInt = int(urlformatado)
    urlformatado = str(urlformatadoInt)
    scopo = scopo.replace(urlformatado, "")
    return scopo

def Tirar_CNPJ_Scopo_Ate_a_Barra(scopo, cnpj):
    str(cnpj)
    str(scopo)

    cnpj = cnpj.split("/")

    urlformatado = cnpj[0].replace(".", '').replace("/", '').replace("-", '')
    scopo = scopo.replace(urlformatado, "")
    return scopo

def Tirar_CNPJ_Scopo_Split_Ponto(scopo, cnpj):
    str(cnpj)
    str(scopo)

    cnpj = cnpj.split(".")

    urlformatado = cnpj[0] + cnpj[1]
    scopo = scopo.replace(urlformatado, "")
    return scopo

def Remover_Caracteres_Especiais(item):
    return re.sub('[^A-Za-z0-9]+ ', '', item )

def formata_cnpj(item):
    item = str(item)
    if item == "":
        return item
    else:
        return item[0:2] + "." + item[2:5] + "." + item[5:8] + "/" + item[8:12] + "-" + item[12:14]

df['Loc'] = ''

df.loc[~df['URL'].str.contains('cnpj.info|situacaocadastral.info|cnpj.biz|cadastroempresa|casadosdados|informecadastral|consultas.plus|econodata|cnpjs.rocks|consultacnpj.com|cnpj.services|consultecnpj|empresasdobrasil|consultascnpj|transparencia.cc|compras.dados|cnpjs.info|valor.srv|brasilcnpj.org|portaltransparencia|cnpj.dendrites'), 'Loc'] = '0'
df.loc[df['URL'].str.contains('cnpj.info'), 'Loc'] = '1'
df.loc[df['URL'].str.contains('situacaocadastral.info'), 'Loc'] = '2'
df.loc[df['URL'].str.contains('cnpj.biz'), 'Loc'] = '3'
df.loc[df['URL'].str.contains('cadastroempresa'), 'Loc'] = '4'
df.loc[df['URL'].str.contains('casadosdados'), 'Loc'] = '5'
df.loc[df['URL'].str.contains('informecadastral'), 'Loc'] = '6'
df.loc[df['URL'].str.contains('consultas.plus'), 'Loc'] = '7'
df.loc[df['URL'].str.contains('econodata'), 'Loc'] = '8'
df.loc[df['URL'].str.contains('cnpjs.rocks'), 'Loc'] = '9'
df.loc[df['URL'].str.contains('consultacnpj.com'), 'Loc'] = '10'
df.loc[df['URL'].str.contains('cnpj.services'), 'Loc'] = '11'
df.loc[df['URL'].str.contains('consultecnpj'), 'Loc'] = '12'
df.loc[df['URL'].str.contains('empresasdobrasil'), 'Loc'] = '13'
df.loc[df['URL'].str.contains('consultascnpj'), 'Loc'] = '14'
df.loc[df['URL'].str.contains('transparencia.cc'), 'Loc'] = '15'
df.loc[df['URL'].str.contains('compras.dados'), 'Loc'] = '16'
df.loc[df['URL'].str.contains('cnpjs.info'), 'Loc'] = '17'
df.loc[df['URL'].str.contains('valor.srv'), 'Loc'] = '18'
df.loc[df['URL'].str.contains('brasilcnpj.org'), 'Loc'] = '19'
df.loc[df['URL'].str.contains('portaltransparencia'), 'Loc'] = '20'
df.loc[df['URL'].str.contains('cnpj.dendrites'), 'Loc'] = '21'

df0 = df[ df['Loc'] == '0' ]
df1 = df[ df['Loc'] == '1' ]
df2 = df[ df['Loc'] == '2' ]
df3 = df[ df['Loc'] == '3' ]
df4 = df[ df['Loc'] == '4' ]
df5 = df[ df['Loc'] == '5' ]
df6 = df[ df['Loc'] == '6' ]
df7 = df[ df['Loc'] == '7' ]
df8 = df[ df['Loc'] == '8' ]
df9 = df[ df['Loc'] == '9' ]
df10 = df[ df['Loc'] == '10' ]
df11 = df[ df['Loc'] == '11' ]
df12 = df[ df['Loc'] == '12' ]
df13 = df[ df['Loc'] == '13' ]
df14 = df[ df['Loc'] == '14' ]
df15 = df[ df['Loc'] == '15' ]
df16 = df[ df['Loc'] == '16' ]
df17 = df[ df['Loc'] == '17' ]
df18 = df[ df['Loc'] == '18' ]
df19 = df[ df['Loc'] == '19' ]
df20 = df[ df['Loc'] == '20' ]
df21 = df[ df['Loc'] == '21' ]

df0.reset_index(inplace = True)
df1.reset_index(inplace = True)
df2.reset_index(inplace = True)
df3.reset_index(inplace = True)
df4.reset_index(inplace = True)
df5.reset_index(inplace = True)
df6.reset_index(inplace = True)
df7.reset_index(inplace = True)
df8.reset_index(inplace = True)
df9.reset_index(inplace = True)
df10.reset_index(inplace = True)
df11.reset_index(inplace = True)
df12.reset_index(inplace = True)
df13.reset_index(inplace = True)
df14.reset_index(inplace = True)
df15.reset_index(inplace = True)
df16.reset_index(inplace = True)
df17.reset_index(inplace = True)
df18.reset_index(inplace = True)
df19.reset_index(inplace = True)
df20.reset_index(inplace = True)
df21.reset_index(inplace = True)

df2['URL'] = df2['URL'].str.split('/', expand=True).get(4)
df3['URL'] = df3['URL'].str.split('/', expand=True).get(3)
df4['URL'] = df4['URL'].str.split('/', expand=True).get(4) + "/" + df4['URL'].str.split('/', expand=True).get(5)
df5['URL'] = df5['URL'].str.split('/', expand=True).get(5)
df6['URL'] = df6['URL'].str.split('/', expand=True).get(4)
df7['URL'] = df7['URL'].str.split('/', expand=True).get(6)
df8['URL'] = df8['URL'].str.split('/', expand=True).get(7)
df9['URL'] = df9['URL'].str.split('/', expand=True).get(4)
df10['URL'] = df10['URL'].str.split('/', expand=True).get(4)
df11['URL'] = df11['URL'].str.split('/', expand=True).get(3)
df12['URL'] = df12['URL'].str.split('/', expand=True).get(4)
df13['URL'] = df13['URL'].str.split('/', expand=True).get(4)
df14['URL'] = df14['URL'].str.split('/', expand=True).get(4)
df15['URL'] = df15['URL'].str.split('/', expand=True).get(5)
df16['URL'] = df16['URL'].str.split('/', expand=True).get(6)
df17['URL'] = df17['URL'].str.split('/', expand=True).get(4)
df18['URL'] = df18['URL'].str.split('/', expand=True).get(3)
df19['URL'] = df19['URL'].str.split('/', expand=True).get(5)
df20['URL'] = df20['URL'].str.split('/', expand=True).get(4)
df21['URL'] = df21['URL'].str.split('/', expand=True).get(4)

df3['Scopo'] = df3['Scopo'].str.split(' -', expand=True).get(0)
df7['Scopo'] = df7['Scopo'].str.split(' » ', expand=True).get(0)
df8['Scopo'] = df8['Scopo'].str.split(' -', expand=True).get(0)
df9['Scopo'] = df9['Scopo'].str.split(' -', expand=True).get(0)
df11['Scopo'] = df11['Scopo'].str.split(' -', expand=True).get(0)
df12['Scopo'] = df12['Scopo'].str.split(' -', expand=True).get(0)
df17['Scopo'] = df17['Scopo'].str.split(' -', expand=True).get(0)
df21['Scopo'] = df21['Scopo'].str.split(' -', expand=True).get(0)
df7['URL'] = df7['URL'].str.split('-', expand=True).get(0)
df8['URL'] = df8['URL'].str.split('-', expand=True).get(0)
df12['URL'] = df12['URL'].str.split('-', expand=True).get(0)
df15['URL'] = df15['URL'].str.split('-', expand=True).get(0)

df4['URL'] = df4['URL'].str.split('-', expand=True).get(0) + "-" + df4['URL'].str.split('-', expand=True).get(1)

df19.dropna(subset=['URL'], inplace=True)

Vazios = df19[ df19['URL'] == '' ].index

df19.drop(Vazios , inplace=True)

df2['URL'] = df2['URL'].apply(retornaUltimos14)
df5['URL'] = df5['URL'].apply(retornaUltimos14)
df6['URL'] = df6['URL'].apply(retornaUltimos14)
df10['URL'] = df10['URL'].apply(retornaUltimos14)
df13['URL'] = df13['URL'].apply(retornaUltimos14)
df18['URL'] = df18['URL'].apply(retornaUltimos14)
df19['URL'] = df19['URL'].apply(retornaUltimos14)

df2['URL'] = df2['URL'].apply(formata_cnpj)
df3['URL'] = df3['URL'].apply(formata_cnpj)
df5['URL'] = df5['URL'].apply(formata_cnpj)
df6['URL'] = df6['URL'].apply(formata_cnpj)
df7['URL'] = df7['URL'].apply(formata_cnpj)
df8['URL'] = df8['URL'].apply(formata_cnpj)
df9['URL'] = df9['URL'].apply(formata_cnpj)
df10['URL'] = df10['URL'].apply(formata_cnpj)
df11['URL'] = df11['URL'].apply(formata_cnpj)
df12['URL'] = df12['URL'].apply(formata_cnpj)
df13['URL'] = df13['URL'].apply(formata_cnpj)
df14['URL'] = df14['URL'].apply(formata_cnpj)
df15['URL'] = df15['URL'].apply(formata_cnpj)
df16['URL'] = df16['URL'].apply(formata_cnpj)
df17['URL'] = df17['URL'].apply(formata_cnpj)
df18['URL'] = df18['URL'].apply(formata_cnpj)
df19['URL'] = df19['URL'].apply(formata_cnpj)
df20['URL'] = df20['URL'].apply(formata_cnpj)
df21['URL'] = df21['URL'].apply(formata_cnpj)

dfTotal = df3
dfTotal = dfTotal.append(df2)
dfTotal = dfTotal.append(df4)
dfTotal = dfTotal.append(df5)
dfTotal = dfTotal.append(df6)
dfTotal = dfTotal.append(df7)
dfTotal = dfTotal.append(df8)
dfTotal = dfTotal.append(df9)
dfTotal = dfTotal.append(df10)
dfTotal = dfTotal.append(df11)
dfTotal = dfTotal.append(df12)
dfTotal = dfTotal.append(df13)
dfTotal = dfTotal.append(df14)
dfTotal = dfTotal.append(df15)
dfTotal = dfTotal.append(df17)
dfTotal = dfTotal.append(df18)
dfTotal = dfTotal.append(df19)
dfTotal = dfTotal.append(df21)

dfTotal['Len'] = dfTotal['URL'].str.len()

df_Dif18 = dfTotal[dfTotal["Len"]!=18].index
dfTotal = dfTotal.drop(df_Dif18)

dfTotal = dfTotal.drop('Len', 1)

dfTotal['Scopo'] = dfTotal['Scopo'].apply(Remover_Caracteres_Especiais)

dfTotal['Scopo'] = dfTotal['Scopo'].str.replace(".", "").str.replace("/", "").str.replace("-", "").str.replace("(", "").str.replace(")", "")

dfTotal = dfTotal.reset_index(drop=True)

for i in dfTotal.index:
    dfTotal['Scopo'][i] = Tirar_CNPJ_Scopo(dfTotal['Scopo'][i], dfTotal['URL'][i])

indexNames = dfTotal[ dfTotal['Scopo'] == 'https:wwwinformecadastralcombrcondominioedificio ' ].index
dfTotal.drop(indexNames , inplace=True)

for i in dfTotal.index:
    if dfTotal['URL'][i].replace(".", "").replace("/", "").replace("-", "").isnumeric():
        dfTotal['Scopo'][i] = Tirar_CNPJ_Int_Scopo(dfTotal['Scopo'][i], dfTotal['URL'][i])

for i in dfTotal.index:
    dfTotal['Scopo'][i] = Tirar_CNPJ_Scopo_Ate_a_Barra(dfTotal['Scopo'][i], dfTotal['URL'][i])

for i in dfTotal.index:
    dfTotal['Scopo'][i] = Tirar_CNPJ_Scopo_Split_Ponto(dfTotal['Scopo'][i], dfTotal['URL'][i])

dfTotal['Scopo'] = dfTotal['Scopo'].str.lower()

dfTotal['Scopo'] = dfTotal['Scopo'].str.replace('consulta cnpj ', '').str.replace(' - cadastro empresa', '').str.replace('cnpj', '').str.replace(' - informe cadastral', '').str.replace(' - consultas plus', '')
dfTotal['Scopo'] = dfTotal['Scopo'].str.replace(' - consulta cnpj', '').str.replace('dados da empresa', '').str.replace('endereço', '').str.replace('brasil', '').str.replace('', '').str.replace('situação cadastral', '').str.replace('', '')
dfTotal['Scopo'] = dfTotal['Scopo'].str.replace('situação', '').str.replace('cadastro empresa', '').str.replace('informe cadastral', '').str.replace('informe ', '').str.replace('consultas', '').str.replace('plus', '')
dfTotal['Scopo'] = dfTotal['Scopo'].str.replace('consulta', '').str.replace('empresas do', '')

Vazios = dfTotal[ dfTotal['Scopo'] == '' ].index

dfTotal.drop(Vazios , inplace=True)

dfTotal['Loc'] = pd.to_numeric(dfTotal['Loc'])

dfTotal['Scopo'] = dfTotal['Scopo'].str.lstrip()

writer = pd.ExcelWriter(pasta_import + 'Output_' + arquivo_import + '.xlsx', engine='xlsxwriter')

dfTotal.to_excel(writer, sheet_name='Total', index=False)
df0.to_excel(writer, sheet_name='0', index=False)
df1.to_excel(writer, sheet_name='1', index=False)
df2.to_excel(writer, sheet_name='2', index=False)
df3.to_excel(writer, sheet_name='3', index=False)
df4.to_excel(writer, sheet_name='4', index=False)
df5.to_excel(writer, sheet_name='5', index=False)
df6.to_excel(writer, sheet_name='6', index=False)
df7.to_excel(writer, sheet_name='7', index=False)
df8.to_excel(writer, sheet_name='8', index=False)
df9.to_excel(writer, sheet_name='9', index=False)
df10.to_excel(writer, sheet_name='10', index=False)
df11.to_excel(writer, sheet_name='11', index=False)
df12.to_excel(writer, sheet_name='12', index=False)
df13.to_excel(writer, sheet_name='13', index=False)
df14.to_excel(writer, sheet_name='14', index=False)
df15.to_excel(writer, sheet_name='15', index=False)
df16.to_excel(writer, sheet_name='16', index=False)
df17.to_excel(writer, sheet_name='17', index=False)
df18.to_excel(writer, sheet_name='18', index=False)
df19.to_excel(writer, sheet_name='19', index=False)
df20.to_excel(writer, sheet_name='20', index=False)
df21.to_excel(writer, sheet_name='21', index=False)

writer.save()