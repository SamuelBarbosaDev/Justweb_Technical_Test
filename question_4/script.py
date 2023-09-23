import pandas as pd

# Substitua 'seuarquivo.xlsx' pelo nome do seu arquivo Excel
path = r'../data/Tabela financeiro - teste Python pleno.xlsx'

# Carregue o arquivo Excel em um DataFrame do pandas
df = pd.read_excel(path)

# Substitua 'Tabela financeiro - teste Python pleno.csv'
# pelo nome que você deseja para o arquivo CSV
csv_file = r'../data/Tabela financeiro - teste Python pleno.csv'

# Salve o DataFrame em um arquivo CSV
df.to_csv(csv_file, index=False)
