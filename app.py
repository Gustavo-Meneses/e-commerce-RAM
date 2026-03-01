import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

# 1. CONFIGURAÇÃO DE PÁGINA
st.set_page_config(
    page_title="Mestre da RAM | Gustavo Meneses",
    page_icon="🧠",
    layout="wide"
)

# --- CSS DEFINITIVO (FOCO EM LEITURA E CONTRASTE) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700;900&display=swap');

    .stApp { background-color: #0b0d10; color: #ffffff; font-family: 'Roboto', sans-serif; }

    /* BARRA LATERAL - CONTRASTE MÁXIMO */
    [data-testid="stSidebar"] {
        background-color: #15191e !important;
        border-right: 2px solid #ff6500;
    }

    /* Forçar todos os textos da sidebar para Branco Puro e Negrito */
    [data-testid="stSidebar"] section[data-testid="stSidebarNav"] span,
    [data-testid="stSidebar"] label p,
    [data-testid="stSidebar"] div[data-testid="stMarkdownContainer"] p,
    [data-testid="stSidebar"] .st-at, 
    [data-testid="stSidebar"] .st-ae {
        color: #ffffff !important;
        font-weight: 800 !important;
        font-size: 1.1rem !important;
        opacity: 1 !important;
    }

    /* Estilo dos Cards de Produto (Branco para contraste) */
    .product-card {
        background-color: #ffffff; border-radius: 8px; padding: 16px; color: #333;
        text-align: left; min-height: 480px; display: flex; flex-direction: column;
        justify-content: space-between; border: 1px solid #e0e0e0;
    }
    .price-new { font-size: 1.8rem; color: #ff6500; font-weight: 900; }

    /* Botão Laranja KaBuM */
    div.stButton > button {
        background-color: #ff6500 !important; color: white !important;
        font-weight: 900 !important; text-transform: uppercase; width: 100%;
        padding: 15px 0 !important; border-radius: 4px !important;
        border: none !important;
    }
    
    header, footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# 2. BASE DE DADOS (GOOGLE SHEETS)
# Substitui pelo teu link real quando o tiveres
url_planilha = "https://docs.google.com/spreadsheets/d/1vQYv_3nN5S7LwA_XW2X8X8X8X8X8X8/edit?usp=sharing"

try:
    conn = st.connection("gsheets", type=GSheetsConnection)
    df = conn.read(spreadsheet=url_planilha)
except:
    # Dados de exemplo se a planilha falhar
    df = pd.DataFrame([
        {"id": 1, "nome": "RAM Husky Impulse 16GB 3200MHz", "preco_de": 79.9, "preco": 52.9, "tipo": "DDR4", "url_stripe": "#", "url_img": "https://placehold.co/400x300/white/ff6500?text=RAM+DDR4"},
        {"id": 2, "nome": "RAM Kingston Fury 32GB 5600MHz", "preco_de": 159.9, "preco": 129.9, "tipo": "DDR5", "url_stripe": "#", "url_img": "https://placehold.co/400x300/white/ff6500?text=RAM+DDR5"}
    ])

# --- CONTEÚDO ---
st.markdown('<div style="text-align:center; background:#15191e; padding:2rem; border-bottom:4px solid #ff6500;">'
            '<h1 style="color:#ff6500; font-size:3.5rem; font-weight:900; margin:0;">MESTRE DA RAM</h1>'
            '<p style="color:white; letter-spacing:4px; font-weight:700;">CURADORIA: GUSTAVO MENESES</p></div>', unsafe_allow_html=True)

col_sid, col_main = st.columns([1, 4])

with col_sid:
    st.markdown('<p style="color:#ff6500; font-size:1.2rem; font-weight:900;">🔍 FILTROS</p>', unsafe_allow_html=True)
    # Criamos os textos manualmente para garantir o branco puro
    st.markdown("**TECNOLOGIA:**")
    tipo = st.radio("Selecione:", ["Todas", "DDR4", "DDR5"], label_visibility="collapsed")
    st.divider()
    st.checkbox("PRODUTOS EM STOCK", value=True)

with col_main:
    st.markdown('<h2 style="color:white;">🔥 OFERTAS DO MESTRE</h2>', unsafe_allow_html=True)
    
    filtered_df = df if tipo == "Todas" else df[df['tipo'] == tipo]
    
    cols = st.columns(3)
    for i, row in enumerate(filtered_df.itertuples()):
        with cols[i % 3]:
            st.markdown(f"""
                <div class="product-card">
                    <img src="{row.url_img}" style="width:100%; border-radius:4px; height:180px; object-fit:cover;">
                    <div style="font-weight:700; color:#42464d; height:60px; overflow:hidden; margin-top:10px;">{row.nome}</div>
                    <div>
                        <div style="text-decoration:line-through; color:gray; font-size:0.8rem;">€ {row.preco_de:.2f}</div>
                        <div class="price-new">€ {row.preco:.2f}</div>
                        <div style="font-size:0.85rem; color:#42464d;">À vista no PIX ou Boleto</div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            st.link_button("🛒 COMPRAR", row.url_stripe if row.url_stripe != "#" else "https://mestredaram.streamlit.app")

# BLOG SEO (Simplificado para evitar bagunça)
with st.expander("📝 BLOG: Dicas do Mestre para o teu Setup"):
    st.write("Aqui o Gustavo Meneses explica como o SEO ajuda a encontrar as melhores memórias RAM...")
