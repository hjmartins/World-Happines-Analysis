import pandas as pd

# Lê o arquivo CSV
df = pd.read_csv('data/2017.csv')
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
# Salva novamente sem o índice
df.to_csv('2017no.csv', index=False)