import pandas as pd
import validar_url_likedin_docket as valida_linkedin
import juntar_tecnologias

caminho = 'E:\\Python\\Juntar Dados Cadastrais e Contatos\\'
DadosCadastrais = 'BR2 - Enriquecimento Cliente - DB - Cortex'

df_dados_cadastrais = pd.read_excel(
    'E:\\Python\\Juntar Dados Cadastrais e Contatos\\' + 
    'BR2 - Enriquecimento Cliente - DB - Cortex' + 
    '.xlsx', 
    sheet_name='Dados Cadastrais - Cortex'
)




df_matriz_cnpj_website = pd.read_excel(caminho + DadosCadastrais + '.xlsx', sheet_name='Matriz CNPJ Website')
df_DQ = pd.read_excel(caminho + DadosCadastrais + '.xlsx', sheet_name='DQ')

valida_linkedin.validar_url_linkedin()

juntar_tecnologias.juntar_tec()