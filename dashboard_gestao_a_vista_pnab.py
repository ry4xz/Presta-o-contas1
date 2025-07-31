
import streamlit as st
import pandas as pd
import plotly.express as px

# Configurações da página
st.set_page_config(page_title="Prestação de Contas - Gestão à Vista", layout="wide")

# Carregar dados (substituir pelo caminho correto)
@st.cache_data
def carregar_dados():
    url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vT0K7tZ5QxIvAKz_h5JtiJ5x8QuFh1cZQ0N58LjJvNEoYHQVu04_Ki-Ro0tqOpTXQ/pub?output=xlsx"
    return pd.read_excel(url, sheet_name=None)

dados = carregar_dados()

# Menu principal (capa)
st.title("📊 Prestação de Contas - PNAB")
st.markdown("### Gestão à Vista | Projetos Culturais")
st.markdown("---")

abas = list(dados.keys())

col1, col2, col3 = st.columns(3)
for i, aba in enumerate(abas):
    if i % 3 == 0:
        col = col1
    elif i % 3 == 1:
        col = col2
    else:
        col = col3
    if col.button(aba):
        st.session_state["aba_atual"] = aba

# Exibir dados da aba selecionada
aba_atual = st.session_state.get("aba_atual")
if aba_atual:
    df = dados[aba_atual]
    st.header(f"📁 Projeto: {aba_atual}")

    # Indicadores
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.metric("Valor Total Recebido", f"R$ {df['VALOR RECEBIDO'].sum():,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
    with col2:
        st.metric("Valor Pago", f"R$ {df['VALOR PAGO'].sum():,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
    with col3:
        st.metric("Retenção IRPF", f"R$ {df['IR'].sum():,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
    with col4:
        st.metric("Restos a Pagar", f"R$ {df['RESTANTE'].sum():,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
    with col5:
        st.metric("Contemplados", df['NOME'].nunique())

    st.markdown("### 📋 Tabela Detalhada")
    st.dataframe(df, use_container_width=True)

    st.markdown("### 📈 Distribuição de Valores Pagos")
    fig = px.bar(df, x="NOME", y="VALOR PAGO", title="Valores Pagos por Pessoa", text_auto=True)
    fig.update_layout(xaxis_tickangle=-45, height=500)
    st.plotly_chart(fig, use_container_width=True)
