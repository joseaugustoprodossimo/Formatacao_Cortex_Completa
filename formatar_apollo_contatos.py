import pandas as pd
import funcoes

def apollo_contatos(df):
    df = df.filter(items=['Website','First Name', 'Last Name', 'Title','Email', 'Industry', 'Person Linkedin Url','Technologies','Keywords', 'SEO Description', 'Company Linkedin Url','Facebook Url', 'Twitter Url', 'Technologies', 'First Phone'])
    df.rename({'Website':'WEBSITE','First Name':'PRIMEIRO NOME','Last Name':'ULTIMO NOME','Title':'CARGO B2B','Email':'E-MAIL','Person Linkedin Url':'LINKEDIN URL','Technologies':'TECNOLOGIAS'}, axis = 1, inplace = True)
    df['WEBSITE'] = df['WEBSITE'].apply(funcoes.Formatar_sites)
    df['LINKEDIN URL'] = df['LINKEDIN URL'].apply(funcoes.Formatar_sites)
    df['Facebook Url'] = df['Facebook Url'].apply(funcoes.Formatar_sites)
    df['Twitter Url'] = df['Twitter Url'].apply(funcoes.Formatar_sites)
    df['Company Linkedin Url'] = df['Company Linkedin Url'].apply(funcoes.Formatar_sites)
    return df