import pandas as pd

# Carregando os dados
df = pd.read_csv('data/call_center_data.csv')

# Cálculos de Engenharia de Dados
tma = (df['Tempo_Falado_Seg'].mean() + df['Tempo_ACW_Seg'].mean()) / 60
tme_medio = df['Tempo_Espera_Seg'].mean()

print("-" * 30)
print("📊 RELATÓRIO AUTOMATIZADO - MIS")
print("-" * 30)
print(f"Tempo Médio de Atendimento (TMA): {tma:.2f} minutos")
print(f"Tempo Médio de Espera (TME): {tme_medio:.2f} segundos")
print(f"Total de Chamados Analisados: {len(df)}")
print("-" * 30)

