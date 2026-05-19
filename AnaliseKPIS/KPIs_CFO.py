import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="Dashboard Financeiro CFO",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================
# SESSION STATE
# =========================
if "app_theme" not in st.session_state:
    native_theme = st.get_option("theme.base") or "light"
    st.session_state.app_theme = native_theme

if "filtro_ano" not in st.session_state:
    st.session_state.filtro_ano = []
if "filtro_pais" not in st.session_state:
    st.session_state.filtro_pais = []
if "filtro_produto" not in st.session_state:
    st.session_state.filtro_produto = []
if "filtro_segmento" not in st.session_state:
    st.session_state.filtro_segmento = []

# =========================
# TOKENS DE TEMA
# =========================
def get_theme_tokens(theme_name: str) -> dict:
    is_dark = theme_name == "dark"

    return {
        "is_dark": is_dark,
        "bg": "#0E1117" if is_dark else "#F8FAFC",
        "card": "#161B22" if is_dark else "#FFFFFF",
        "text": "#F8FAFC" if is_dark else "#0F172A",
        "muted": "#A3AEBB" if is_dark else "#64748B",
        "border": "#2D3748" if is_dark else "#E2E8F0",
        "primary": "#60A5FA" if is_dark else "#1D4ED8",
        "secondary": "#22D3EE" if is_dark else "#06B6D4",
        "success": "#34D399" if is_dark else "#10B981",
        "warning": "#FBBF24" if is_dark else "#F59E0B",
        "danger": "#F87171" if is_dark else "#EF4444",
        "grid": "#334155" if is_dark else "#E5E7EB",
        "sidebar_bg_1": "#111827" if is_dark else "#0F172A",
        "sidebar_bg_2": "#1F2937" if is_dark else "#1E293B",
        "sidebar_input_bg": "rgba(255,255,255,0.08)" if is_dark else "rgba(255,255,255,0.10)",
        "shadow": "0 10px 28px rgba(0,0,0,0.28)" if is_dark else "0 10px 28px rgba(15, 23, 42, 0.08)",
        "tab_bg": "#1E293B" if is_dark else "#E2E8F0",
        "icon_bg": "rgba(96,165,250,0.18)" if is_dark else "#EFF6FF",
        "insight_bg": "#111827" if is_dark else "#FFFFFF"
    }

TOKENS = get_theme_tokens(st.session_state.app_theme)

PRODUCT_PALETTE = [
    TOKENS["primary"],
    TOKENS["secondary"],
    TOKENS["success"],
    TOKENS["warning"],
    "#A78BFA",
    "#F472B6",
    "#FB923C",
    "#2DD4BF"
]

