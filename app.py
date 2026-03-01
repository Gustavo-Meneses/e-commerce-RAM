import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

# 1. CONFIGURAÇÃO DE PÁGINA
st.set_page_config(
    page_title="Mestre da RAM | Gustavo Meneses",
    page_icon="🧠",
    layout="wide"
)

# --- CSS FIEL À IMAGEM 2 (PRETO/AZULADO E CARDS ESCUROS) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');

    /* Fundo Escuro Profundo */
    .stApp {
        background-color: #05070a;
        color: #ffffff;
        font-family: 'Inter', sans-serif;
    }

    /* Cabeçalho Estilizado (Logo Azul) */
    .main-header {
        text-align: center;
        padding: 2.5rem 0;
    }

    /* CARDS ESCUROS COM BORDA AZUL (IGUAL IMAGEM 2) */
    .product-card {
        background-color: #0d1117;
        border-radius: 12px;
        padding: 20px;
        border: 1px solid #1f2937;
        min-height: 480px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
    
    .product-card:hover {
        border-color: #00a3ff;
        box-shadow: 0 0 15px rgba(0, 163, 255, 0.2);
    }

    .product-title {
        font-size: 1rem;
        font-weight: 700;
        color: #e5e7eb;
        margin: 15px 0;
    }

    .price-tag {
        font-size: 1.5rem;
        color: #00a3ff;
        font-weight: 900;
    }

    /* BOTÃO AZUL GRADIENTE */
    div.stButton > button {
        background: linear-gradient(90deg, #00a3ff 0%, #0066ff 100%) !important;
        color: white !important;
        border: none !important;
        font-weight: 700 !important;
        width: 100%;
        border-radius: 8px !important;
        padding: 12px !important;
        text-transform: uppercase;
    }

    /* TEXTOS DOS FILTROS (BRANCO PURO) */
    [data-testid="stSidebar"] label p, 
    [data-testid="stSidebar"] span,
    [data-testid="stSidebar"] p {
        color: #ffffff !important;
        font-weight: 700 !important;
        opacity: 1 !important;
    }

    /* Esconder elementos desnecessários */
    header, footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# 2. CONEXÃO COM A PLANILHA (O CAMPO QUE VOCÊ PRECISAVA)
url_planilha = "https://docs.google.com/spreadsheets/d/1nHIsdJqvxiXG2Y-LTpBY0JDYsRXVRr1CQCdHzDIntB0/edit?usp=sharing"

try:
    conn = st.connection("gsheets", type=GSheetsConnection)
    df = conn.read(spreadsheet=url_planilha)
except Exception as e:
    st.error("Erro técnico: Certifique-se de que o arquivo 'requirements.txt' contém 'st-gsheets-connection'.")
    st.stop()

# --- ESTRUTURA ---

st.markdown("""
    <div class="main-header">
        <h1 style="color: #00a3ff; font-size: 3rem; font-weight: 900; margin-bottom: 0;">🔵 MESTRE DA RAM</h1>
        <p style="color: #9ca3af; font-size: 1.1rem;">Alta performance e curadoria técnica por Gustavo Meneses</p>
    </div>
""", unsafe_allow_html=True)

# Abas de Navegação
tab1, tab2, tab3 = st.tabs(["🖥️ Showroom", "📖 Artigos", "🛠️ Consultoria"])

with tab1:
    col_sid, col_main = st.columns([1, 4])

    with col_sid:
        st.markdown("### 🔍 Filtrar")
        tipo = st.radio("Tecnologia:", ["Todas", "DDR4", "DDR5"])
        st.divider()
        st.write("🛒 **Minha Seleção**")
        st.caption("Carrinho vazio.")

    with col_main:
        # Lógica de filtro baseada na sua planilha
        df_filtered = df if tipo == "Todas" else df[df['tipo'] == tipo]
        
        cols = st.columns(3)
        for i, row in enumerate(df_filtered.itertuples()):
            with cols[i % 3]:
                # Card Estilizado
                st.markdown(f"""
                    <div class="product-card">
                        <img src="{row.url_img}" style="width:100%; border-radius: 8px; height: 180px; object-fit: cover;">
                        <div class="product-title">{row.nome}</div>
                        <div class="price-tag">€ {row.preco:.2f}</div>
                    </div>
                """, unsafe_allow_html=True)
                
                # Botão que leva ao link da sua planilha
                st.link_button("🚀 Comprar Agora", row.url_stripe)

# Abas extras (Mantendo a organização da Imagem 2)
with tab2:
    st.markdown("### 📖 Blog e Dicas (SEO)")
with tab3:
    st.markdown("### 🛠️ Suporte Técnico")
