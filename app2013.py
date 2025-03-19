import pandas as pd

# Caminho do arquivo CSV
arquivo = "C:/Users/User/Documents/MASTER INSPER/PROJETO FINAL/MEDIA_RENDA_ENEM/MEDIA_RENDA_ENEM/MICRODADOS_ENEM_2013.CSV"

# Definir colunas de interesse
colunas = ["NU_NOTA_CN", "NU_NOTA_CH", "NU_NOTA_LC", "NU_NOTA_MT", "NU_NOTA_REDACAO", "Q003", "TP_FAIXA_ETARIA"]

# Criar lista para armazenar os chunks
chunks = []
chunk_size = 100000  # Número de linhas por chunk

# Ler o CSV em partes
for chunk in pd.read_csv(arquivo, sep=';', encoding='ISO-8859-1', usecols=colunas, chunksize=chunk_size, low_memory=False):
    chunk = chunk.dropna()  # Remover valores nulos
    chunk = chunk[chunk["TP_FAIXA_ETARIA"].isin([1, 2, 3, 4, 5])]  # Filtrar candidatos de até 20 anos
    chunk["MEDIA_GERAL"] = chunk[["NU_NOTA_CN", "NU_NOTA_CH", "NU_NOTA_LC", "NU_NOTA_MT", "NU_NOTA_REDACAO"]].mean(axis=1)
    chunks.append(chunk)

# Concatenar todos os chunks
df = pd.concat(chunks, ignore_index=True)

# Calcular a média por faixa de renda
media_por_renda = df.groupby("Q003")["MEDIA_GERAL"].mean().reset_index()

# Exibir os resultados
print(media_por_renda)

# Salvar em CSV
media_por_renda.to_csv("media_renda_2013.csv", index=False, sep=";")