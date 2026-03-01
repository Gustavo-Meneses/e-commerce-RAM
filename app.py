import streamlit as st
import pandas as pd

# 1. CONFIGURAÇÃO DE SEO E PÁGINA
st.set_page_config(
    page_title="Mestre da RAM | Gustavo Meneses",
    page_icon="🧠",
    layout="wide"
)

# --- CSS ESTILO KABUM (PRETO E LARANJA) COM ALTO CONTRASTE ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700;900&display=swap');

    /* Fundo Escuro */
    .stApp {
        background-color: #0b0d10;
        color: #f2f2f2;
        font-family: 'Roboto', sans-serif;
    }

    /* Título e Subtítulo */
    .header-box {
        text-align: center;
        padding: 2.5rem 0;
        background-color: #15191e;
        border-bottom: 4px solid #ff6500;
        margin-bottom: 2rem;
    }

    /* AJUSTE DE CONTRASTE DOS FILTROS (SIDEBAR) */
    /* Força o texto de labels e botões de rádio a ficar branco */
    [data-testid="stSidebar"] p, 
    [data-testid="stSidebar"] label, 
    [data-testid="stSidebar"] span {
        color: #ffffff !important;
        font-weight: 700 !important;
        font-size: 1rem !important;
    }
    
    /* Cor do título da seção de filtros */
    .filter-title {
        color: #ff6500 !important;
        font-weight: 900;
        text-transform: uppercase;
        margin-bottom: 15px;
    }

    /* Card de Produto Estilo Marketplace */
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

    .price-old {
        font-size: 0.8rem;
        color: #7f858d;
        text-decoration: line-through;
        margin-top: 15px;
    }

    .price-new {
        font-size: 1.8rem;
        color: #ff6500;
        font-weight: 900;
        margin: 5px 0;
    }

    .price-installments {
        font-size: 0.85rem;
        color: #42464d;
    }

    /* Botão de Compra - ALTO CONTRASTE */
    div.stButton > button {
        background-color: #ff6500 !important;
        color: #ffffff !important;
        border: none !important;
        font-weight: 900 !important;
        text-transform: uppercase;
        width: 100%;
        padding: 12px 0 !important;
        border-radius: 4px !important;
        font-size: 1.1rem !important;
        margin-top: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
    }

    div.stButton > button:hover {
        background-color: #e55a00 !important;
        transform: scale(1.02);
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
        <h1 style="color: #ff6500; margin-bottom: 0; font-size: 3.5rem; font-weight: 900;">MESTRE DA RAM</h1>
        <p style="color: #ffffff; letter-spacing: 4px; font-weight: 700;">CURADORIA TÉCNICA: GUSTAVO MENESES</p>
    </div>
    """, unsafe_allow_html=True)

# --- CORPO DO SITE ---
col_sidebar, col_main = st.columns([1, 4])

with col_sidebar:
    st.markdown('<p class="filter-title">🔍 Filtros de Busca</p>', unsafe_allow_html=True)
    
    st.write("Ordenar por:")
    st.selectbox("Selecione:", ["Lançamentos", "Menor Preço", "Maior Preço"], label_visibility="collapsed")
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.write("Tecnologia:")
    tipo = st.radio("Escolha:", ["Todas", "DDR4", "DDR5"], label_visibility="collapsed")
    
    st.divider()
    st.checkbox("Produtos em Stock", value=True)

with col_main:
    st.markdown('<h2 style="color: #ffffff; margin-bottom: 20px;">🔥 OFERTAS EM DESTAQUE</h2>', unsafe_allow_html=True)
    
    # Lógica de filtro simples
    filtered_products = products if tipo == "Todas" else [p for p in products if p['nome'].find(tipo) != -1]
    
    # Grid de 3 colunas
    cols = st.columns(3)
    
    for i, p in enumerate(filtered_products):
        with cols[i % 3]:
            st.markdown(f"""
                <div class="product-card">
                    <img src="{p['img']}" style="width:100%; border-radius: 4px; height: 180px; object-fit: cover;">
                    <div class="product-title">{p['nome']}</div>
                    <div>
                        <div class="price-old">€ {p['preco_de']:.2f}</div>
                        <div class="price-new">€ {p['preco']:.2f}</div>
                        <div class="price-installments">No boleto ou PIX</div>
                        <div style="font-size: 0.8rem; color: #ff6500; font-weight: 700;">ou 10x de € {(p['preco']*1.1)/10:.2f}</div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            
            if st.button(f"🛒 COMPRAR", key=f"btn_{p['id']}"):
                st.toast(f"🛒 {p['nome']} adicionado ao carrinho!")

# --- RODAPÉ ---
st.markdown("<br><br>", unsafe_allow_html=True)
st.divider()
st.markdown("""
    <div style="text-align: center; color: #ffffff; padding: 20px;">
        <h3 style="color: #ff6500;">O Diferencial Mestre da RAM</h3>
        <p style="max-width: 800px; margin: 0 auto;">Não vendemos apenas hardware. Gustavo Meneses analisa a latência, o barramento e a compatibilidade de cada módulo para que você tenha o máximo de FPS sem travamentos.</p>
    </div>
""", unsafe_allow_html=True)
