#%%

from pyspark.sql import SparkSession
import time
import pyspark.pandas as pd
builder = SparkSession.builder.appName("etl-pandas-json")
builder = builder.config("spark.sql.execution.arrow.pyspark.enabled", "true").config("spark.sql.ansi.enabled", "false")
builder.getOrCreate()
print(builder)

# %%

users_data = "./data/clientes.json"

# %%
start = time.time()
pd_clientes = pd.read_json(users_data, lines=True)
print(f"Tempo pyspark.pandas: {time.time() - start:.2f} segundos")
pd_clientes.head()
# %%