# =========================
# CSS
# =========================
def inject_css(tokens: dict) -> None:
    st.markdown(
        f"""
        <style>
            .stApp {{
                background-color: {tokens["bg"]};
            }}

            .block-container {{
                padding-top: 1.1rem;
                padding-bottom: 2rem;
                padding-left: 1.2rem;
                padding-right: 1.2rem;
                max-width: 100%;
            }}

            section[data-testid="stSidebar"] {{
                background: linear-gradient(180deg, {tokens["sidebar_bg_1"]} 0%, {tokens["sidebar_bg_2"]} 100%);
                border-right: 1px solid {tokens["border"]};
            }}

            section[data-testid="stSidebar"] .stMarkdown,
            section[data-testid="stSidebar"] label,
            section[data-testid="stSidebar"] p,
            section[data-testid="stSidebar"] span,
            section[data-testid="stSidebar"] h1,
            section[data-testid="stSidebar"] h2,
            section[data-testid="stSidebar"] h3,
            section[data-testid="stSidebar"] small {{
                color: #FFFFFF !important;
            }}

            section[data-testid="stSidebar"] div[data-baseweb="select"] {{
                background-color: {tokens["sidebar_input_bg"]} !important;
                border: 1px solid rgba(255,255,255,0.14) !important;
                border-radius: 12px !important;
            }}

            section[data-testid="stSidebar"] div[data-baseweb="tag"] {{
                background-color: rgba(255,255,255,0.14) !important;
                color: #FFFFFF !important;
                border-radius: 999px !important;
            }}

            h1, h2, h3 {{
                color: {tokens["text"]};
                font-weight: 800;
                letter-spacing: -0.02em;
            }}

            .app-subtitle {{
                color: {tokens["muted"]};
                font-size: 1rem;
                margin-top: -8px;
                margin-bottom: 18px;
            }}

            .section-caption {{
                color: {tokens["muted"]};
                font-size: 0.92rem;
                margin-top: -6px;
                margin-bottom: 14px;
                line-height: 1.5;
            }}

            .toolbar-card {{
                background: {tokens["card"]};
                border: 1px solid {tokens["border"]};
                border-radius: 18px;
                padding: 12px 16px;
                box-shadow: {tokens["shadow"]};
                margin-bottom: 16px;
            }}

            .toolbar-title {{
                color: {tokens["text"]};
                font-weight: 700;
                font-size: 0.95rem;
                margin-bottom: 4px;
            }}

            .toolbar-desc {{
                color: {tokens["muted"]};
                font-size: 0.84rem;
            }}

            .kpi-card {{
                background: {tokens["card"]};
                border: 1px solid {tokens["border"]};
                border-radius: 20px;
                padding: 18px;
                box-shadow: {tokens["shadow"]};
                min-height: 162px;
            }}

            .kpi-top {{
                display: flex;
                justify-content: space-between;
                align-items: center;
                gap: 12px;
                margin-bottom: 14px;
            }}

            .kpi-title {{
                font-size: 0.95rem;
                color: {tokens["muted"]};
                font-weight: 600;
            }}

            .kpi-icon {{
                font-size: 1.2rem;
                padding: 8px 12px;
                border-radius: 12px;
                background: {tokens["icon_bg"]};
            }}

            .kpi-value {{
                font-size: 1.55rem;
                color: {tokens["text"]};
                font-weight: 800;
                margin-bottom: 8px;
                word-break: break-word;
            }}

            .kpi-delta {{
                display: inline-block;
                font-size: 0.84rem;
                font-weight: 700;
                padding: 6px 10px;
                border-radius: 999px;
                margin-bottom: 10px;
            }}

            .delta-up {{
                background: rgba(16, 185, 129, 0.16);
                color: {tokens["success"]};
            }}

            .delta-down {{
                background: rgba(239, 68, 68, 0.16);
                color: {tokens["danger"]};
            }}

            .delta-neutral {{
                background: rgba(148, 163, 184, 0.18);
                color: {tokens["muted"]};
            }}

            .kpi-desc {{
                color: {tokens["muted"]};
                font-size: 0.83rem;
                line-height: 1.45;
            }}

            .insight-box {{
                background: {tokens["insight_bg"]};
                border: 1px solid {tokens["border"]};
                border-left: 6px solid {tokens["primary"]};
                border-radius: 18px;
                padding: 18px;
                box-shadow: {tokens["shadow"]};
                margin-bottom: 12px;
            }}

            .insight-title {{
                font-size: 1rem;
                font-weight: 800;
                color: {tokens["text"]};
                margin-bottom: 8px;
            }}

            .insight-text {{
                color: {tokens["muted"]};
                font-size: 0.95rem;
                line-height: 1.6;
            }}

            .alert-success {{
                border-left-color: {tokens["success"]} !important;
            }}

            .alert-warning {{
                border-left-color: {tokens["warning"]} !important;
            }}

            .alert-danger {{
                border-left-color: {tokens["danger"]} !important;
            }}

            .stTabs [data-baseweb="tab-list"] {{
                gap: 8px;
                flex-wrap: wrap;
            }}

            .stTabs [data-baseweb="tab"] {{
                background-color: {tokens["tab_bg"]};
                border-radius: 12px;
                padding: 10px 18px;
                color: {tokens["text"]};
                font-weight: 600;
            }}

            .stTabs [aria-selected="true"] {{
                background-color: {tokens["primary"]} !important;
                color: {"#0B1020" if tokens["is_dark"] else "#FFFFFF"} !important;
            }}

            div[data-testid="stDataFrame"] {{
                border: 1px solid {tokens["border"]};
                border-radius: 16px;
                overflow: hidden;
                background: {tokens["card"]};
            }}

            hr {{
                border: none;
                border-top: 1px solid {tokens["border"]};
                margin: 1rem 0 1.2rem 0;
            }}

            @media (max-width: 1200px) {{
                .kpi-card {{
                    min-height: 175px;
                }}
                .kpi-value {{
                    font-size: 1.35rem;
                }}
            }}

            @media (max-width: 768px) {{
                .block-container {{
                    padding-left: 0.9rem;
                    padding-right: 0.9rem;
                }}
                .kpi-card {{
                    min-height: auto;
                    padding: 16px;
                }}
                .kpi-value {{
                    font-size: 1.2rem;
                }}
                .kpi-desc {{
                    font-size: 0.80rem;
                }}
            }}
        </style>
        """,
        unsafe_allow_html=True
    )

