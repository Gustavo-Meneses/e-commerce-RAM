import streamlit as st
import pandas as pd

# 1. CONFIGURAÇÃO DE SEO E PÁGINA
st.set_page_config(
    page_title="Mestre da RAM | Gustavo Meneses",
    page_icon="🧠",
    layout="wide"
)

# --- CSS ESTILO KABUM COM CONTRASTE TOTAL ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700;900&display=swap');

    /* Fundo Escuro */
    .stApp {
        background-color: #0b0d10;
        color: #f2f2f2;
        font-family: 'Roboto', sans-serif;
    }

    /* Cabeçalho */
    .header-box {
        text-align: center;
        padding: 2.5rem 0;
        background-color: #15191e;
        border-bottom: 4px solid #ff6500;
        margin-bottom: 2rem;
    }

    /* --- AJUSTE DEFINITIVO DOS FILTROS (BRANCO PURO) --- */
    /* Alvo: Rótulos de Radio Buttons, Checkboxes e Textos da Sidebar */
    [data-testid="stSidebar"] .st-at, 
    [data-testid="stSidebar"] .st-ae, 
    [data-testid="stSidebar"] .st-af,
    [data-testid="stSidebar"] label p,
    [data-testid="stSidebar"] div[data-testid="stMarkdownContainer"] p,
    [data-testid="stSidebar"] span[data-testid="stWidgetLabel"] p {
        color: #FFFFFF !important;
        font-weight: 700 !important;
        opacity: 1 !important;
        font-size: 1.05rem !important;
    }

    /* Título laranja dos Filtros */
    .filter-title {
        color: #ff6500 !important;
        font-weight: 900;
        text-transform: uppercase;
        margin-bottom: 15px;
        font-size: 1.2rem;
    }

    /* Card de Produto */
    .product-card {
        background-color: #ffffff;
        border-radius: 8px;
        padding: 16px;
        color: #333333;
        text-align: left;
        min-height: 480px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        border: 1px solid #e0e0e0;
    }

    .product-title {
        font-size: 0.95rem;
        font-weight: 700;
        color: #42464d;
        height: 60px;
        overflow: hidden;
        margin-top: 10px;
    }

    .price-new {
        font-size: 1.8rem;
        color: #ff6500;
        font-weight: 900;
        margin: 5px 0;
    }

    /* Botão de Compra */
    div.stButton > button {
        background-color: #ff6500 !important;
        color: #ffffff !important;
        border: none !important;
        font-weight: 900 !important;
        text-transform: uppercase;
        width: 100%;
        padding: 12px 0 !important;
        border-radius: 4px !important;
    }

    div.stButton > button:hover {
        background-color: #e55a00 !important;
        box-shadow: 0 0 15px rgba(255, 101, 0, 0.4);
    }

    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: #15191e;
        border-right: 2px solid #ff6500;
    }

    header {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# 2. DADOS DOS PRODUTOS
def load_data():
    return [
        {"id": 1, "nome": "Memória RAM Husky Impulse 16GB 3200MHz DDR4 CL22 Preto", "preco_de": 75.90, "preco": 52.90, "img": "https://images.unsplash.com/photo-1562976540-1502c2145186?w=400"},
        {"id": 2, "nome": "Memória RAM Kingston Fury Beast 32GB 5600MHz DDR5 Black", "preco_de": 169.90, "preco": 129.90, "img": "https://images.unsplash.com/photo-1591405351990-4726e331f141?w=400"},
        {"id": 3, "nome": "Memória RAM Corsair Vengeance RGB 16GB (2x8) DDR4 3600MHz", "preco_de": 99.00, "preco": 79.00, "img": "https://images.unsplash.com/photo-1544099858-75feeb57f0ce?w=400"},
    ]

products = load_data()

# --- HEADER ---
st.markdown("""
    <div class="header-box">
        <h1 style="color: #ff6500; margin-bottom: 0; font-size: 3.5rem; font-weight: 900;">MESTRE DA RAM</h1>
        <p style="color: #ffffff; letter-spacing: 4px; font-weight: 700;">CURADORIA TÉCNICA: GUSTAVO MENESES</p>
    </div>
    """, unsafe_allow_html=True)

# --- CORPO ---
col_sidebar, col_main = st.columns([1, 4])

with col_sidebar:
    st.markdown('<p class="filter-title">🔍 FILTROS</p>', unsafe_allow_html=True)
    
    st.write("ORDENAR POR:")
    st.selectbox("Ordenar:", ["Lançamentos", "Menor Preço", "Maior Preço"], label_visibility="collapsed")
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.write("TECNOLOGIA:")
    tipo = st.radio("Tecnologia:", ["Todas", "DDR4", "DDR5"], label_visibility="collapsed")
    
    st.divider()
    st.checkbox("PRODUTOS EM STOCK", value=True)

with col_main:
    st.markdown('<h2 style="color: #ffffff; margin-bottom: 20px;">🔥 OFERTAS EM DESTAQUE</h2>', unsafe_allow_html=True)
    
    # Grid
    cols = st.columns(3)
    for i, p in enumerate(products):
        with cols[i % 3]:
            st.markdown(f"""
                <div class="product-card">
                    <img src="{p['img']}" style="width:100%; border-radius: 4px; height: 180px; object-fit: cover;">
                    <div class="product-title">{p['nome']}</div>
                    <div>
                        <div style="font-size: 0.8rem; color: #7f858d; text-decoration: line-through;">€ {p['preco_de']:.2f}</div>
                        <div class="price-new">€ {p['preco']:.2f}</div>
                        <div style="font-size: 0.85rem; color: #42464d;">À vista no Boleto ou PIX</div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            if st.button(f"🛒 COMPRAR", key=f"btn_{p['id']}"):
                st.toast(f"Adicionado ao carrinho!")

# --- RODAPÉ ---
st.markdown("<br><br><hr>", unsafe_allow_html=True)
st.markdown('<div style="text-align: center; color: white;">Mestre da RAM © 2026 - Gustavo Meneses</div>', unsafe_allow_html=True)
