import pandas as pd
import validar_url_likedin_docket as valida_linkedin
import juntar_tecnologias
import formatar_apollo_contatos
import formatar_apollo_empresas
import formatar_ddplus_contatos
import formatar_ddplus_contatos_empresas
import formatar_ddplus_linkedin
import formatar_ddplus_linkedin_empresas
import formatar_ddplus_receita_federal_empresas
import formatar_ddplus_receita_federal_socios
import formatar_e_juntar_contatos_apollo_ddplus
import funcoes

caminho = 'E:\\Python\\Juntar Dados Cadastrais e Contatos\\'
DadosCadastrais = 'BR2 - Enriquecimento Cliente - DB - Cortex'

df_dados_cadastrais = pd.read_excel(
    'E:\\Python\\Juntar Dados Cadastrais e Contatos\\' + 
    'BR2 - Enriquecimento Cliente - DB - Cortex' + 
    '.xlsx', 
    sheet_name='Dados Cadastrais - Cortex'
)

df_apollo_contatos = pd.read_csv(
    'E:\\Python\\Apollo Tratamentos\\' +
    'apollo-contacts-export.csv'
)

df_apollo_contatos = formatar_apollo_contatos.apollo_contatos(df_apollo_contatos)

print(df_apollo_contatos)

df_matriz_cnpj_website = pd.read_excel(caminho + DadosCadastrais + '.xlsx', sheet_name='Matriz CNPJ Website')
df_DQ = pd.read_excel(caminho + DadosCadastrais + '.xlsx', sheet_name='DQ')

valida_linkedin.validar_url_linkedin()

juntar_tecnologias.juntar_tec()