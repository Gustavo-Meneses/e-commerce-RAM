import streamlit as st
import pandas as pd

# 1. CONFIGURAÇÃO DE SEO E IDENTIDADE
st.set_page_config(
    page_title="Mestre da RAM | Upgrade por Gustavo Meneses",
    page_icon="🧠",
    layout="wide"
)

# --- CSS CUSTOMIZADO (O "BANHO DE LOJA") ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');

    /* Fundo e Fonte Global */
    .stApp {
        background: radial-gradient(circle at top, #0d1117 0%, #010409 100%);
        font-family: 'Inter', sans-serif;
        color: #c9d1d9;
    }

    /* Estilo do Título Principal */
    .main-title {
        font-size: 3.5rem !important;
        font-weight: 900 !important;
        background: linear-gradient(90deg, #00d4ff, #005fad);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0px !important;
        text-align: center;
    }

    .sub-title {
        text-align: center;
        color: #8b949e;
        font-size: 1.2rem;
        margin-bottom: 40px;
    }

    /* Card do Produto */
    .product-card {
        background: rgba(22, 27, 34, 0.8);
        border: 1px solid #30363d;
        border-radius: 16px;
        padding: 20px;
        transition: all 0.3s ease;
        text-align: center;
        height: 100%;
    }

    .product-card:hover {
        border-color: #58a6ff;
        transform: translateY(-8px);
        box-shadow: 0 10px 30px rgba(0, 212, 255, 0.15);
    }

    /* Imagem do Produto */
    .product-img {
        border-radius: 12px;
        margin-bottom: 15px;
        border: 1px solid #21262d;
    }

    /* Botão de Compra */
    div.stButton > button {
        background: linear-gradient(135deg, #1f6feb 0%, #00d4ff 100%);
        color: white;
        border: none;
        padding: 12px 24px;
        border-radius: 10px;
        font-weight: bold;
        width: 100%;
        transition: 0.3s;
    }

    div.stButton > button:hover {
        box-shadow: 0 0 15px rgba(31, 111, 235, 0.6);
        transform: scale(1.02);
    }

    /* Sidebar Estilizada */
    section[data-testid="stSidebar"] {
        background-color: #0d1117 !important;
        border-right: 1px solid #30363d;
    }

    /* Abas (Tabs) */
    .stTabs [data-baseweb="tab-list"] {
        gap: 20px;
        justify-content: center;
    }

    .stTabs [data-baseweb="tab"] {
        background-color: transparent !important;
        border-radius: 4px;
        color: #8b949e !important;
    }

    .stTabs [aria-selected="true"] {
        color: #58a6ff !important;
        border-bottom: 2px solid #58a6ff !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. BASE DE DADOS SIMULADA
def load_products():
    data = [
        {"id": 1, "nome": "Mestre DDR4 16GB 3200Mhz", "preco": 52.90, "tipo": "DDR4", "link": "#", "img": "https://images.unsplash.com/photo-1562976540-1502c2145186?auto=format&fit=crop&q=80&w=400"},
        {"id": 2, "nome": "Mestre DDR5 32GB 5600Mhz", "preco": 129.90, "tipo": "DDR5", "link": "#", "img": "https://images.unsplash.com/photo-1591405351990-4726e331f141?auto=format&fit=crop&q=80&w=400"},
        {"id": 3, "nome": "Kit RGB Dual Channel 16GB", "preco": 79.00, "tipo": "DDR4", "link": "#", "img": "https://images.unsplash.com/photo-1544099858-75feeb57f0ce?auto=format&fit=crop&q=80&w=400"},
    ]
    return pd.DataFrame(data)

df = load_products()

if 'cart' not in st.session_state:
    st.session_state.cart = []

# --- HEADER PRINCIPAL ---
st.markdown('<h1 class="main-title">🧠 MESTRE DA RAM</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Alta performance e curadoria técnica por Gustavo Meneses</p>', unsafe_allow_html=True)

# --- NAVEGAÇÃO ---
menu = st.tabs(["🛒 Showroom", "📖 Artigos do Mestre", "🛠️ Consultoria"])

with menu[0]:
    # Filtro Centralizado
    c1, c2, c3 = st.columns([1, 2, 1])
    with c2:
        categoria = st.segmented_control("Filtrar por tecnologia:", ["Todas", "DDR4", "DDR5"], default="Todas", label_visibility="collapsed")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    df_filtered = df if categoria == "Todas" else df[df['tipo'] == categoria]
    
    # Grid de Produtos
    cols = st.columns(3)
    for i, row in enumerate(df_filtered.itertuples()):
        with cols[i % 3]:
            st.markdown(f"""
                <div class="product-card">
                    <img src="{row.img}" class="product-img" width="100%">
                    <h3 style="margin: 10px 0;">{row.nome}</h3>
                    <p style="color: #58a6ff; font-size: 1.4rem; font-weight: bold;">{row.preco:.2f}€</p>
                </div>
            """, unsafe_allow_html=True)
            
            # Botões (fora do markdown para manter funcionalidade)
            st.button(f"🚀 Comprar Agora", key=f"buy_{row.id}")
            if st.button(f"📥 Adicionar ao Carrinho", key=f"add_{row.id}"):
                st.session_state.cart.append({"nome": row.nome, "preco": row.preco})
                st.toast(f"{row.nome} adicionado!")

with menu[1]:
    st.header("📖 Blog de Performance")
    st.info("Aqui entram seus artigos para SEO orgânico. O Google adora este conteúdo!")

with menu[2]:
    st.header("🛠️ Suporte Direto")
    st.write("Fale com o Gustavo para tirar dúvidas técnicas.")

# --- SIDEBAR ---
with st.sidebar:
    st.markdown("### 🛍️ Minha Seleção")
    if st.session_state.cart:
        for item in st.session_state.cart:
            st.write(f"🔹 {item['nome']} - {item['preco']}€")
        total = sum(i['preco'] for i in st.session_state.cart)
        st.divider()
        st.markdown(f"### Total: {total:.2f}€")
        if st.button("Finalizar Pedido"):
            st.balloons()
            st.success("Redirecionando...")
    else:
        st.write("Carrinho vazio.")
