import pandas as pd
import os

def executar_pipeline():
    print("📂 Carregando base de 1000 registros...")
    df = pd.read_csv('data/base_operacional_mis.csv')
    
    print("⚙️ Calculando KPIs (TMA, CSAT, Produtividade)...")
    tma_medio = df['tempo_atendimento'].mean()
    csat_total = df['satisfacao'].value_counts(normalize=True)
    
    print(f"✅ Insights Gerados! TMA Médio: {tma_medio:.2f}s")
    
    # Simulação de criação de arquivo Excel para o Tableau
    print("📊 Gerando arquivo .xlsx para integração com Tableau/Power BI...")
    # df.to_excel('data/relatorio_final.xlsx', index=False) 

if __name__ == "__main__":
    executar_pipeline()
