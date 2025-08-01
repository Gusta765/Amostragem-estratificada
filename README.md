# 📊 Amostragem Estratificada para Auditoria de Produtos

## 📖 Descrição

Este projeto implementa um pipeline de **ETL (Extract, Transform, Load)** em Python para realizar **amostragem estratificada** em um grande catálogo de produtos. O objetivo é selecionar uma amostra estatisticamente representativa que possa ser usada para fins de auditoria, controle de qualidade ou análise de dados, garantindo que todas as categorias de produtos, mesmo as menores, sejam devidamente representadas.

O sistema primeiro gera um conjunto de dados sintético e desbalanceado, simulando um cenário real. Em seguida, calcula o tamanho de amostra necessário para cada categoria (estrato) com base em parâmetros estatísticos (nível de confiança e margem de erro) e, por fim, extrai a amostra e a salva em um relatório Excel.

---

## 🔗 Contexto e Evolução do Projeto

Este trabalho é a segunda fase de uma iniciativa de engenharia de dados. Ele representa a evolução natural do projeto anterior, que focava na limpeza e padronização de dados.

* **Fase 1: [Classificador de Produtos com Levenshtein](https://github.com/Gusta765/Classificando-Produtos-Levenshtein-)**
    * **Problema:** Lidar com descrições de produtos não padronizadas e duplicadas.
    * **Solução:** Um pipeline ETL que usa a Distância de Levenshtein para encontrar e classificar produtos com descrições similares.
    * **Resultado:** Uma base de dados mais limpa e organizada.

* **Fase 2: Amostragem Estratificada para Auditoria (Este Projeto)**
    * **Problema:** Como validar a qualidade dos dados em um catálogo massivo sem precisar verificar todos os itens?
    * **Solução:** Um pipeline ETL que aplica amostragem estratificada para selecionar um subconjunto de produtos que seja representativo de todo o catálogo.
    * **Resultado:** Uma amostra confiável para auditoria, economizando tempo e recursos.

---

## ✨ Funcionalidades Principais

* **Geração de Dados Sintéticos:** Utiliza a biblioteca `Faker` para criar um arquivo `.csv` com 10.000 produtos distribuídos de forma desigual em categorias, simulando um ambiente de produção.
* **Cálculo de Amostra Estatística:** Calcula o tamanho de amostra necessário para cada categoria usando a fórmula de amostragem para populações finitas, permitindo a configuração de nível de confiança e margem de erro.
* **Amostragem Estratificada:** Garante que a amostra final contenha um número proporcional e estatisticamente relevante de itens de cada categoria, evitando o viés que ocorreria em uma amostragem aleatória simples.
* **Pipeline ETL Estruturado:** O código é organizado nas etapas clássicas de Extração, Transformação e Carga.
* **Relatório em Excel:** Gera um arquivo `.xlsx` com duas abas:
    1.  `Resumo Amostragem`: Mostra o total de produtos por categoria e o tamanho da amostra calculada para cada uma.
    2.  `Produtos Selecionados`: Contém a lista final de produtos selecionados para a auditoria.

---

## 💡 A Lógica por Trás da Amostragem Estratificada

Em um conjunto de dados onde as categorias (estratos) têm tamanhos muito diferentes, uma amostragem aleatória simples poderia facilmente sub-representar ou até ignorar completamente as categorias menores.

A **amostragem estratificada** resolve isso tratando cada categoria como uma subpopulação independente. O processo é:

1.  **Estratificação:** O conjunto de dados é dividido em grupos (estratos) com base na coluna `CATEGORIA`.
2.  **Cálculo do Tamanho:** Para cada estrato, a fórmula abaixo calcula o tamanho de amostra (`n`) necessário, corrigido para o tamanho da população (`N`) daquele estrato.
    ```
    n = n0 / (1 + (n0 - 1) / N)
    onde n0 = (Z² * p * (1-p)) / e²
    ```
3.  **Seleção:** Uma amostra aleatória simples é retirada de *dentro* de cada estrato, com o tamanho calculado no passo anterior.
4.  **Combinação:** As amostras de cada estrato são unidas para formar a amostra final.

Isso garante que a amostra final seja um "mini-universo" do conjunto de dados original.

---

## 🚀 Como Usar

### Pré-requisitos

* Python 3.8+
* Bibliotecas: `pandas`, `faker`, `openpyxl`

### Instalação

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/Gusta765/seu-novo-repositorio.git](https://github.com/Gusta765/seu-novo-repositorio.git)
    cd seu-novo-repositorio
    ```

2.  **Instale as dependências:**
    (Recomenda-se criar um ambiente virtual)
    ```bash
    pip install pandas faker openpyxl
    ```

### Execução

Para rodar o pipeline completo, basta executar o script `main.py`:

```bash
python main.py
```

O script irá:
1.  Gerar o arquivo `produtos_aleatorios.csv`.
2.  Processar os dados e realizar a amostragem.
3.  Salvar o resultado final no arquivo `Produtos_Auditoria.xlsx`.
4.  Imprimir os DataFrames de resumo e da amostra final no terminal.

---

## 🛠️ Estrutura do Projeto

```
.
├── main.py             # Orquestrador do pipeline ETL
├── arquivos.py         # Script para gerar o dataset sintético
├── config.py           # Parâmetros estatísticos para o cálculo da amostra
├── extract.py          # Função para carregar os dados do CSV
├── transform.py        # Funções para realizar a amostragem estratificada
└── load.py             # Função para salvar o relatório final em Excel

### 📫 Contato

[![LinkedIn](https://img.shields.io/badge/-LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/gustavo-barbosa-868976236/) [![Email](https://img.shields.io/badge/Email-gustavobarbosa7744@gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:gustavobarbosa7744@gmail.com)
