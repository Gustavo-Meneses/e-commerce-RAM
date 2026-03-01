import streamlit as st
import pandas as pd

# 1. CONFIGURAÇÃO DE SEO E IDENTIDADE
st.set_page_config(
    page_title="Mestre da RAM | Upgrade por Gustavo Meneses",
    page_icon="🧠",
    layout="wide"
)

# Estilização CSS para a "Vibe" Mestre da RAM
st.markdown("""
    <style>
    /* Cores principais: Azul Neon e Cinza Espacial */
    .stApp { background-color: #05070a; color: #ffffff; }
    .product-card { 
        border: 1px solid #1e2630; 
        padding: 25px; 
        border-radius: 20px; 
        background-color: #0d1117;
        box-shadow: 0 4px 15px rgba(0,0,0,0.5);
        transition: 0.4s;
        text-align: center;
    }
    .product-card:hover { 
        border-color: #00d4ff; 
        box-shadow: 0 0 20px rgba(0, 212, 255, 0.2);
        transform: scale(1.02);
    }
    h1, h2 { color: #00d4ff; font-family: 'Inter', sans-serif; }
    .stButton>button { 
        background: linear-gradient(90deg, #00d4ff, #005fad); 
        color: white; 
        font-weight: bold;
        border: none;
        transition: 0.3s;
    }
    .stButton>button:hover { opacity: 0.8; color: white; }
    </style>
    """, unsafe_allow_html=True)

# 2. BASE DE DATOS (Preparada para Expansão)
def load_products():
    # Aqui simulamos os dados que virão da sua Google Sheet
    data = [
        {"id": 1, "nome": "Mestre DDR4 16GB 3200Mhz", "preco": 52.90, "tipo": "DDR4", "link": "#", "img": "https://placehold.co/400x300/0d1117/00d4ff?text=DDR4+PREMIUM"},
        {"id": 2, "nome": "Mestre DDR5 32GB 5600Mhz", "preco": 129.90, "tipo": "DDR5", "link": "#", "img": "https://placehold.co/400x300/0d1117/00d4ff?text=DDR5+ULTRA"},
        {"id": 3, "nome": "Kit Dual Channel RGB 16GB", "preco": 79.00, "tipo": "DDR4", "link": "#", "img": "https://placehold.co/400x300/0d1117/00d4ff?text=RGB+EDITION"},
    ]
    return pd.DataFrame(data)

df = load_products()

# 3. GESTÃO DO CARRINHO
if 'cart' not in st.session_state:
    st.session_state.cart = []

# --- CABEÇALHO ---
st.title("🧠 Mestre da RAM")
st.markdown("#### Consultoria e Peças de Alta Performance por **Gustavo Meneses**")
st.divider()

# --- NAVEGAÇÃO ---
menu = st.tabs(["🛒 Loja do Mestre", "📖 Blog & Dicas (SEO)", "🛠️ Suporte Técnico"])

with menu[0]:
    # Filtros Rápidos
    categoria = st.segmented_control("Tecnologia:", ["Todas", "DDR4", "DDR5"], default="Todas")
    
    # Lógica de Filtro
    df_filtered = df if categoria == "Todas" else df[df['tipo'] == categoria]
    
    # Exibição
    cols = st.columns(3)
    for i, row in enumerate(df_filtered.itertuples()):
        with cols[i % 3]:
            st.markdown(f'<div class="product-card">', unsafe_allow_html=True)
            st.image(row.img, use_container_width=True)
            st.subheader(row.nome)
            st.write(f"🏷️ **Investimento: {row.preco}€**")
            
            # Checkout
            st.link_button("🚀 Comprar com o Mestre", row.link)
            
            if st.button(f"Adicionar à Reserva", key=f"add_{row.id}"):
                st.session_state.cart.append({"nome": row.nome, "preco": row.preco})
                st.toast(f"{row.nome} reservado!")
            st.markdown('</div>', unsafe_allow_html=True)

with menu[1]:
    st.header("Mestre da RAM: Blog de Performance")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        ### 🚀 Como escolher a RAM ideal em 2026?
        Muitos cometem o erro de olhar apenas para a frequência (MHz). O **Mestre da RAM** (Gustavo Meneses) 
        ensina: a latência CAS (CL) é o que define a agilidade real do seu PC. 
        Para gaming, busque o equilíbrio entre clock alto e latência baixa.
        """)
    with col2:
        st.markdown("""
        ### 🔍 O que é o Tráfego Orgânico em Hardware?
        Este site foi construído para ser leve e rápido. Quanto mais conteúdo técnico publicamos aqui, 
        mais o Google nos recomenda para quem busca 'Memória RAM de qualidade'.
        """)

with menu[2]:
    st.header("Fale com o Gustavo Meneses")
    st.write("Precisa de ajuda para saber se a sua motherboard suporta DDR5?")
    st.button("Chamar o Mestre no WhatsApp")

# --- SIDEBAR RESUMO ---
with st.sidebar:
    st.image("https://placehold.co/200x100/0d1117/00d4ff?text=MESTRE+DA+RAM", use_container_width=True)
    st.header("💼 Sua Seleção")
    if st.session_state.cart:
        for item in st.session_state.cart:
            st.write(f"🔹 {item['nome']}")
        total = sum(i['preco'] for i in st.session_state.cart)
        st.divider()
        st.write(f"### Total: {total:.2f}€")
        if st.button("Limpar Tudo"):
            st.session_state.cart = []
            st.rerun()
    else:
        st.write("Sua lista está vazia.")
