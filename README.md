# Comparação de desempenho — Pandas vs PySpark Pandas

O objetivo deste experimento é comparar o **tempo de leitura** de um arquivo `clientes.json` contendo **10 milhões de linhas** (aproximadamente **661 MB**) utilizando as bibliotecas **Pandas** e **PySpark Pandas** (*pandas-on-Spark*).

---

## ⚙️ Ambiente de execução

Os testes foram realizados em **máquina local**, com as seguintes especificações:

- **Processador:** Intel Core i5 (12 threads)  
- **Memória RAM:** 16 GB  
- **Sistema:** Linux  
- **Arquivo de entrada:** `clientes.json` (~661 MB, 10 milhões de registros, formato JSON com `lines=True`)

---

## 🧪 Metodologia

O tempo total foi medido utilizando a função `time.time()`, considerando desde o início da leitura até a criação completa do DataFrame.

### Leitura com Pandas

```python
import pandas as pd
import time

start = time.time()
df_pandas = pd.read_json("clientes.json", lines=True)
print(f"Tempo (Pandas): {time.time() - start:.2f} segundos")
```

### Leitura com PySpark Pandas

```python
import pyspark.pandas as ps
import time
from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("Comparacao_Pandas_PySparkPandas")
    .config("spark.sql.execution.arrow.pyspark.enabled", "true")
    .config("spark.sql.ansi.enabled", "false")
    .getOrCreate()
)

start = time.time()
df_ps = ps.read_json("clientes.json", lines=True)
print(f"Tempo (PySpark Pandas): {time.time() - start:.2f} segundos")
```

---

## 📊 Resultados obtidos

| Biblioteca         | Tempo de leitura | Diferença relativa | Observações |
|--------------------|------------------|--------------------|--------------|
| **Pandas**         | 18,71 s | — | Processamento sequencial em memória |
| **PySpark Pandas** | **1,81 s** | **~10,3× mais rápido** | Aproveitou o paralelismo das 12 threads via Spark |

---

## 🧠 Análise

Mesmo com um arquivo de apenas 661 MB, o **PySpark Pandas** apresentou desempenho muito superior.  
Isso ocorre porque o **Spark** divide automaticamente o trabalho em várias partições e executa a leitura de forma **paralela**, enquanto o **Pandas** utiliza apenas um núcleo da CPU.  

Além disso, a ativação do **Apache Arrow** (`spark.sql.execution.arrow.pyspark.enabled=true`) reduziu a sobrecarga de conversão entre Spark e Pandas, otimizando ainda mais a leitura.

---

## 🧩 Conclusão

- O **Pandas** continua sendo uma opção simples e eficiente para arquivos pequenos e médios.  
- Entretanto, mesmo em um **ambiente local**, o **PySpark Pandas** demonstrou ganhos expressivos de desempenho graças ao **processamento paralelo**.  
- Esse resultado evidencia que o **Spark** pode ser vantajoso não apenas em clusters, mas também em **máquinas multicore** com hardware moderno.
