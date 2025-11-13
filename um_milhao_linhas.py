import pandas as pd
import json

# cria 1 milhão de registros falsos
df = pd.DataFrame({
    "id": range(10_000_000),
    "nome": [f"Cliente_{i}" for i in range(10_000_000)],
    "idade": (pd.Series(range(10_000_000)) % 80) + 18,
    "cidade": ["São Paulo", "Rio", "BH", "Curitiba", "Recife"] * 2000_000
})

# salva em JSON linha a linha
df.to_json("data/clientes.json", orient="records", lines=True)
