import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

# 1. CONFIGURAÇÃO DE PÁGINA
st.set_page_config(
    page_title="Mestre da RAM | Gustavo Meneses",
    page_icon="🧠",
    layout="wide"
)

# --- CSS DEFINITIVO: ESTILO KABUM (ALTO CONTRASTE) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700;900&display=swap');

    /* Fundo Escuro */
    .stApp {
        background-color: #0b0d10;
        color: #ffffff;
        font-family: 'Roboto', sans-serif;
    }

    /* HEADER LARANJA */
    .header-box {
        text-align: center;
        padding: 2.5rem 0;
        background-color: #15191e;
        border-bottom: 4px solid #ff6500;
        margin-bottom: 2rem;
    }

    /* --- FILTROS NA SIDEBAR (TEXTO BRANCO PURO) --- */
    [data-testid="stSidebar"] {
        background-color: #15191e !important;
        border-right: 2px solid #ff6500;
    }
    
    /* Força brancos nos labels, rádio buttons e checkboxes */
    [data-testid="stSidebar"] label p, 
    [data-testid="stSidebar"] .st-at, 
    [data-testid="stSidebar"] .st-ae,
    [data-testid="stSidebar"] p {
        color: #ffffff !important;
        font-weight: 700 !important;
        font-size: 1.1rem !important;
        opacity: 1 !important;
    }

    /* CARDS DOS PRODUTOS */
    .product-card {
        background-color: #ffffff;
        border-radius: 8px;
        padding: 16px;
        color: #333333;
        text-align: left;
        min-height: 520px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        border: 1px solid #e0e0e0;
        margin-bottom: 20px;
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

    /* BOTÃO DE COMPRA KABUM */
    div.stButton > button {
        background-color: #ff6500 !important;
        color: #ffffff !important;
        border: none !important;
        font-weight: 900 !important;
        text-transform: uppercase;
        width: 100%;
        padding: 15px 0 !important;
        border-radius: 4px !important;
        font-size: 1.1rem !important;
        cursor: pointer;
    }

    div.stButton > button:hover {
        background-color: #e55a00 !important;
        box-shadow: 0px 4px 15px rgba(255, 101, 0, 0.4);
    }

    /* Esconder Menu Nativo */
    header, footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# 2. CONEXÃO COM A TUA PLANILHA GOOGLE
# Link que forneceste integrado aqui:
url_planilha = "https://docs.google.com/spreadsheets/d/1nHIsdJqvxiXG2Y-LTpBY0JDYsRXVRr1CQCdHzDIntB0/edit?usp=sharing"

try:
    conn = st.connection("gsheets", type=GSheetsConnection)
    df = conn.read(spreadsheet=url_planilha)
except Exception as e:
    st.error("Erro ao ligar à planilha. Verifica se ela está 'Pública' (Qualquer pessoa com o link).")
    st.stop()

# --- ESTRUTURA VISUAL DO SITE ---

# Topo
st.markdown(f"""
    <div class="header-box">
        <h1 style="color: #ff6500; margin-bottom: 0; font-size: 3.5rem; font-weight: 900;">MESTRE DA RAM</h1>
        <p style="color: #ffffff; letter-spacing: 4px; font-weight: 700;">CURADORIA TÉCNICA: GUSTAVO MENESES</p>
    </div>
    """, unsafe_allow_html=True)

# Navegação e Filtros
col_sidebar, col_main = st.columns([1, 4])

with col_sidebar:
    st.markdown('<p style="color:#ff6500; font-weight:900; font-size:1.2rem;">🔍 FILTROS</p>', unsafe_allow_html=True)
    
    st.write("ORDENAR POR:")
    st.selectbox("Selecione", ["Lançamentos", "Menor Preço", "Maior Preço"], label_visibility="collapsed")
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.write("TECNOLOGIA:")
    tipo_filtro = st.radio("Filtro_Tec", ["Todas", "DDR4", "DDR5"], label_visibility="collapsed")
    
    st.divider()
    st.checkbox("PRODUTOS EM STOCK", value=True)

with col_main:
    st.markdown('<h2 style="color: #ffffff; margin-bottom: 25px;">🔥 OFERTAS EM DESTAQUE</h2>', unsafe_allow_html=True)
    
    # Lógica de Filtro baseada na coluna 'tipo' da tua planilha
    if tipo_filtro != "Todas":
        df_display = df[df['tipo'] == tipo_filtro]
    else:
        df_display = df

    # Grid de Produtos (3 colunas)
    cols = st.columns(3)
    
    for i, row in enumerate(df_display.itertuples()):
        with cols[i % 3]:
            # Card Visual
            st.markdown(f"""
                <div class="product-card">
                    <img src="{row.url_img}" style="width:100%; border-radius: 4px; height: 200px; object-fit: cover;">
                    <div class="product-title">{row.nome}</div>
                    <div>
                        <div class="price-old">€ {row.preco_de:.2f}</div>
                        <div class="price-new">€ {row.preco:.2f}</div>
                        <div style="font-size: 0.85rem; color: #42464d;">À vista no PIX ou Boleto</div>
                        <div style="font-size: 0.8rem; color: #ff6500; font-weight: bold;">Ou 10x sem juros</div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            
            # Botão funcional que usa a URL de pagamento da tua planilha
            if st.button(f"🛒 COMPRAR AGORA", key=f"btn_{row.id}"):
                st.markdown(f'<meta http-equiv="refresh" content="0;URL={row.url_stripe}">', unsafe_allow_html=True)

# --- ABA DE BLOG (Foco em SEO) ---
st.markdown("<br><br>", unsafe_allow_html=True)
with st.expander("📖 BLOG DO MESTRE: Por que a RAM certa muda o seu jogo?"):
    st.write("""
    ### Artigo por Gustavo Meneses
    Escolher uma memória RAM não é apenas sobre GBs. A latência (CL) e a frequência (MHz) 
    determinam se o seu processador vai conseguir entregar o máximo de FPS. No **Mestre da RAM**, 
    filtramos apenas componentes que passam no teste de stress...
    """)
