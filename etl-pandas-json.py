#%%

import pandas as pd
import time
#import pyspark.pandas as pd

# %%

users_data = "./data/clientes.json"

# %%
start = time.time()
pd_clientes = pd.read_json(users_data, lines=True)
print(f"Tempo pandas: {time.time() - start:.2f} segundos")
pd_clientes.head()
#%%
#Media de Idade por Cidade ordernado pela maior media.
pd_clientes_media_idade = (pd_clientes.groupby("cidade")["idade"]
                           .mean()
                           .sort_values(ascending=False)
                           .reset_index()
)

# %%
pd_clientes_media_idade.head()

#%%
start = time.time()
salvar = "media_idade_no_index.csv"
pd_clientes_csv = pd_clientes_media_idade.to_csv(f"data/{salvar}", index=False)
print(f"Arquivo .csv salvo com sucesso como: {salvar}: {time.time() - start:.2f} segundos")



# %%
