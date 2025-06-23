import pandas as pd
import glob
import os
# Caminho dos arquivos .csv
caminho = "data/"  # substitua pelo caminho onde estão seus arquivos
arquivos = sorted(glob.glob(caminho + "*.csv"))

# Lista para armazenar os DataFrames
dfs = []

# Loop para ler e juntar os arquivos
for arquivo in arquivos:
    ano = os.path.basename(arquivo).split(".")[0]  # extrai o nome do arquivo como ano
    df = pd.read_csv(arquivo)
    df["year"] = int(ano)
    dfs.append(df)

# Concatena todos os DataFrames
df_final = pd.concat(dfs, ignore_index=True)

# Padroniza nomes de colunas
df_final.columns = [col.strip().lower().replace(" ", "_") for col in df_final.columns]

# Ordena por país e ano
df_final = df_final.sort_values(by=["country", "year"])

# Salva como CSV unificado
df_final.to_csv("world_happiness_2015_2023.csv", index=False)

print("Dados unidos e salvos como 'world_happiness_2015_2023.csv'")