
# Apache Spark – Visão Geral e Guia de Aprendizagem

##  Tópico 1: O que é o Apache Spark?
- **Explicação Tópico 1**  
  Apache Spark é um mecanismo unificado de análise para processamento de dados em larga escala. Oferece APIs de alto nível em Java, Scala, Python e R, com um engine otimizado que suporta gráficos de execução gerais. Também inclui ferramentas como Spark SQL, pandas API no Spark, MLlib, GraphX e Structured Streaming ([spark.apache.org](https://spark.apache.org/docs/latest/?utm_source=chatgpt.com)).

- **Exercício simples**  
  Escreva um pequeno script em PySpark que crie uma DataFrame a partir de um array de tuplas contendo (nome, idade) e exiba o conteúdo com `.show()`.

- **Exercício avançado**  
  Crie um pipeline que leia um arquivo CSV de usuários (nome, idade, renda), filtre por renda > 5000, agregue por faixa etária e exporte o resultado em formato parquet usando DataFrame API.

##  Tópico 2: Quick Start / Shell Interativo
- **Explicação Tópico 2**  
  Spark oferece shells interativos em Scala (`spark-shell`) e Python (`pyspark`) que permitem explorar o API em tempo real. Desde Spark 2.0, o foco é usar `Dataset` (em Scala/Java) ou `DataFrame` (que é um alias de `Dataset[Row]` em Python) em vez de RDDs, por oferecerem melhores otimizações ([spark.apache.org](https://spark.apache.org/docs/latest/quick-start.html?utm_source=chatgpt.com)).

- **Exercício simples**  
  No `pyspark`, crie um `DataFrame` a partir de uma lista de dicionários com "nome" e "idade", mostre seu schema com `.printSchema()` e visualize os dados com `.show()`.

- **Exercício avançado**  
  No `spark-shell`, crie um Dataset de pessoas, filtre por idade > 30, faça cache do resultado e conte o número de elementos, comparando performance antes e depois de usar `.cache()`.

##  Tópico 3: RDDs – Resilient Distributed Datasets
- **Explicação Tópico 3**  
  RDDs são coleções distribuídas tolerantes a falhas, fundamentais desde a origem do Spark. Podem ser criados a partir de coleções locais ou arquivos externos, e permitem operações paralelas com transformações e ações ([spark.apache.org](https://spark.apache.org/docs/latest/rdd-programming-guide.html?utm_source=chatgpt.com)).

- **Exercício simples**  
  Use `sc.parallelize([1, 2, 3, 4, 5])` em PySpark, aplique `reduce` para somar os valores e exiba o resultado.

- **Exercício avançado**  
  Carregue um arquivo de texto (por exemplo, `textFile`) como RDD, conte quantas linhas contêm uma palavra específica (ex: “erro”), usando `filter` e `count`.

##  Tópico 4: Spark SQL, DataFrames e Datasets
- **Explicação Tópico 4**  
  - **DataFrames**: coleções distribuídas com colunas nomeadas, equivalentes a tabelas SQL, disponíveis em Python, Scala, Java e R.  
  - **Datasets**: disponíveis em Scala e Java, são coleções distribuídas fortemente tipadas, com as vantagens do RDD e otimizações do Spark SQL.

- **Exercício simples**  
  Crie um DataFrame com colunas "nome", "idade", filtrando por idade > 25 e exiba o resultado.

- **Exercício avançado**  
  Utilize `spark.sql()` para criar uma view temporária a partir de um DataFrame, execute uma consulta SQL agregando salários e filtre pela média de idade.

##  Tópico 5: Structured Streaming vs Spark Streaming (DStreams)
- **Explicação Tópico 5**  
  - **Spark Streaming (DStreams)**: sistema legado baseado em micro-batches, trabalhando com DStreams – sequências de RDDs.  
  - **Structured Streaming**: API moderna para streaming baseado em DataFrames/Datasets, mais segura e recomendada para uso atual.

- **Exercício simples**  
  Monte um `Structured Streaming` simples que lê texto de um socket TCP e imprime as linhas recebidas.

- **Exercício avançado**  
  Use `Structured Streaming` para ler de Kafka, aplicar um agregador por janela de tempo (window), e escrever o resultado em um sink como console ou arquivo parquet.

##  Tópico 6: MLlib – Machine Learning
- **Explicação Tópico 6**  
  MLlib é a biblioteca de aprendizado de máquina do Spark, com algoritmos distribuídos como regressão, classificação, clustering, filtragem colaborativa, redução de dimensionalidade, entre outros.

- **Exercício simples**  
  Use MLlib no PySpark para treinar um classificador de regressão logística com dados sintéticos (ex: label e features), e avalie a acurácia no conjunto de teste.

- **Exercício avançado**  
  Monte um pipeline com `VectorAssembler`, `StringIndexer`, `RandomForestClassifier`, treine com dados de CSV, e salve o modelo treinado em disco.

##  Tópico 7: GraphX – Processamento de Grafos
- **Explicação Tópico 7**  
  GraphX é a API para processamento distribuído de grafos, disponível em Scala/Java. Permite expressar cálculos em grafos, baseados no modelo Pregel, com otimizações próprias.

- **Exercício simples**  
  Em Scala, crie um grafo com três vértices e arestas, e calcule o número de conexões por vértice.

- **Exercício avançado**  
  Implemente o algoritmo PageRank usando GraphX em um grafo de superfície média, e exiba os principais vértices por ranking.

##  Tópico 8: Spark Connect
- **Explicação Tópico 8**  
  Spark Connect é uma nova arquitetura cliente-servidor: permite que aplicativos PySpark ou Scala se conectem remotamente a um servidor Spark, com benefícios operacionais como estabilidade isolada, atualizações independentes e melhor observabilidade.

- **Exercício simples**  
  Inicie um servidor Spark Connect local com `./sbin/start-connect-server.sh`, execute `pyspark --remote "sc://localhost"` e crie um DataFrame simples.

- **Exercício avançado**  
  Implemente um cliente que se conecta ao Spark Connect, envia consultas via DataFrame/Dataset e captura logs ou métricas para monitoramento personalizado.

##  Tópico 9: Cluster Mode – Execução em Cluster
- **Explicação Tópico 9**  
  O Spark pode rodar em clusters com diferentes gerenciadores como Standalone, YARN ou Kubernetes. O `SparkContext` coordena a execução, requisita executors e distribui tarefas.

- **Exercício simples**  
  Execute um job local com `--master local[2]`, conte o número de partições, e observe a distribuição.

- **Exercício avançado**  
  Submeta uma aplicação com `spark-submit` para um cluster YARN ou Kubernetes, configure recursos (CPU, memória), e monitore performance via UI.

---

