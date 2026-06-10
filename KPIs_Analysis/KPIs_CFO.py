import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import os

# =========================================
# CONFIGURAÇÃO DA PÁGINA (ESTRUTURA LIMPA)
# =========================================
st.set_page_config(
    page_title="Dashboard Financeiro CFO",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed" # Recolhido por padrão para caber no iframe do site
)

# Força o ecossistema a casar estritamente com a paleta Azul/Digital do seu portfólio
TOKENS = {
    "is_dark": True,
    "bg": "rgba(0,0,0,0)",         # Fundo 100% transparente para mesclar com o site
    "card": "rgba(22, 27, 34, 0.4)", # Glassmorphism sutil para os blocos de KPI
    "text": "#FFFFFF",
    "muted": "#A3AEBB",
    "border": "rgba(0, 242, 254, 0.2)", # Bordas com o seu ciano digital
    "primary": "#00f2fe",          # Cor principal do seu portfólio
    "success": "#00e676",          # Verde para deltas positivos
    "danger": "#ff4b4b",           # Vermelho para quedas
    "grid": "#1e293b"
}

PRODUCT_PALETTE = [TOKENS["primary"], "#2dd4bf", "#a78bfa", "#f472b6", "#fb923c", "#34d399"]

# =========================================
# INJEÇÃO DE INVISIBILIDADE E RESPONSIVIDADE (CSS)
# =========================================
st.markdown(f"""
    <style>
        /* Remove fundos pesados e barras nativas do Streamlit */
        .stApp, .block-container {{ background-color: transparent !important; padding-top: 0.5rem !important; }}
        header, footer {{ visibility: hidden !important; }}

        /* Estilização dos Cartões de KPI combinando com o portfólio web */
        .kpi-card {{
            background: {TOKENS["card"]};
            border: 1px solid {TOKENS["border"]};
            border-radius: 12px;
            padding: 16px;
            box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
            backdrop-filter: blur(5px);
            margin-bottom: 12px;
        }}
        .kpi-title {{ font-size: 0.85rem; color: {TOKENS["muted"]}; font-weight: 600; letter-spacing: 0.5px; }}
        .kpi-value {{ font-size: 1.4rem; color: #ffffff; font-weight: 800; margin: 5px 0; font-family: monospace; }}
        .kpi-delta {{ display: inline-block; font-size: 0.75rem; font-weight: 700; padding: 2px 8px; border-radius: 999px; }}
        .delta-up {{ background: rgba(0, 230, 118, 0.15); color: {TOKENS["success"]}; }}
        .delta-down {{ background: rgba(255, 75, 75, 0.15); color: {TOKENS["danger"]}; }}
        .delta-neutral {{ background: rgba(148, 163, 184, 0.15); color: {TOKENS["muted"]}; }}

        /* Ajuste dos seletores da barra lateral */
        section[data-testid="stSidebar"] {{ background: #0f172a !important; border-right: 1px solid {TOKENS["border"]}; }}
        h1, h2, h3 {{ color: #ffffff !important; font-weight: 800; }}
        div[data-baseweb="select"] {{ background-color: rgba(255,255,255,0.05) !important; border-radius: 4px !important; }}
    </style>
""", unsafe_allow_html=True)

# =========================================
# ESTEIRA DE DADOS (RESOLUÇÃO DE CAMINHO DA NUVEM)
# =========================================
@st.cache_data
def carregar_dados() -> pd.DataFrame:
    # Captura a pasta atual do script dinamicamente para evitar erro 404 na nuvem
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    caminho_csv = os.path.join(diretorio_atual, "Financials.csv")

    df = pd.read_csv(caminho_csv)
    df.columns = df.columns.str.strip()

    cols_numericas = ["Units Sold", "Sale Price", "Gross Sales", "Discounts", "Sales", "COGS", "Profit"]
    for col in cols_numericas:
        df[col] = df[col].astype(str).str.replace("$", "", regex=False).str.replace(",", "", regex=False).str.strip()
        df[col] = pd.to_numeric(df[col], errors="coerce")

    df["Discounts"] = df["Discounts"].fillna(0)
    df["Cost Manufacturing"] = np.where(df["Units Sold"] != 0, df["COGS"] / df["Units Sold"], 0)
    df["Gross Profit Margin"] = np.where(df["Sales"] != 0, df["Profit"] / df["Sales"], 0)
    return df

# Auxiliares de formatação de valores monetários e decimais
def formatar_moeda(v: float) -> str: return f"R$ {v:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
def formatar_delta(v: float) -> str: return f"{'+' if v > 0 else ''}{v:.2f}%"

def classe_delta(v: float) -> tuple[str, str]:
    if v > 0: return "delta-up", "▲"
    if v < 0: return "delta-down", "▼"
    return "delta-neutral", "■"

def calcular_delta_mes(grupo: pd.DataFrame, coluna: str) -> float:
    if grupo.shape[0] < 2: return 0.0
    atual, anterior = grupo.iloc[-1][coluna], grupo.iloc[-2][coluna]
    return ((atual - anterior) / anterior) * 100 if anterior != 0 else 0.0

