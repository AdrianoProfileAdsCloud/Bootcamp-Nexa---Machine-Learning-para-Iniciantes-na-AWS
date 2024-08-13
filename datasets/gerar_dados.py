import pandas as pd
import random
from datetime import datetime, timedelta

# Parâmetros
num_records = 600
start_date = datetime(2022, 1, 1)
end_date = datetime(2024, 8, 12)
product_names = ['Arroz', 'Feijão', 'Macarrão', 'Leite', 'Açúcar', 'Sal', 'Café', 'Óleo', 'Farinha', 'Milho']

# Funções auxiliares
def random_date(start, end):
    """Gera uma data aleatória entre start e end."""
    return start + timedelta(days=random.randint(0, int((end - start).days)))

def generate_record(id_produto):
    nome_produto = random.choice(product_names)
    preco_produto = round(random.uniform(1.0, 10.0), 2)
    qtd_em_estoque = random.randint(50, 200)
    qtd_produto_vendido = random.randint(0, 10)
    produto_em_promocao = random.choice(['SIM', 'NÃO'])
    qtd_dias_em_promocao = random.randint(0, 30) if produto_em_promocao == 'SIM' else 0
    data_compra = random_date(start_date, end_date).strftime('%Y-%m-%d')

    return {
        "ID_PRODUTO": id_produto,
        "NOME_DO_PRODUTO": nome_produto,
        "PRECO_PRODUTO": preco_produto,
        "QTD_EM_ESTOQUE": qtd_em_estoque,
        "QTD_PRODUTO_VENDIDO": qtd_produto_vendido,
        "PRODUTO_EM_PROMOCAO": produto_em_promocao,
        "QTD_DIAS_EM_PROMOCAO": qtd_dias_em_promocao,
        "DATA_COMPRA": data_compra,
    }

# Geração dos registros
data = []
id_produto = 1

while len(data) < num_records:
    for _ in range(10):
        record = generate_record(id_produto)
        data.append(record)
        id_produto += 1
        
        # Atualiza estoque baseado nas vendas
        record['QTD_EM_ESTOQUE'] -= record['QTD_PRODUTO_VENDIDO']
        record['QTD_EM_ESTOQUE'] = max(0, record['QTD_EM_ESTOQUE'])  # Garante que não seja negativo

# Criar DataFrame
df = pd.DataFrame(data)

# Exportar para CSV
csv_path = r'C:\\Users\\Adriano Aparecido\\Desktop\\dataset_produtos.csv'
df.to_csv(csv_path, index=False)

csv_path
