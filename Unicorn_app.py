import streamlit as st



# ------- CONFIGURACION DE LA PAGINA---------------------------------------#
st.set_page_config(page_title="Empresas unicornios",page_icon="🦄",layout= 'wide')
# """(para que no nos muestre (los waring) lo que cabia de streamlist y nos muestre solo lo que hagamos)"""
st.set_option('deprecation.showPyplotGlobalUse', False)

# ------- ESTILO DE LA PAGINA ---------------------------------------------#
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
background-color: #e5e5f7;
opacity: 0.8;
background-image:  linear-gradient(#96bd99 1px, transparent 1px), linear-gradient(to right, #96bd99 1px, #e5e5f7 1px);
background-size: 20px 20px;
}
</style>
"""
st.markdown(page_bg_img,unsafe_allow_html=True)



st.title ("**EMPRESAS UNICORNIOS**")


# ------- ESTILO DE LA PAGINA ---------------------------------------------#