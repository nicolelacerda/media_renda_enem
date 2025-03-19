import pandas as pd

# Carregar os dados
file_path = "C:/Users/User/Documents/MASTER INSPER/PROJETO FINAL/MEDIA_RENDA_ENEM/MEDIA_RENDA_ENEM/MICRODADOS_ENEM_2023.CSV"
df = pd.read_csv(file_path, sep=';', encoding='ISO-8859-1')

# Selecionar apenas as colunas necessárias
colunas = ["Q006", "TP_FAIXA_ETARIA", "NU_NOTA_CN", "NU_NOTA_CH", "NU_NOTA_LC", "NU_NOTA_MT", "NU_NOTA_REDACAO"]
df = df[colunas]

# Filtrar candidatos com até 20 anos
df = df[df["TP_FAIXA_ETARIA"].isin([1, 2, 3, 4, 5])]

# Remover valores nulos
df = df.dropna()

# Calcular a média das cinco provas
df["MEDIA_GERAL"] = df[["NU_NOTA_CN", "NU_NOTA_CH", "NU_NOTA_LC", "NU_NOTA_MT", "NU_NOTA_REDACAO"]].mean(axis=1)

# Calcular a média por faixa de renda
media_por_renda = df.groupby("Q006")["MEDIA_GERAL"].mean().reset_index()

# Ordenar as faixas de renda conforme a sequência das letras
ordem_renda = list("ABCDEFGHIJKLMNOPQ")
media_por_renda["Q006"] = pd.Categorical(media_por_renda["Q006"], categories=ordem_renda, ordered=True)
media_por_renda = media_por_renda.sort_values("Q006")

# Salvar os resultados em um arquivo CSV
media_por_renda.to_csv("media_renda_2023.csv", index=False, sep=';')

# Exibir os resultados
print(media_por_renda)