def render_kpi_card(titulo: str, valor: str, delta: float, descricao: str) -> None:
    classe, seta = classe_delta(delta)
    st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-title">{titulo.upper()}</div>
            <div class="kpi-value">{valor}</div>
            <div class="kpi-delta {classe}">{seta} {formatar_delta(delta)}</div>
        </div>
    """, unsafe_allow_html=True)

def aplicar_layout_portfolio(fig, titulo: str, yaxis_title: str = ""):
    # Força uma cor escura padrão para garantir leitura em fundos claros
    cor_texto_estrita = "#0F172A"
    cor_grade_estrita = "#E2E8F0"

    fig.update_layout(
        template="plotly_white", # Garante a paleta base para fundos claros
        title={
            "text": titulo,
            "font": {"size": 14, "color": cor_texto_estrita, "weight": "bold"}
        },
        paper_bgcolor="rgba(0,0,0,0)", # Mantém a transparência do contêiner
        plot_bgcolor="rgba(0,0,0,0)",  # Mantém a transparência do contêiner
        margin=dict(l=10, r=10, t=40, b=10),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1,
            font=dict(color=cor_texto_estrita)
        )
    )
    # Força as cores dos eixos e legendas a ficarem visíveis no fundo claro
    fig.update_xaxes(showgrid=False, linecolor=cor_grade_estrita, tickfont=dict(color=cor_texto_estrita))
    fig.update_yaxes(title=yaxis_title, gridcolor=cor_grade_estrita, zeroline=False, tickfont=dict(color=cor_texto_estrita))
    return fig


# Execution pipeline
df = carregar_dados()

# =========================================
# FILTRAGEM STRATEGICA DA SIDEBAR
# =========================================
st.sidebar.markdown("### 🎛️ Filtros do Portfólio")
paises = st.sidebar.multiselect("Países Selecionados:", options=sorted(df["Country"].unique()), default=sorted(df["Country"].unique()))
produtos = st.sidebar.multiselect("Produtos Selecionados:", options=sorted(df["Product"].unique()), default=sorted(df["Product"].unique()))

df_filtrado = df[df["Country"].isin(paises) & df["Product"].isin(produtos)]
if df_filtrado.empty:
    st.warning("Ajuste os filtros laterais para renderizar o painel.")
    st.stop()

# Agrupamento da base mensal cronológica
base_mensal = df_filtrado.groupby(["Month Number", "Month Name"], as_index=False).agg({
    "Sales": "sum", "Profit": "sum", "Units Sold": "sum"
}).sort_values("Month Number")

base_mensal["Gross Margin"] = np.where(base_mensal["Sales"] != 0, base_mensal["Profit"] / base_mensal["Sales"], 0)
base_mensal["Ticket Medio"] = np.where(base_mensal["Units Sold"] != 0, base_mensal["Sales"] / base_mensal["Units Sold"], 0)

# =========================================
# RENDERIZAÇÃO DA GRADE OPERACIONAL
# =========================================
st.markdown("### 📊 Executivo CFO Monitor")

receita_t = df_filtrado["Sales"].sum()
lucro_t = df_filtrado["Profit"].sum()
margem_b = lucro_t / receita_t if receita_t != 0 else 0
ticket_m = receita_t / df_filtrado["Units Sold"].sum() if df_filtrado["Units Sold"].sum() != 0 else 0

# Grid de cartões compactos (Estilo Bloco Financeiro)
k1, k2, k3, k4 = st.columns(4)
with k1: render_kpi_card("Receita Líquida", formatar_moeda(receita_t), calcular_delta_mes(base_mensal, "Sales"), "")
with k2: render_kpi_card("Lucro Consolidado", formatar_moeda(lucro_t), calcular_delta_mes(base_mensal, "Profit"), "")
with k3: render_kpi_card("Margem Bruta %", f"{margem_b:.2%}", calcular_delta_mes(base_mensal, "Gross Margin"), "")
with k4: render_kpi_card("Ticket Médio", formatar_moeda(ticket_m), calcular_delta_mes(base_mensal, "Ticket Medio"), "")

st.markdown("<br>", unsafe_allow_html=True)

# Bloco Gráfico com as linhas e barras estilizadas no Ciano do site
g1, g2 = st.columns(2)
with g1:
    fig_rec = px.line(base_mensal, x="Month Name", y="Sales", markers=True, color_discrete_sequence=[TOKENS["primary"]])
    fig_rec.update_traces(line=dict(width=3.5), marker=dict(size=7))
    aplicar_layout_portfolio(fig_rec, "Tendência Mensal da Receita")
    st.plotly_chart(fig_rec, use_container_width=True)
with g2:
    fig_luc = px.bar(base_mensal, x="Month Name", y="Profit", color_discrete_sequence=["#2dd4bf"])
    aplicar_layout_portfolio(fig_luc, "Distribuição do Lucro por Período")
    st.plotly_chart(fig_luc, use_container_width=True)
