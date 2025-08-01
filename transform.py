import pandas as pd
import config as c

def tratamento(df) -> pd.DataFrame | None:

    df = df[['CATEGORIA', 'PRODUTOS']]

    df = df.groupby(['CATEGORIA']).count().reset_index()

    return df

def amostragem_simples(df, Z=c.Z, p=c.p, e=c.e) -> pd.DataFrame | None:

    n0 = (Z**2 * p * (1 - p)) / (e**2)

    df["AMOSTRA_NECESSARIA"] = df["PRODUTOS"].apply(
        lambda N: round(n0 / (1 + ((n0 - 1) / N))) if N > 50 else N
    )
    
    return df

def selecionar_amostra_por_categoria(df_produtos, df_amostragem) -> pd.DataFrame | None:
    
    lista_de_amostras = []

    for _, linha in df_amostragem.iterrows():
        categoria = linha['CATEGORIA']
        tamanho_amostra = linha['AMOSTRA_NECESSARIA']
        
        print(f"  - Categoria: {categoria}, Sorteando: {tamanho_amostra} produtos")

        produtos_da_categoria = df_produtos[df_produtos['CATEGORIA'] == categoria]
        
        amostra_da_categoria = produtos_da_categoria.sample(
            n=tamanho_amostra, 
            random_state=42
        )
        
        lista_de_amostras.append(amostra_da_categoria)

    df_final_amostra = pd.concat(lista_de_amostras)
    
    print("\nAmostragem aleatória concluída!")
    return df_final_amostra