import streamlit as st
import pandas as pd
import altair as alt



df = pd.read_csv("data/media_idade.csv")

pd_clientes_media_idade = (
    df.groupby("cidade")["idade"]
      .mean()
      .sort_values(ascending=False)
      .reset_index()
)

st.markdown("## <div style='text-align: center;'>MÉDIA DE IDADE POR CIDADE</div>", unsafe_allow_html=True)


st.dataframe(pd_clientes_media_idade)

st.write("Gráfico de Barras")

chart = (
    alt.Chart(pd_clientes_media_idade)
    .mark_bar()
    .encode(
        x=alt.X("cidade:N", title="Cidade"),                     # título do eixo X
        y=alt.Y("idade:Q", title="Média de Idade"),              # título do eixo Y
        color=alt.Color("cidade:N", legend=None),
        tooltip=["cidade", "idade"]
    )
)

st.altair_chart(chart, use_container_width=True)
