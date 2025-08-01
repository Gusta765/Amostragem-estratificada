import arquivos
import extract
import transform 
import load 

arquivos.gera_arquivo()

df_produtos = extract.extrair('produtos_aleatorios.csv')

df = transform.tratamento(df_produtos)

df_amostragem = transform.amostragem_simples(df)

df_amostra_final = transform.selecionar_amostra_por_categoria(df_produtos, df_amostragem)

load.carregar(df_amostragem, df_amostra_final)

print(df_amostra_final)
print(df_amostragem)