import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

# 1. CONFIGURAÇÃO DE PÁGINA E SEO
st.set_page_config(
    page_title="Mestre da RAM | Gustavo Meneses",
    page_icon="🧠",
    layout="wide"
)

# --- CSS ESTILO KABUM (ALTO CONTRASTE) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700;900&display=swap');
    .stApp { background-color: #0b0d10; color: #f2f2f2; font-family: 'Roboto', sans-serif; }
    
    /* Sidebar Textos Brancos */
    [data-testid="stSidebar"] .st-at, [data-testid="stSidebar"] label p, 
    [data-testid="stSidebar"] span[data-testid="stWidgetLabel"] p {
        color: #FFFFFF !important; font-weight: 700 !important; opacity: 1 !important;
    }

    /* Card de Produto */
    .product-card {
        background-color: #ffffff; border-radius: 8px; padding: 16px; color: #333;
        text-align: left; min-height: 500px; display: flex; flex-direction: column;
        justify-content: space-between; border: 1px solid #e0e0e0;
    }
    .product-title { font-size: 0.95rem; font-weight: 700; color: #42464d; height: 60px; overflow: hidden; }
    .price-new { font-size: 1.8rem; color: #ff6500; font-weight: 900; }
    
    /* Botão KaBuM Style */
    div.stButton > button {
        background-color: #ff6500 !important; color: white !important;
        font-weight: 900 !important; text-transform: uppercase; width: 100%;
        padding: 12px 0 !important; border-radius: 4px !important;
    }
    header, footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# 2. CONEXÃO COM BASE DE DADOS (GOOGLE SHEETS)
# Substitua pela URL da sua planilha pública ou use o segredo do Streamlit
url_planilha = "SUA_URL_DA_PLANILHA_AQUI" 

try:
    conn = st.connection("gsheets", type=GSheetsConnection)
    df = conn.read(spreadsheet=url_planilha)
except:
    # Dados de backup caso a planilha não esteja conectada
    df = pd.DataFrame([
        {"id": 1, "nome": "RAM Husky Impulse 16GB 3200MHz", "preco_de": 79.9, "preco": 55.9, "tipo": "DDR4", "url_stripe": "https://stripe.com", "url_img": "https://images.unsplash.com/photo-1562976540-1502c2145186?w=400"},
        {"id": 2, "nome": "RAM Fury Beast 32GB 5600MHz", "preco_de": 159.9, "preco": 125.9, "tipo": "DDR5", "url_stripe": "https://stripe.com", "url_img": "https://images.unsplash.com/photo-1591405351990-4726e331f141?w=400"}
    ])

# --- HEADER ---
st.markdown('<div style="text-align:center; background:#15191e; padding:2rem; border-bottom:4px solid #ff6500;">'
            '<h1 style="color:#ff6500; font-size:3rem; font-weight:900; margin:0;">MESTRE DA RAM</h1>'
            '<p style="color:white; letter-spacing:3px;">BY GUSTAVO MENESES</p></div>', unsafe_allow_html=True)

# --- NAVEGAÇÃO ---
tab_loja, tab_blog = st.tabs(["🛒 LOJA", "📖 BLOG TÉCNICO"])

with tab_loja:
    col_sid, col_main = st.columns([1, 4])
    
    with col_sid:
        st.write("TECNOLOGIA:")
        tipo = st.radio("Filtro", ["Todas", "DDR4", "DDR5"], label_visibility="collapsed")
        st.divider()
        st.success("✅ Site Seguro")

    with col_main:
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
                # Integração de Pagamento Direta
                st.link_button("🛒 COMPRAR AGORA", row.url_stripe)

with tab_blog:
    st.markdown("## 📖 Blog do Mestre da RAM")
    st.write(f"Artigos exclusivos por **Gustavo Meneses** para turbinar seu conhecimento.")
    
    with st.expander("DDR4 ou DDR5: Qual o melhor custo-benefício em 2026?"):
        st.write("""
        Texto focado em SEO: Ao procurar por memória RAM de alta qualidade, o Mestre da RAM (Gustavo Meneses) 
        recomenda analisar a frequência... (insira aqui 300 palavras sobre o tema para o Google te achar).
        """)
