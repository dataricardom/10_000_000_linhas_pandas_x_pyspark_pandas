#%%

import pandas as pd
import time
#import pyspark.pandas as pd

# %%

users_data = "./data/clientes.json"

# %%
start = time.time()
pd_flights = pd.read_json(users_data, lines=True)
print(f"Tempo pandas: {time.time() - start:.2f} segundos")
pd_flights.describe()
pd_flights.head()
#%%


