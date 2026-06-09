import pandas as pd
import numpy as np

# =================
# CARREGAR CSV 
# =================

df = pd.read_csv('drinks.csv')

# =================
# RENOMEAR COLUNAS
# =================

df.columns = [
    'Pais',
    'Cerveja',
    'Destilados',
    'Vinho',
    'LitrosAlcool' 
]
# =====================
# VISUALIZAÇÃO INICIAL
# =====================

print('=== PRIMEIRAS 5 LINHAS ===')
print(df.head())

print('\n=== INFORMAÇÕES DO DATAFRAME ===')
print(df.info())

print('\n=== ESTATISTICAS GERAIS ===')
print(df.describe())

# =======================
# ESTATÍSTICAS COM NUMPY
# =======================

print('\n=== ESTATISTICAS DE CERVEJA ===')
print(f"Média: {np.mean(df['Cerveja']):.2f}")
print(f"Mediana: {np.median(df['Cerveja']):.2f}")
print(f"Maior Consumo: {np.max(df['Cerveja']):.2f}")
print(f"Menor Consumo: {np.min(df['Cerveja']):.2f}")
print(f"Desvio Padrão: {np.std(df['Cerveja']):.2f}")

# =====================
# TOP 10 CERVEJA
# =====================

print("\n=== TOP 10 PAISES QUE MAIS CONSOMEM CERVEJA ===")
top10 = df.nlargest(10, 'Cerveja')
print(
    top10[
        ["Pais", "Cerveja"]
        ]
)

# =====================
# TOP 10 VINHO
# =====================

print("\n=== TOP 10 PAISES QUE MAIS CONSOMEM VINHO ===")
top10 = df.nlargest(10, 'Vinho')
print(
    top10[
        ["Pais", "Vinho"]
    ]    
)

# =====================
# FILTROS
# =====================

mediaAlcool = df['LitrosAlcool'].mean()
print('\n=== ACIMA DA MEDIA DE ALCOOL ===')
print(
    df[df["LitrosAlcool"] > mediaAlcool][["Pais", "LitrosAlcool"]]
)

# =====================
# NOVA COLUNA TOTAL
# =====================

df['TotalBebidas'] = (
    df['Cerveja'] + 
    df['Destilados'] +
    df['Vinho']
)
print('\n=== TOTAL DE BEBIDAS ===')
print(df[['Pais', 'TotalBebidas']].head())

# =========================
# CLASIFICAÇÃO COM O NUMPY
# =========================

condicoes = [
    df['LitrosAlcool'] < 2,
    df['LitrosAlcool'] < 5,
    df['LitrosAlcool'] < 8,
    df['LitrosAlcool'] >= 8    
]

categorias = [
    "Muito Baixo",
    "Baixo",
    "Médio",
    "Alto"    
]

# Select tem que ter default. Ele pega o primeiro de consumo se der ok, e cruza com o primeiro de categorias

df ["NivelConsumo"] = np.select(
    condicoes,
    categorias,
    default = "Não informado"   
)

print('\n=== CLASSIFICAÇÃO DE CONSUMO ===')

print(
    df[
        ["Pais", "LitrosAlcool", "NivelConsumo"]     
       ].head(20)
)

# =========================
# CONTAGEM POR CATEGORIA
# =========================

print('\n=== QUANTIDADE DE PAISES POR NIVEL ===')
print(df["NivelConsumo"].value_counts())

# =========================
# PAIS COM MAIOR CONSUMO TOTAL
# =========================

# =========================
# ACIMA DA MÉDIA EM TUDO 
# =========================

# =========================
# CORRELAÇÃO
# =========================

# =========================
# 
# =========================