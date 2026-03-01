import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

# 1. CONFIGURAÇÃO DE PÁGINA
st.set_page_config(
    page_title="Mestre da RAM | Gustavo Meneses",
    page_icon="🧠",
    layout="wide"
)

# --- CSS RESTAURADO (BASEADO NA IMAGEM 2 - MODERNO E LIMPO) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');

    .stApp {
        background-color: #05070a;
        color: #ffffff;
        font-family: 'Inter', sans-serif;
    }

    /* HEADER ESTILIZADO */
    .main-header {
        text-align: center;
        padding: 3rem 0;
        background: radial-gradient(circle, #0a0f16 0%, #05070a 100%);
    }

    /* CARDS ESCUROS (ESTILO IMAGEM 2) */
    .product-card {
        background-color: #0d1117;
        border-radius: 12px;
        padding: 20px;
        border: 1px solid #1f2937;
        transition: transform 0.3s, border-color 0.3s;
        min-height: 450px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
    
    .product-card:hover {
        transform: translateY(-5px);
        border-color: #00a3ff;
    }

    .product-title {
        font-size: 1.1rem;
        font-weight: 700;
        color: #e5e7eb;
        margin: 15px 0;
        line-height: 1.4;
    }

    .price-tag {
        font-size: 1.6rem;
        color: #00a3ff;
        font-weight: 900;
        margin-bottom: 15px;
    }

    /* BOTÃO COMPRAR AGORA (AZUL DA IMAGEM 2) */
    div.stButton > button {
        background: linear-gradient(90deg, #00a3ff 0%, #0066ff 100%) !important;
        color: white !important;
        border: none !important;
        font-weight: 700 !important;
        width: 100%;
        padding: 10px !important;
        border-radius: 8px !important;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    /* AJUSTE FILTROS SIDEBAR (BRANCO PURO) */
    [data-testid="stSidebar"] { background-color: #0a0f16 !important; }
    [data-testid="stSidebar"] label p, [data-testid="stSidebar"] p {
        color: #ffffff !important;
        font-weight: 600 !important;
    }

    header, footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# 2. CONEXÃO COM A TUA PLANILHA
url_planilha = "https://docs.google.com/spreadsheets/d/1nHIsdJqvxiXG2Y-LTpBY0JDYsRXVRr1CQCdHzDIntB0/edit?usp=sharing"

try:
    conn = st.connection("gsheets", type=GSheetsConnection)
    df = conn.read(spreadsheet=url_planilha)
except:
    st.error("Erro ao carregar dados. Verifique a conexão com o Google Sheets.")
    st.stop()

# --- LAYOUT DO SITE ---

st.markdown("""
    <div class="main-header">
        <h1 style="color: #00a3ff; font-size: 3.5rem; font-weight: 900; margin: 0;">MESTRE DA RAM</h1>
        <p style="color: #9ca3af; font-size: 1.1rem;">Alta performance e curadoria técnica por Gustavo Meneses</p>
    </div>
""", unsafe_allow_html=True)

# Navegação (Tabs como na Imagem 2)
tab1, tab2, tab3 = st.tabs(["🖥️ Showroom", "📖 Artigos do Mestre", "🛠️ Consultoria"])

with tab1:
    col_sid, col_main = st.columns([1, 4])

    with col_sid:
        st.markdown("### 🔍 Filtrar")
        tipo = st.radio("Tecnologia:", ["Todas", "DDR4", "DDR5"])
        st.divider()
        st.write("🛒 **Minha Seleção**")
        st.caption("Carrinho vazio.")

    with col_main:
        df_filtered = df if tipo == "Todas" else df[df['tipo'] == tipo]
        
        cols = st.columns(3)
        for i, row in enumerate(df_filtered.itertuples()):
            with cols[i % 3]:
                st.markdown(f"""
                    <div class="product-card">
                        <img src="{row.url_img}" style="width:100%; border-radius: 8px; height: 180px; object-fit: cover;">
                        <div class="product-title">{row.nome}</div>
                        <div>
                            <div class="price-tag">€ {row.preco:.2f}</div>
                        </div>
                    </div>
                """, unsafe_allow_html=True)
                
                # Link de compra do Stripe/Gateway da planilha
                st.link_button("🚀 Comprar Agora", row.url_stripe)

with tab2:
    st.subheader("Artigos e Dicas de SEO")
    st.info("Espaço destinado aos teus textos técnicos para atrair tráfego orgânico.")

with tab3:
    st.subheader("Suporte Especializado")
    st.write("Entre em contato para uma consultoria direta com Gustavo Meneses.")