inject_css(TOKENS)

# =========================
# FUNÇÕES DE DADOS
# =========================
@st.cache_data
def carregar_dados() -> pd.DataFrame:
    df = pd.read_csv("AnaliseKPIS/Financials.csv")
    df.columns = df.columns.str.strip()

    cols_numericas = [
        "Units Sold", "Sale Price", "Gross Sales",
        "Discounts", "Sales", "COGS", "Profit"
    ]

    for col in cols_numericas:
        df[col] = (
            df[col]
            .astype(str)
            .str.replace("$", "", regex=False)
            .str.replace(",", "", regex=False)
            .str.strip()
        )
        df[col] = pd.to_numeric(df[col], errors="coerce")

    df["Discounts"] = df["Discounts"].fillna(0)

    df["Cost Manufacturing"] = np.where(
        df["Units Sold"] != 0,
        df["COGS"] / df["Units Sold"],
        0
    )

    df["Gross Profit Margin"] = np.where(
        df["Sales"] != 0,
        df["Profit"] / df["Sales"],
        0
    )

    df["Unit Contribution Margin"] = np.where(
        df["Sale Price"] != 0,
        (df["Sale Price"] - df["Cost Manufacturing"]) / df["Sale Price"],
        0
    )

    df["Discount Impact"] = np.where(
        df["Gross Sales"] != 0,
        df["Discounts"] / df["Gross Sales"],
        0
    )

    df["Cogs Sales"] = np.where(
        df["Sales"] != 0,
        df["COGS"] / df["Sales"],
        0
    )

    return df


def formatar_moeda(valor: float) -> str:
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def formatar_numero(valor: float) -> str:
    return f"{valor:,.0f}".replace(",", "X").replace(".", ",").replace("X", ".")


def formatar_delta(valor: float) -> str:
    sinal = "+" if valor > 0 else ""
    return f"{sinal}{valor:.2f}%"


def classe_delta(valor: float) -> tuple[str, str]:
    if valor > 0:
        return "delta-up", "▲"
    if valor < 0:
        return "delta-down", "▼"
    return "delta-neutral", "■"


def calcular_delta_mes(grupo: pd.DataFrame, coluna: str) -> float:
    if grupo.shape[0] < 2:
        return 0.0

    atual = grupo.iloc[-1][coluna]
    anterior = grupo.iloc[-2][coluna]

    if anterior == 0:
        return 0.0

    return ((atual - anterior) / anterior) * 100


def render_kpi_card(titulo: str, valor: str, delta: float, descricao: str, icone: str) -> None:
    classe, seta = classe_delta(delta)

    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-top">
                <div class="kpi-title">{titulo}</div>
                <div class="kpi-icon">{icone}</div>
            </div>
            <div class="kpi-value">{valor}</div>
            <div class="kpi-delta {classe}">{seta} {formatar_delta(delta)}</div>
            <div class="kpi-desc">{descricao}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


