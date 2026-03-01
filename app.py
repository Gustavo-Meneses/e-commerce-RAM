import streamlit as st

# Configuração da página (SEO Básico)
st.set_page_config(page_title="TechRAM - Especialistas em Performance", layout="wide")

# 1. Inicialização do Carrinho (Armazenamento Temporário)
if 'cart' not in st.session_state:
    st.session_state.cart = []

# 2. Dados dos Produtos (Podes expandir esta lista facilmente)
products = [
    {"id": 1, "nome": "Memória RAM 16GB DDR4 3200MHz", "preco": 55.00, "tipo": "DDR4", "img": "https://placehold.co/300x200?text=DDR4+16GB"},
    {"id": 2, "nome": "Memória RAM 32GB DDR5 5200MHz", "preco": 120.00, "tipo": "DDR5", "img": "https://placehold.co/300x200?text=DDR5+32GB"},
    {"id": 3, "nome": "Memória RAM 8GB DDR4 2666MHz", "preco": 30.00, "tipo": "DDR4", "img": "https://placehold.co/300x200?text=DDR4+8GB"},
    {"id": 4, "nome": "Memória RAM RGB 16GB DDR4", "preco": 75.00, "tipo": "DDR4", "img": "https://placehold.co/300x200?text=RGB+DDR4"},
]

# --- INTERFACE DO SITE ---

st.title("🚀 TechRAM Store")
st.markdown("### Upgrade de performance para o teu PC com tráfego orgânico.")

# Barra Lateral - Carrinho de Compras
st.sidebar.header("🛒 Teu Carrinho")
if not st.session_state.cart:
    st.sidebar.write("O carrinho está vazio.")
else:
    total = 0
    for item in st.session_state.cart:
        st.sidebar.write(f"**{item['nome']}** - {item['preco']}€")
        total += item['preco']
    st.sidebar.divider()
    st.sidebar.write(f"### Total: {total:.2f}€")
    if st.sidebar.button("Finalizar Compra"):
        st.sidebar.success("Redirecionando para o Checkout (Stripe/PayPal)...")

# Filtros na página principal
st.subheader("Filtrar por Categoria")
tipo_filtro = st.selectbox("Escolha o tipo de memória:", ["Todas", "DDR4", "DDR5"])

# Lógica de Filtro
filtered_products = products if tipo_filtro == "Todas" else [p for p in products if p['tipo'] == tipo_filtro]

# Exibição dos Produtos em Colunas
cols = st.columns(3)
for idx, product in enumerate(filtered_products):
    with cols[idx % 3]:
        st.image(product['img'], use_container_width=True)
        st.subheader(product['nome'])
        st.write(f"Preço: **{product['preco']}€**")
        
        # Botão para adicionar ao carrinho
        if st.button(f"Adicionar", key=f"btn_{product['id']}"):
            st.session_state.cart.append(product)
            st.toast(f"{product['nome']} adicionado!")
            st.rerun() # Atualiza a página para mostrar no carrinho

# Rodapé para SEO Orgânico
st.divider()
st.write("🔍 **Dica Tech:** Como escolher a RAM certa? Verifique a compatibilidade da sua motherboard com DDR4 ou DDR5.")
