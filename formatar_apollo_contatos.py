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
    df['CARGO B2B'] = df['CARGO B2B'].str.title()
    
    for i in df.index:
      if df['PRIMEIRO NOME'][i] == "":
        df['PRIMEIRO NOME'][i] = df['ULTIMO NOME'][i]
        df['ULTIMO NOME'][i] = ""

    return df

if(__name__ == "__main__"):

  pasta_import = "C:\\Projetos\\Python\\Apollo\\"
  arquivo_import = "apollo-contacts-export"

  df = pd.read_csv(pasta_import + arquivo_import + ".csv", converters={'First Name': lambda x: str(x),
                                                                     'Last Name': lambda x: str(x),
                                                                     'Title': lambda x: str(x),
                                                                     'Company': lambda x: str(x),
                                                                     'Company Name for Emails': lambda x: str(x),
                                                                     'Email': lambda x: str(x),
                                                                     'Email Status': lambda x: str(x),
                                                                     'Email Confidence': lambda x: str(x),
                                                                     'Contact Owner': lambda x: str(x),
                                                                     'First Phone': lambda x: str(x),
                                                                     'Work Direct Phone': lambda x: str(x),
                                                                     'Home Phone': lambda x: str(x),
                                                                     'Mobile Phone': lambda x: str(x),
                                                                     'Corporate Phone': lambda x: str(x),
                                                                     'Other Phone': lambda x: str(x),
                                                                     'Stage': lambda x: str(x),
                                                                     'Lists': lambda x: str(x),
                                                                     'Last Contacted': lambda x: str(x),
                                                                     'Account Owner': lambda x: str(x),
                                                                     '# Employees': lambda x: str(x),
                                                                     'Industry': lambda x: str(x),
                                                                     'Keywords': lambda x: str(x),
                                                                     'Person Linkedin Url': lambda x: str(x),
                                                                     'Website': lambda x: str(x),
                                                                     'Company Linkedin Url': lambda x: str(x),
                                                                     'Facebook Url': lambda x: str(x),
                                                                     'Twitter Url': lambda x: str(x),
                                                                     'City': lambda x: str(x),
                                                                     'State': lambda x: str(x),
                                                                     'Country': lambda x: str(x),
                                                                     'Company Address': lambda x: str(x),
                                                                     'Company City': lambda x: str(x),
                                                                     'Company State': lambda x: str(x),
                                                                     'Company Country': lambda x: str(x),
                                                                     'Company Phone': lambda x: str(x),
                                                                     'SEO Description': lambda x: str(x),
                                                                     'Technologies': lambda x: str(x),
                                                                     'Annual Revenue': lambda x: str(x),
                                                                     'Total Funding': lambda x: str(x),
                                                                     'Latest Funding': lambda x: str(x),
                                                                     'Latest Funding Amount': lambda x: str(x),
                                                                     'Last Raised At': lambda x: str(x),
                                                                     'Email Sent': lambda x: str(x),
                                                                     'Email Open': lambda x: str(x),
                                                                     'Email Bounced': lambda x: str(x),
                                                                     'Replied': lambda x: str(x),
                                                                     'Demoed': lambda x: str(x),
                                                                     'Number of Retail Locations': lambda x: str(x),
                                                                     'Apollo Contact Id': lambda x: str(x),
                                                                     'Apollo Account Id': lambda x: str(x)
                                                                     })

  df = apollo_contatos(df)

  writer = pd.ExcelWriter(pasta_import + 'Output_' + arquivo_import + '.xlsx', engine='xlsxwriter',options={'strings_to_urls': False})
  df.to_excel(writer)
  writer.close()
  print('Finalizado')

  #arquivo_export = 'Output ' + arquivo_import + '.xlsx'
  #df.to_excel(pasta_import + arquivo_export, index = False)