def render_insight_box(titulo: str, texto: str, classe: str = "") -> None:
    st.markdown(
        f"""
        <div class="insight-box {classe}">
            <div class="insight-title">{titulo}</div>
            <div class="insight-text">{texto}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


def aplicar_layout(fig, titulo: str, yaxis_title: str = ""):
    fig.update_layout(
        template="plotly_dark" if TOKENS["is_dark"] else "plotly_white",
        title={
            "text": titulo,
            "x": 0.02,
            "xanchor": "left",
            "font": {"size": 18, "color": TOKENS["text"]}
        },
        paper_bgcolor=TOKENS["card"],
        plot_bgcolor=TOKENS["card"],
        font=dict(family="Arial", size=12, color=TOKENS["text"]),
        margin=dict(l=20, r=20, t=60, b=20),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1,
            font=dict(color=TOKENS["muted"])
        )
    )

    fig.update_xaxes(
        title="",
        showgrid=False,
        linecolor=TOKENS["border"],
        tickfont=dict(color=TOKENS["muted"])
    )

    fig.update_yaxes(
        title=yaxis_title,
        gridcolor=TOKENS["grid"],
        zeroline=False,
        tickfont=dict(color=TOKENS["muted"])
    )

    return fig


def resetar_filtros(df: pd.DataFrame) -> None:
    anos = sorted(df["Year"].dropna().unique()) if "Year" in df.columns else []
    paises = sorted(df["Country"].dropna().unique())
    produtos = sorted(df["Product"].dropna().unique())
    segmentos = sorted(df["Segment"].dropna().unique()) if "Segment" in df.columns else []

    st.session_state.filtro_ano = anos
    st.session_state.filtro_pais = paises
    st.session_state.filtro_produto = produtos
    st.session_state.filtro_segmento = segmentos


def alternar_tema() -> None:
    st.session_state.app_theme = "dark" if st.session_state.app_theme == "light" else "light"


# =========================
# CARREGAMENTO
# =========================
df = carregar_dados()

# inicializa filtros com todos os valores na primeira carga
if not st.session_state.filtro_ano and "Year" in df.columns:
    st.session_state.filtro_ano = sorted(df["Year"].dropna().unique())
if not st.session_state.filtro_pais:
    st.session_state.filtro_pais = sorted(df["Country"].dropna().unique())
if not st.session_state.filtro_produto:
    st.session_state.filtro_produto = sorted(df["Product"].dropna().unique())
if not st.session_state.filtro_segmento and "Segment" in df.columns:
    st.session_state.filtro_segmento = sorted(df["Segment"].dropna().unique())

# =========================
# HEADER / TOOLBAR
# =========================
titulo_col, controle_col = st.columns([5, 1.4])

with titulo_col:
    st.title("📊 Dashboard Financeiro CFO")
    st.markdown(
        '<div class="app-subtitle">Painel executivo com tema adaptável, filtros persistentes, deltas automáticos e insights gerenciais para tomada de decisão.</div>',
        unsafe_allow_html=True
    )

with controle_col:
    st.markdown(
        """
        <div class="toolbar-card">
            <div class="toolbar-title">Tema do App</div>
            <div class="toolbar-desc">Alterne entre light e dark.</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    if st.button(
        "🌙 Dark Mode" if st.session_state.app_theme == "light" else "☀️ Light Mode",
        use_container_width=True
    ):
        alternar_tema()
        st.rerun()

# =========================
# SIDEBAR
# =========================
st.sidebar.markdown("## 🎛 Filtros Estratégicos")
st.sidebar.markdown("Os filtros persistem na sessão e podem ser redefinidos a qualquer momento.")

anos = sorted(df["Year"].dropna().unique()) if "Year" in df.columns else []
paises = sorted(df["Country"].dropna().unique())
produtos = sorted(df["Product"].dropna().unique())
segmentos = sorted(df["Segment"].dropna().unique()) if "Segment" in df.columns else []

col_sb_1, col_sb_2 = st.sidebar.columns(2)

with col_sb_1:
    if st.button("✅ Todos", use_container_width=True):
        resetar_filtros(df)
        st.rerun()

with col_sb_2:
    if st.button("🧹 Resetar", use_container_width=True):
        resetar_filtros(df)
        st.rerun()

if anos:
    ano_sel = st.sidebar.multiselect(
        "Ano",
        options=anos,
        default=st.session_state.filtro_ano,
        key="filtro_ano"
    )
else:
    ano_sel = []

pais_sel = st.sidebar.multiselect(
    "País",
    options=paises,
    default=st.session_state.filtro_pais,
    key="filtro_pais"
)

produto_sel = st.sidebar.multiselect(
    "Produto",
    options=produtos,
    default=st.session_state.filtro_produto,
    key="filtro_produto"
)

if segmentos:
    segmento_sel = st.sidebar.multiselect(
        "Segmento",
        options=segmentos,
        default=st.session_state.filtro_segmento,
        key="filtro_segmento"
    )
else:
    segmento_sel = []

st.sidebar.markdown("---")
st.sidebar.caption(
    "💡 Dica: os componentes visuais e os gráficos acompanham o tema selecionado no aplicativo."
)

# =========================
# FILTRAGEM
# =========================
df_filtrado = df.copy()

if anos:
    df_filtrado = df_filtrado[df_filtrado["Year"].isin(ano_sel)]

df_filtrado = df_filtrado[df_filtrado["Country"].isin(pais_sel)]
df_filtrado = df_filtrado[df_filtrado["Product"].isin(produto_sel)]

if segmentos:
    df_filtrado = df_filtrado[df_filtrado["Segment"].isin(segmento_sel)]

# proteção para filtros vazios
if df_filtrado.empty:
    st.warning("Nenhum dado encontrado para os filtros selecionados. Ajuste os filtros para continuar.")
    st.stop()

# =========================
# BASE MENSAL
# =========================
base_mensal = (
    df_filtrado.groupby(["Month Number", "Month Name"], as_index=False)
    .agg({
        "Sales": "sum",
        "Profit": "sum",
        "Units Sold": "sum",
        "Gross Sales": "sum",
        "Discounts": "sum",
        "COGS": "sum"
    })
    .sort_values("Month Number")
)

base_mensal["Gross Margin"] = np.where(
    base_mensal["Sales"] != 0,
    base_mensal["Profit"] / base_mensal["Sales"],
    0
)

base_mensal["Ticket Médio"] = np.where(
    base_mensal["Units Sold"] != 0,
    base_mensal["Sales"] / base_mensal["Units Sold"],
    0
)

base_mensal["Discount Impact"] = np.where(
    base_mensal["Gross Sales"] != 0,
    base_mensal["Discounts"] / base_mensal["Gross Sales"],
    0
)

base_mensal["COGS Ratio"] = np.where(
    base_mensal["Sales"] != 0,
    base_mensal["COGS"] / base_mensal["Sales"],
    0
)

base_mensal["MoM Growth (%)"] = base_mensal["Sales"].pct_change() * 100
base_mensal["Cor"] = np.where(
    base_mensal["MoM Growth (%)"] >= 0,
    "Positivo",
    "Negativo"
)

# =========================
# KPIs
# =========================
receita_total = df_filtrado["Sales"].sum()
lucro_total = df_filtrado["Profit"].sum()
gross_sales_total = df_filtrado["Gross Sales"].sum()
descontos_total = df_filtrado["Discounts"].sum()
unidades_total = df_filtrado["Units Sold"].sum()
cogs_total = df_filtrado["COGS"].sum()

margem_bruta = lucro_total / receita_total if receita_total != 0 else 0
impacto_desconto = descontos_total / gross_sales_total if gross_sales_total != 0 else 0
ticket_medio = receita_total / unidades_total if unidades_total != 0 else 0
cogs_ratio = cogs_total / receita_total if receita_total != 0 else 0

st.markdown("## 📌 KPIs Executivos")
st.markdown(
    '<div class="section-caption">Indicadores consolidados com variação do último mês em relação ao mês imediatamente anterior.</div>',
    unsafe_allow_html=True
)

kpi1, kpi2, kpi3, kpi4 = st.columns(4)
with kpi1:
    render_kpi_card(
        "Receita Líquida Total",
        formatar_moeda(receita_total),
        calcular_delta_mes(base_mensal, "Sales"),
        "Variação mensal da receita líquida no recorte selecionado.",
        "💰"
    )
with kpi2:
    render_kpi_card(
        "Lucro Total",
        formatar_moeda(lucro_total),
        calcular_delta_mes(base_mensal, "Profit"),
        "Rentabilidade total consolidada após custos e descontos.",
        "📈"
    )
with kpi3:
    render_kpi_card(
        "Margem Bruta",
        f"{margem_bruta:.2%}",
        calcular_delta_mes(base_mensal, "Gross Margin"),
        "Eficiência da operação na conversão da receita em lucro bruto.",
        "🎯"
    )
with kpi4:
    render_kpi_card(
        "Ticket Médio",
        formatar_moeda(ticket_medio),
        calcular_delta_mes(base_mensal, "Ticket Médio"),
        "Receita média gerada por unidade vendida.",
        "🛒"
    )

kpi5, kpi6, kpi7, kpi8 = st.columns(4)
with kpi5:
    render_kpi_card(
        "Receita Bruta",
        formatar_moeda(gross_sales_total),
        calcular_delta_mes(base_mensal, "Gross Sales"),
        "Volume bruto antes da aplicação de descontos comerciais.",
        "🏦"
    )
with kpi6:
    render_kpi_card(
        "Descontos Totais",
        formatar_moeda(descontos_total),
        calcular_delta_mes(base_mensal, "Discounts"),
        "Pressão promocional acumulada sobre a receita bruta.",
        "🏷️"
    )
with kpi7:
    render_kpi_card(
        "Impacto dos Descontos",
        f"{impacto_desconto:.2%}",
        calcular_delta_mes(base_mensal, "Discount Impact"),
        "Participação percentual dos descontos sobre a receita bruta.",
        "⚠️"
    )
with kpi8:
    render_kpi_card(
        "COGS / Sales",
        f"{cogs_ratio:.2%}",
        calcular_delta_mes(base_mensal, "COGS Ratio"),
        "Parcela da receita líquida consumida pelos custos diretos.",
        "⚙️"
    )

st.markdown("<hr>", unsafe_allow_html=True)

# =========================
# INSIGHTS
# =========================
st.markdown("## 🧠 Insights Automáticos")
st.markdown(
    '<div class="section-caption">Leitura executiva automatizada para apoiar decisões de portfólio, margem, custo e mercados prioritários.</div>',
    unsafe_allow_html=True
)

top_produto_receita = (
    df_filtrado.groupby("Product", as_index=False)["Sales"]
    .sum()
    .sort_values("Sales", ascending=False)
)

top_produto_lucro = (
    df_filtrado.groupby("Product", as_index=False)["Profit"]
    .sum()
    .sort_values("Profit", ascending=False)
)

top_pais_receita = (
    df_filtrado.groupby("Country", as_index=False)["Sales"]
    .sum()
    .sort_values("Sales", ascending=False)
)

eficiencia_produto = (
    df_filtrado.groupby("Product", as_index=False)
    .agg({
        "Discount Impact": "mean",
        "Cogs Sales": "mean",
        "Gross Profit Margin": "mean"
    })
)

if not eficiencia_produto.empty:
    melhor_margem = eficiencia_produto.sort_values("Gross Profit Margin", ascending=False).iloc[0]
    pior_cogs = eficiencia_produto.sort_values("Cogs Sales", ascending=False).iloc[0]
    maior_desconto = eficiencia_produto.sort_values("Discount Impact", ascending=False).iloc[0]

    ins1, ins2 = st.columns(2)

    with ins1:
        if not top_produto_receita.empty:
            render_insight_box(
                "Produto líder em receita",
                f"O produto <b>{top_produto_receita.iloc[0]['Product']}</b> lidera a receita com "
                f"<b>{formatar_moeda(top_produto_receita.iloc[0]['Sales'])}</b>. Isso sugere maior tração comercial "
                f"e potencial para priorização em estoque, marketing e expansão.",
                "alert-success"
            )

        if not top_produto_lucro.empty:
            render_insight_box(
                "Produto líder em lucro",
                f"O produto <b>{top_produto_lucro.iloc[0]['Product']}</b> concentra o maior lucro, somando "
                f"<b>{formatar_moeda(top_produto_lucro.iloc[0]['Profit'])}</b>. Esse item pode representar um eixo central "
                f"de rentabilidade do portfólio.",
                "alert-success"
            )

        if not top_pais_receita.empty:
            render_insight_box(
                "País com maior participação",
                f"O país <b>{top_pais_receita.iloc[0]['Country']}</b> apresenta a maior receita do recorte, com "
                f"<b>{formatar_moeda(top_pais_receita.iloc[0]['Sales'])}</b>. Vale monitorar a sustentabilidade dessa liderança "
                f"em margem e crescimento.",
                "alert-success"
            )

    with ins2:
        render_insight_box(
            "Produto com maior pressão de custo",
            f"O produto <b>{pior_cogs['Product']}</b> apresenta a maior relação <b>COGS / Sales</b>, com média de "
            f"<b>{pior_cogs['Cogs Sales']:.2%}</b>. Isso pode indicar necessidade de revisão de custo, cadeia operacional "
            f"ou precificação.",
            "alert-danger"
        )

        render_insight_box(
            "Produto mais impactado por descontos",
            f"O produto <b>{maior_desconto['Product']}</b> possui impacto médio de desconto de "
            f"<b>{maior_desconto['Discount Impact']:.2%}</b>. Caso esse desconto não converta em ganho de volume com margem, "
            f"há risco de erosão de valor.",
            "alert-warning"
        )

        render_insight_box(
            "Produto com melhor margem média",
            f"O produto <b>{melhor_margem['Product']}</b> apresenta a melhor margem bruta média, em "
            f"<b>{melhor_margem['Gross Profit Margin']:.2%}</b>. Esse desempenho pode servir como referência para decisões de mix "
            f"e estratégia comercial.",
            "alert-success"
        )

if margem_bruta < 0.20:
    render_insight_box(
        "Alerta de margem bruta",
        f"A margem bruta consolidada está em <b>{margem_bruta:.2%}</b>, abaixo de um patamar de referência de 20%. "
        f"Esse comportamento pode sugerir excesso de desconto, custo elevado ou mix menos rentável.",
        "alert-danger"
    )
elif margem_bruta < 0.35:
    render_insight_box(
        "Margem em atenção",
        f"A margem bruta consolidada está em <b>{margem_bruta:.2%}</b>. Embora positiva, recomenda-se acompanhamento próximo "
        f"da evolução por produto e país.",
        "alert-warning"
    )
else:
    render_insight_box(
        "Margem saudável",
        f"A margem bruta consolidada está em <b>{margem_bruta:.2%}</b>, sugerindo boa conversão da receita em resultado bruto "
        f"no recorte atual.",
        "alert-success"
    )

st.markdown("<hr>", unsafe_allow_html=True)

# =========================
# AGRUPAMENTOS
# =========================
ticket_por_produto = (
    df_filtrado.groupby("Product", as_index=False)
    .agg({"Sales": "sum", "Units Sold": "sum"})
)

ticket_por_produto["Average Ticket"] = np.where(
    ticket_por_produto["Units Sold"] != 0,
    ticket_por_produto["Sales"] / ticket_por_produto["Units Sold"],
    0
)

receita_por_pais = (
    df_filtrado.groupby("Country", as_index=False)["Sales"]
    .sum()
    .sort_values("Sales", ascending=False)
)

mix_produtos = (
    df_filtrado.groupby("Product", as_index=False)["Profit"]
    .sum()
    .sort_values("Profit", ascending=False)
)

mix_produtos["Mix (%)"] = np.where(
    mix_produtos["Profit"].sum() != 0,
    (mix_produtos["Profit"] / mix_produtos["Profit"].sum()) * 100,
    0
)

# =========================
# GRÁFICOS
# =========================
st.markdown("## 📈 Evolução Mensal")
st.markdown(
    '<div class="section-caption">Acompanhe o comportamento temporal da receita, lucro, volume e crescimento mês a mês.</div>',
    unsafe_allow_html=True
)

g1, g2 = st.columns(2)

with g1:
    fig_receita = px.line(
        base_mensal,
        x="Month Name",
        y="Sales",
        markers=True,
        color_discrete_sequence=[TOKENS["primary"]]
    )
    fig_receita.update_traces(line=dict(width=4), marker=dict(size=8))
    aplicar_layout(fig_receita, "Receita Líquida por Mês", "Receita")
    fig_receita.update_yaxes(tickprefix="R$ ")
    st.plotly_chart(fig_receita, use_container_width=True)

with g2:
    fig_lucro = px.bar(
        base_mensal,
        x="Month Name",
        y="Profit",
        text_auto=".2s",
        color_discrete_sequence=[TOKENS["success"]]
    )
    aplicar_layout(fig_lucro, "Lucro Total por Mês", "Lucro")
    fig_lucro.update_yaxes(tickprefix="R$ ")
    st.plotly_chart(fig_lucro, use_container_width=True)

g3, g4 = st.columns(2)

with g3:
    fig_tpv = px.area(
        base_mensal,
        x="Month Name",
        y="Units Sold",
        color_discrete_sequence=[TOKENS["secondary"]]
    )
    fig_tpv.update_traces(
        fillcolor="rgba(34, 211, 238, 0.22)" if TOKENS["is_dark"] else "rgba(6, 182, 212, 0.25)",
        line=dict(width=2)
    )
    aplicar_layout(fig_tpv, "Volume de Vendas por Mês", "Unidades Vendidas")
    st.plotly_chart(fig_tpv, use_container_width=True)

with g4:
    fig_mom = px.bar(
        base_mensal,
        x="Month Name",
        y="MoM Growth (%)",
        color="Cor",
        text_auto=".2f",
        color_discrete_map={
            "Positivo": TOKENS["success"],
            "Negativo": TOKENS["danger"]
        }
    )
    aplicar_layout(fig_mom, "Crescimento Mensal (MoM)", "MoM Growth (%)")
    fig_mom.update_yaxes(ticksuffix="%")
    st.plotly_chart(fig_mom, use_container_width=True)

st.markdown("<hr>", unsafe_allow_html=True)

st.markdown("## 🌍 Países e Produtos")
st.markdown(
    '<div class="section-caption">Entenda a distribuição geográfica da receita e a contribuição do portfólio em ticket, lucro e margem.</div>',
    unsafe_allow_html=True
)

g5, g6 = st.columns(2)

with g5:
    fig_pais = px.bar(
        receita_por_pais,
        x="Country",
        y="Sales",
        color="Country",
        text_auto=".2s",
        color_discrete_sequence=PRODUCT_PALETTE
    )
    aplicar_layout(fig_pais, "Receita Líquida por País", "Receita")
    fig_pais.update_yaxes(tickprefix="R$ ")
    st.plotly_chart(fig_pais, use_container_width=True)

with g6:
    fig_mix = px.pie(
        mix_produtos,
        names="Product",
        values="Profit",
        color="Product",
        color_discrete_sequence=PRODUCT_PALETTE,
        hole=0.45
    )
    fig_mix.update_traces(
        textinfo="percent+label",
        marker=dict(line=dict(color=TOKENS["card"], width=2))
    )
    aplicar_layout(fig_mix, "Mix de Lucro por Produto")
    st.plotly_chart(fig_mix, use_container_width=True)

g7, g8 = st.columns(2)

with g7:
    fig_ticket = px.bar(
        ticket_por_produto.sort_values("Average Ticket", ascending=False),
        x="Product",
        y="Average Ticket",
        color="Product",
        text_auto=".2s",
        color_discrete_sequence=PRODUCT_PALETTE
    )
    aplicar_layout(fig_ticket, "Ticket Médio por Produto", "Ticket Médio")
    fig_ticket.update_yaxes(tickprefix="R$ ")
    st.plotly_chart(fig_ticket, use_container_width=True)

with g8:
    fig_eff = px.bar(
        eficiencia_produto.sort_values("Gross Profit Margin", ascending=False),
        x="Product",
        y="Gross Profit Margin",
        color="Product",
        text_auto=".2%",
        color_discrete_sequence=PRODUCT_PALETTE
    )
    aplicar_layout(fig_eff, "Margem Bruta Média por Produto", "Margem Bruta")
    fig_eff.update_yaxes(tickformat=".0%")
    st.plotly_chart(fig_eff, use_container_width=True)

st.markdown("<hr>", unsafe_allow_html=True)

# =========================
# TABELAS
# =========================
st.markdown("## 📋 Tabelas Analíticas")
st.markdown(
    '<div class="section-caption">Explore dados agregados por produto, país e também a base detalhada após a aplicação dos filtros.</div>',
    unsafe_allow_html=True
)

aba1, aba2, aba3 = st.tabs(["Produtos", "Países", "Base Filtrada"])

with aba1:
    tabela_produtos = ticket_por_produto.sort_values("Average Ticket", ascending=False).copy()
    tabela_produtos["Sales"] = tabela_produtos["Sales"].map(formatar_moeda)
    tabela_produtos["Average Ticket"] = tabela_produtos["Average Ticket"].map(formatar_moeda)
    tabela_produtos["Units Sold"] = tabela_produtos["Units Sold"].map(formatar_numero)
    st.dataframe(tabela_produtos, use_container_width=True)

with aba2:
    tabela_paises = receita_por_pais.copy()
    tabela_paises["Sales"] = tabela_paises["Sales"].map(formatar_moeda)
    st.dataframe(tabela_paises, use_container_width=True)

with aba3:
    st.dataframe(df_filtrado, use_container_width=True)

st.markdown("---")
st.caption(
    f"Modo atual do app: {'Dark' if TOKENS['is_dark'] else 'Light'} • Dashboard com tema adaptável e experiência executiva."
)