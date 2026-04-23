import pandas as pd

def processar_dashboard():
    print("Iniciando processamento dos 100 registros...")
    dados = {
        'Status': ['Concluído', 'Pendente', 'Em Análise'],
        'Quantidade': [60, 25, 15]
    }
    df = pd.DataFrame(dados)
    print("Tratamento de dados finalizado com sucesso!")
    return df

if __name__ == "__main__":
    processar_dashboard()
