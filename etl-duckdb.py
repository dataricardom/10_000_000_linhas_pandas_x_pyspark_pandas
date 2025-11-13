#%%

import duckdb  as dk
import time
#%%

conn = dk.connect(database=':memory', read_only=False)

#%%

path = "data/clientes.json"
#%%

start = time.time()
read_json = conn.read_json(path)
print(f"Leitura do arquivo finalizado em: {time.time() - start:.2f} segundos")
#%%

read_json.filter("idade < 20").fetchdf()


# %%

conn.sql("SELECT cidade, avg(idade) AS media_idade FROM read_json GROUP BY cidade ORDER BY avg(idade) DESC")


#%%

conn.close()