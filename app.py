import streamlit as st
import pandas as pd

# 1. CONFIGURAÇÃO DE SEO
st.set_page_config(
    page_title="Mestre da RAM | Gustavo Meneses",
    page_icon="🧠",
    layout="wide"
)

# --- CSS AVANÇADO PARA LIMPEZA DE LAYOUT ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Rajdhani:wght@500;700&display=swap');

    /* Reset de fundo */
    .stApp {
        background-color: #05070a;
        color: #e0e6ed;
        font-family: 'Rajdhani', sans-serif;
    }

    /* Bloco de Título Isolado */
    .header-container {
        text-align: center;
        padding: 40px 0px;
        background: linear-gradient(180deg, #0d1117 0%, #05070a 100%);
        border-bottom: 1px solid #1f2937;
        margin-bottom: 30px;
    }

    .main-title {
        font-size: 4rem !important;
        letter-spacing: 2px;
        font-weight: 700;
        color: #00d4ff;
        text-shadow: 0px 0px 15px rgba(0, 212, 255, 0.3);
        margin: 0;
    }

    .sub-title {
        color: #94a3b8;
        font-size: 1.2rem;
        text-transform: uppercase;
        letter-spacing: 4px;
    }

    /* Container do Catálogo */
    .catalog-container {
        padding: 20px;
    }

    /* Card do Produto Estilizado */
    .product-card {
        background: #0d1117;
        border: 1px solid #1f2937;
        border-radius: 12px;
        padding: 15px;
        transition: 0.3s;
        min-height: 450px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }

    .product-card:hover {
        border-color: #00d4ff;
        box-shadow: 0px 0px 20px rgba(0, 212, 255, 0.1);
    }

    .product-name {
        color: #ffffff;
        font-size: 1.4rem;
        margin: 15px 0 5px 0;
        height: 60px; /* Garante alinhamento */
        overflow: hidden;
    }

    .product-price {
        color: #00d4ff;
        font-size: 1.8rem;
        font-weight: bold;
        margin-bottom: 15px;
    }

    /* Ajuste de Botões Streamlit */
    div.stButton > button {
        width: 100%;
        border-radius: 8px;
        background: transparent;
        border: 1px solid #00d4ff;
        color: #00d4ff;
        font-weight: bold;
    }

    div.stButton > button:hover {
        background: #00d4ff;
        color: #05070a;
    }

    /* Esconder elementos desnecessários */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# 2. DADOS DOS PRODUTOS
def get_data():
    return [
        {"id": 1, "nome": "RAM Mestre DDR4 16GB 3200Mhz", "preco": 52.90, "tipo": "DDR4", "img": "https://images.unsplash.com/photo-1562976540-1502c2145186?w=400"},
        {"id": 2, "nome": "RAM Mestre DDR5 32GB 5600Mhz", "preco": 129.90, "tipo": "DDR5", "img": "https://images.unsplash.com/photo-1591405351990-4726e331f141?w=400"},
        {"id": 3, "nome": "Kit RGB Dual Channel 16GB", "preco": 79.00, "tipo": "DDR4", "img": "https://images.unsplash.com/photo-1544099858-75feeb57f0ce?w=400"},
    ]

products = get_data()

# --- LAYOUT DO TOPO (HEADER ISOLADO) ---
st.markdown(f"""
    <div class="header-container">
        <p class="sub-title">Consultoria Técnica</p>
        <h1 class="main-title">MESTRE DA RAM</h1>
        <p style="color: #4ade80; margin-top: 10px;">Curadoria por Gustavo Meneses</p>
    </div>
    """, unsafe_allow_html=True)

# --- NAVEGAÇÃO E FILTROS ---
tab_loja, tab_blog, tab_contato = st.tabs(["🛒 CATÁLOGO", "📖 ARTIGOS", "🛠️ SUPORTE"])

with tab_loja:
    # Filtro centralizado e discreto
    col_f1, col_f2, col_f3 = st.columns([1, 1, 1])
    with col_f2:
        filtro = st.radio("Selecione a Tecnologia:", ["Todas", "DDR4", "DDR5"], horizontal=True, label_visibility="collapsed")
    
    st.markdown("<br>", unsafe_allow_html=True)

    # Grid de Produtos
    cols = st.columns(3)
    
    for i, p in enumerate(products):
        if filtro == "Todas" or p['tipo'] == filtro:
            with cols[i % 3]:
                # Card visual via HTML para controle total do design
                st.markdown(f"""
                    <div class="product-card">
                        <img src="{p['img']}" style="width:100%; border-radius: 8px; height: 180px; object-fit: cover;">
                        <div class="product-name">{p['nome']}</div>
                        <div class="product-price">{p['preco']:.2f}€</div>
                    </div>
                """, unsafe_allow_html=True)
                
                # Botão funcional do Streamlit logo abaixo do card
                if st.button(f"Comprar {p['id']}", key=f"btn_{p['id']}", help="Clique para iniciar a compra"):
                    st.toast(f"A processar pedido de: {p['nome']}")

with tab_blog:
    st.markdown("### 📚 Espaço de Conhecimento")
    st.write("Em breve, conteúdos exclusivos para SEO orgânico.")

with tab_contato:
    st.markdown("### 📞 Fale com o Mestre")
    st.write("Dúvidas sobre compatibilidade com o Gustavo Meneses.")

# --- SIDEBAR LIMPA ---
with st.sidebar:
    st.markdown("### 🛒 SEU CARRINHO")
    st.write("O seu carrinho está vazio.")
    st.divider()
    st.caption("Mestre da RAM © 2026")
