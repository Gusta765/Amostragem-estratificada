import pandas as pd
import openpyxl 

def carregar(df_amostragem, df_amostra_final):
        
    with pd.ExcelWriter('Produtos_Auditoria.xlsx', engine='openpyxl') as writer:

        df_amostragem.to_excel(writer, sheet_name='Resumo Amostragem', index=False)

        df_amostra_final.to_excel(writer, sheet_name='Produtos Selecionados', index=False)

    print('Arquivo Excel gerado com sucesso!')