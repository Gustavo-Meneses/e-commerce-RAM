import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

# 1. CONFIGURAÇÃO DE PÁGINA E SEO
st.set_page_config(
    page_title="Mestre da RAM | Gustavo Meneses",
    page_icon="🧠",
    layout="wide"
)

# --- CSS ESTILO KABUM (PRETO E LARANJA) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700;900&display=swap');
    .stApp { background-color: #0b0d10; color: #f2f2f2; font-family: 'Roboto', sans-serif; }
    [data-testid="stSidebar"] .st-at, [data-testid="stSidebar"] label p, 
    [data-testid="stSidebar"] span[data-testid="stWidgetLabel"] p {
        color: #FFFFFF !important; font-weight: 700 !important; opacity: 1 !important;
    }
    .product-card {
        background-color: #ffffff; border-radius: 8px; padding: 16px; color: #333;
        text-align: left; min-height: 500px; display: flex; flex-direction: column;
        justify-content: space-between; border: 1px solid #e0e0e0;
    }
    .product-title { font-size: 0.95rem; font-weight: 700; color: #42464d; height: 60px; overflow: hidden; }
    .price-new { font-size: 1.8rem; color: #ff6500; font-weight: 900; }
    div.stButton > button {
        background-color: #ff6500 !important; color: white !important;
        font-weight: 900 !important; text-transform: uppercase; width: 100%;
        padding: 12px 0 !important; border-radius: 4px !important;
    }
    header, footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# ==========================================================
# 2. BASE DE DADOS (CONFIGURAÇÃO DO LINK AQUI)
# ==========================================================
# COLA O LINK DA TUA PLANILHA ABAIXO (DEVE ESTAR PÚBLICA: "Qualquer pessoa com o link")
url_planilha = "https://docs.google.com/spreadsheets/d/1nHIsdJqvxiXG2Y-LTpBY0JDYsRXVRr1CQCdHzDIntB0/edit?usp=drivesdk" 

try:
    # Tentativa de ler a planilha real
    conn = st.connection("gsheets", type=GSheetsConnection)
    df = conn.read(spreadsheet=url_planilha)
except Exception as e:
    # Dados de backup para o site não ficar em branco caso o link falhe
    df = pd.DataFrame([
        {"id": 1, "nome": "RAM Husky Impulse 16GB 3200MHz", "preco_de": 79.9, "preco": 52.9, "tipo": "DDR4", "url_stripe": "https://stripe.com", "url_img": "https://images.unsplash.com/photo-1562976540-1502c2145186?w=400"},
        {"id": 2, "nome": "RAM Kingston Fury Beast 32GB 5600MHz", "preco_de": 159.9, "preco": 129.9, "tipo": "DDR5", "url_stripe": "https://stripe.com", "url_img": "https://images.unsplash.com/photo-1591405351990-4726e331f141?w=400"}
    ])

# --- CONTEÚDO DO SITE ---
st.markdown('<div style="text-align:center; background:#15191e; padding:2rem; border-bottom:4px solid #ff6500;">'
            '<h1 style="color:#ff6500; font-size:3rem; font-weight:900; margin:0;">MESTRE DA RAM</h1>'
            '<p style="color:white; letter-spacing:3px; font-weight:700;">CURADORIA TÉCNICA: GUSTAVO MENESES</p></div>', unsafe_allow_html=True)

tab_loja, tab_blog = st.tabs(["🛒 LOJA", "📖 BLOG TÉCNICO"])

with tab_loja:
    col_sid, col_main = st.columns([1, 4])
    
    with col_sid:
        st.markdown('<p style="color:#ff6500; font-weight:900;">🔍 FILTROS</p>', unsafe_allow_html=True)
        tipo = st.radio("TECNOLOGIA:", ["Todas", "DDR4", "DDR5"])
        st.divider()

    with col_main:
        # Lógica de Filtro
        filtered_df = df if tipo == "Todas" else df[df['tipo'] == tipo]
        
        cols = st.columns(3)
        for i, row in enumerate(filtered_df.itertuples()):
            with cols[i % 3]:
                st.markdown(f"""
                    <div class="product-card">
                        <img src="{row.url_img}" style="width:100%; border-radius:4px; height:180px; object-fit:cover;">
                        <div class="product-title">{row.nome}</div>
                        <div>
                            <div style="text-decoration:line-through; color:gray; font-size:0.8rem;">€ {row.preco_de:.2f}</div>
                            <div class="price-new">€ {row.preco:.2f}</div>
                            <div style="font-size:0.8rem; color:#42464d;">À vista no PIX</div>
                        </div>
                    </div>
                """, unsafe_allow_html=True)
                st.link_button("🛒 COMPRAR AGORA", row.url_stripe)

with tab_blog:
    st.header("📖 Artigos do Mestre")
    st.write("Conteúdo para SEO em desenvolvimento por Gustavo Meneses.")
