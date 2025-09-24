Conversation opened. 1 unread message. 

Skip to content
Using Gmail with screen readers
30 of 3,535
Para de faltar vagabundo
Inbox

Carlos Alves <cadulabr@gmail.com>
Attachments
Sep 2, 2025, 9:00 AM (6 days ago)
to me


 3 Attachments
  •  Scanned by Gmail
import streamlit as st

st.set_page_config(
    page_title="Projeto de Estilização Stramlit",
    page_icon="",
    layout="wide"
)

st.title("Projeto de estilização do streamlit")
st.subheader("Exemplo de como organizar e estilizar um app")

st.sidebar.header("Filtros")
st.sidebar.checkbox("Ativar tema escuro", key="tema")
st.sidebar.slider("Selecionar valor", 0, 100, 25)

st.metric("Vendas", "R$50.000", "+5%")
st.metric("Usuarios", "1.200", "-2%")

col1, col2, col3 = st.columns(3)

with col1:
    st.header("Coluna 1")
    st.success("Tudo certo!")
    st.button("Clique aqui")

with col2:
    st.header("Coluna 2")
    st.warning("Atenção!")
    st.radio("Escolha uma opção", ["Opção A", "Opção B", "Opção C"])

with col3:
    st.header("Coluna 1")
    st.info("In
    
    
    " \
    "formação útil")
    st.selectbox("Escolha um item", ["Item 1", "Item 2", "Item 3"])

with st.expander("Clique para ver mais detalhes"):
     st.write("Aqui dentro você pode colocar informações adicionais, gráficos ou tabelas.")
     st.checkbox("Ativar detalhe extra")
     st.text_input("Digite algo interessante")

st.markdown(
    """
    <div style='backround-color: #f9f9f9; padding: 10px; border-radius: 10px'>
    <h4 style='color: #FF5733; '>Texto colorido com estilo personalizado</h4>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("---")
st.markdown("💡 Exemplo simples de estilizção no Streamlit sem lógica complexa")
app.py
Displaying app.py.
