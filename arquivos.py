import pandas as pd
import random
from faker import Faker

def gera_arquivo():
    fake = Faker('pt_BR')

    NUM_PRODUTOS = 10000
    CATEGORIAS = ['Alimentos', 'Higiene', 'Limpeza']

    PESOS = [0.60, 0.30, 0.10] 

    BASES_PRODUTOS = ['Sabão em Pó', 'Detergente', 'Arroz', 'Feijão', 'Shampoo', 'Creme Dental', 'Macarrão', 'Óleo', 'Desinfetante', 'Condicionador']
    ADJETIVOS = ['Premium', 'Light', 'Tradicional', 'Orgânico', 'Sem Glúten', '500g', 'Refil', 'Aromatizado', 'Integral', '1kg']

    print("Gerando novo arquivo de produtos com distribuição desigual...")

    lista_de_produtos = []
    for i in range(1, NUM_PRODUTOS + 1):

        categoria_escolhida = random.choices(CATEGORIAS, weights=PESOS, k=1)[0]
        
        descricao_aleatoria = f"{random.choice(BASES_PRODUTOS)} {random.choice(ADJETIVOS)}"
        
        lista_de_produtos.append({
            'PRODUTOS': i,
            'DESCRICAO': descricao_aleatoria,
            'CATEGORIA': categoria_escolhida
        })

    df_novo = pd.DataFrame(lista_de_produtos)

    novo_caminho_csv = 'produtos_aleatorios.csv'

    df_novo.to_csv(novo_caminho_csv, index=False)

    return print('Arquivo gerado com sucesso!')