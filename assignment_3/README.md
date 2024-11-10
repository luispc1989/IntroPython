# Análise do Dataset de Empréstimos da Kiva

Este projeto realiza uma análise exploratória do conjunto de dados de empréstimos da Kiva, aplicando técnicas básicas de manipulação e transformação de dados usando a biblioteca `pandas` em Python. O objetivo do exercício é explorar o dataset, selecionar subconjuntos de dados com base em critérios específicos, ordenar e agrupar informações, bem como categorizar e guardar o resultado final para uso futuro.

## Estrutura e Passos do Código

1. **Importação de Bibliotecas**
   - O código inicia com a importação da biblioteca `pandas`, essencial para a manipulação de dados em Python.

2. **Carregamento do Dataset**
   - Carrega-se o ficheiro CSV do dataset da Kiva (`kiva_loans.csv`) diretamente para um DataFrame `pandas`. 
   - Inclui-se uma inspeção inicial dos dados com `head()` para visualizar as cinco primeiras linhas, e `info()` para obter uma visão geral das colunas, tipos de dados e valores nulos.

3. **Filtragem de Dados**
   - Utilizando o método `query()`, o código seleciona empréstimos concedidos no setor "Agriculture" nas Filipinas, com um valor superior a 1000. O resultado é guardado no `filtered_df`, com uma amostra das primeiras linhas impressa para verificação.

4. **Ordenação de Dados**
   - Ordena-se o dataset com base na coluna `loan_amount` em ordem decrescente, mostrando os cinco empréstimos mais altos. A tabela ordenada contém as colunas `country`, `sector` e `loan_amount`.

5. **Agrupamento e Agregação de Dados**
   - A seguir, o código agrupa os dados pelo país (`country`) e calcula três métricas principais:
     - Montante total de empréstimos por país (`total_loan_amount`)
     - Média do valor dos empréstimos por país (`average_loan_amount`)
     - Contagem de empréstimos por país (`loan_count`)
   - A amostra do resumo é apresentada, formatada com índices para facilitar a leitura.

6. **Criação de Variável com `apply()` e `lambda`**
   - Para categorizar os empréstimos, o código define a coluna `loan_size_category` com três categorias: 
     - `Small` (empréstimos abaixo de 500)
     - `Medium` (empréstimos entre 500 e 2000)
     - `Large` (empréstimos superiores a 2000)
   - Esta nova variável facilita a classificação dos empréstimos e permite análises adicionais.

7. **Gravação do DataFrame Transformado**
   - O DataFrame transformado é guardado como um novo ficheiro CSV (`kiva_loans_analysis.csv`) na mesma pasta. A gravação inclui o encoding `utf-8` e utiliza uma linha inicial para definir o separador como vírgula, o que assegura compatibilidade ao abrir o ficheiro em vários editores.

## Estrutura do Projeto

