import streamlit as st
import pandas as pd

# 1. CONFIGURAÇÃO DE SEO E PÁGINA
st.set_page_config(
    page_title="Mestre da RAM | Gustavo Meneses",
    page_icon="🧠",
    layout="wide"
)

# --- CSS ESTILO KABUM (PRETO E LARANJA) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');

    /* Fundo Escuro */
    .stApp {
        background-color: #0b0d10;
        color: #f2f2f2;
        font-family: 'Roboto', sans-serif;
    }

    /* Título e Subtítulo */
    .header-box {
        text-align: center;
        padding: 2rem 0;
        background-color: #15191e;
        border-bottom: 4px solid #ff6500; /* Laranja KaBuM */
        margin-bottom: 2rem;
    }

    /* Card de Produto Estilo Marketplace */
    .product-card {
        background-color: #ffffff;
        border-radius: 8px;
        padding: 16px;
        color: #333333; /* Texto escuro no card branco para leitura fácil */
        text-align: left;
        min-height: 480px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        border: 1px solid #e0e0e0;
    }

    .product-title {
        font-size: 1rem;
        font-weight: 700;
        color: #42464d;
        height: 60px;
        overflow: hidden;
        margin-top: 10px;
    }

    .price-old {
        font-size: 0.8rem;
        color: #7f858d;
        text-decoration: line-through;
        margin-top: 15px;
    }

    .price-new {
        font-size: 1.6rem;
        color: #ff6500; /* Laranja para destaque */
        font-weight: 900;
        margin: 5px 0;
    }

    .price-installments {
        font-size: 0.85rem;
        color: #7f858d;
    }

    /* Botão de Compra - ALTO CONTRASTE */
    div.stButton > button {
        background-color: #ff6500 !important;
        color: #ffffff !important;
        border: none !important;
        font-weight: 700 !important;
        text-transform: uppercase;
        width: 100%;
        padding: 12px 0 !important;
        border-radius: 4px !important;
        font-size: 1.1rem !important;
        margin-top: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }

    div.stButton > button:hover {
        background-color: #e55a00 !important;
        color: #ffffff !important;
    }

    /* Sidebar Escura */
    [data-testid="stSidebar"] {
        background-color: #15191e;
        border-right: 2px solid #ff6500;
    }

    /* Esconder elementos nativos */
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
        <h1 style="color: #ff6500; margin-bottom: 0;">MESTRE DA RAM</h1>
        <p style="color: #94a3b8; letter-spacing: 2px;">BY GUSTAVO MENESES</p>
    </div>
    """, unsafe_allow_html=True)

# --- CORPO DO SITE ---
col_sidebar, col_main = st.columns([1, 4])

with col_sidebar:
    st.write("### FILTROS")
    st.selectbox("Ordenar por:", ["Lançamentos", "Menor Preço", "Maior Preço"])
    st.radio("Tecnologia:", ["Todas", "DDR4", "DDR5"])
    st.divider()
    st.write("✅ Produtos em Stock")

with col_main:
    st.write("### 🔥 OFERTAS EM DESTAQUE")
    
    # Grid de 3 colunas
    cols = st.columns(3)
    
    for i, p in enumerate(products):
        with cols[i % 3]:
            # Card HTML para estrutura
            st.markdown(f"""
                <div class="product-card">
                    <img src="{p['img']}" style="width:100%; border-radius: 4px; height: 180px; object-fit: cover;">
                    <div class="product-title">{p['nome']}</div>
                    <div>
                        <div class="price-old">€ {p['preco_de']:.2f}</div>
                        <div class="price-new">€ {p['preco']:.2f}</div>
                        <div class="price-installments">À vista no PIX / Boleto</div>
                        <div style="font-size: 0.8rem; color: #42464d;">ou € {(p['preco']*1.1)/10:.2f} em 10x sem juros</div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            
            # Botão Streamlit com estilo KaBuM
            if st.button(f"🛒 COMPRAR", key=f"btn_{p['id']}"):
                st.toast(f"Adicionado: {p['nome']}")

# --- RODAPÉ SEO ---
st.markdown("<br><br>", unsafe_allow_html=True)
st.divider()
st.markdown("""
    <div style="text-align: center; color: #7f858d; padding: 20px;">
        <h3>Por que comprar no Mestre da RAM?</h3>
        <p>Gustavo Meneses seleciona pessoalmente cada pente de memória, garantindo compatibilidade e performance extrema para seu setup gamer.</p>
    </div>
""", unsafe_allow_html=True)
