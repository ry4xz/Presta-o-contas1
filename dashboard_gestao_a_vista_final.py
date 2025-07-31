
import streamlit as st
import pandas as pd

# ====================== CONFIGURAÇÃO ======================
st.set_page_config(page_title="Gestão à Vista - Prestação de Contas", layout="wide")

@st.cache_data
def carregar_dados():
    return pd.read_excel("PRESTAÇÃO DE CONTAS PNAB.xlsx", sheet_name=None)

dados = carregar_dados()

# ====================== CAPA COM BOTÕES ======================
st.title("📊 Gestão à Vista - Prestação de Contas PNAB")

abas_disponiveis = list(dados.keys()) + ["Cadastro de Beneficiários"]
col1, col2, col3 = st.columns(3)
for i, aba in enumerate(abas_disponiveis):
    if i % 3 == 0:
        col = col1
    elif i % 3 == 1:
        col = col2
    else:
        col = col3
    if col.button(f"🔎 {aba}"):
        st.session_state["aba_atual"] = aba

# Define aba padrão
if "aba_atual" not in st.session_state:
    st.session_state["aba_atual"] = abas_disponiveis[0]

aba = st.session_state["aba_atual"]

st.markdown("---")

# ====================== VISUALIZAÇÃO POR ABA ======================
if aba != "Cadastro de Beneficiários":
    df = dados[aba].dropna(how="all")  # remove linhas completamente vazias
    df = df.fillna("R$ 0,00")          # substitui valores None
    st.subheader(f"Aba: {aba}")
    st.dataframe(df, use_container_width=True)

    # Indicadores simulados (exemplo: somar colunas específicas)
    with st.container():
        col1, col2, col3, col4 = st.columns(4)
        try:
            df_num = df.copy()
            for col in df.columns:
                df_num[col] = pd.to_numeric(df[col].astype(str).str.replace(r"[^\d,]", "", regex=True).str.replace(",", "."), errors="coerce")
            col1.metric("📥 Valor Total Recebido", f"R$ {df_num.sum().sum():,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
            col2.metric("📤 Valor Pago", "R$ 0,00")
            col3.metric("💰 Retenção IRPF", "R$ 0,00")
            col4.metric("📌 Restos a Pagar", "R$ 0,00")
        except:
            st.warning("Não foi possível calcular os valores numéricos.")

# ====================== ABA BENEFICIÁRIOS ======================
else:
    st.subheader("Cadastro de Beneficiários")

    dados_benef = [
        {"Projeto": "PONTÕES DE CULTURA", "Nome": "2024NE000130", "CPF/CNPJ": "22.222.222/2222-22"},
        {"Projeto": "REDE DE PONTOS", "Nome": "2024NE000123", "CPF/CNPJ": "000.000.000-00"},
        {"Projeto": "PONTÕES DE CULTURA", "Nome": "2024NE000001", "CPF/CNPJ": "111.111.111-11"},
        {"Projeto": "REDE DE PONTOS", "Nome": "2024NE000002", "CPF/CNPJ": "33.333.333/3333-33"},
        {"Projeto": "REDE DE PONTOS", "Nome": "2024NE000321", "CPF/CNPJ": "123.456.789-00"},
    ]
    df_benef = pd.DataFrame(dados_benef)
    st.dataframe(df_benef, use_container_width=True)
