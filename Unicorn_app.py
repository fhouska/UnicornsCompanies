import streamlit as st



# ------- CONFIGURACION DE LA PAGINA---------------------------------------#
st.set_page_config(page_title="Empresas unicornios",page_icon="🦄",layout= 'centered')
# """(para que no nos muestre (los waring) lo que cabia de streamlist y nos muestre solo lo que hagamos)"""
st.set_option('deprecation.showPyplotGlobalUse', False)

title = '<p style="font-family:Open Sans; color:Purple; font-size:60px;">EMPRESAS UNICORNIOS</p>'
st.markdown(title, unsafe_allow_html=True)

# ------- ESTILO DE LA PAGINA ---------------------------------------------#
# DEFINIMOS LA IMAGEN DE FONDO
import base64
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )

add_bg_from_local('picture/fondo2.jpg')

# Para que la imagen se vea en toda la pantalla
st.markdown(
    f"""
    <style>
    [data-testid="stHeader"] {{
    background-color: rgba(0, 0, 0, 0);
    }}
    [data-testid="stSidebar"]{{                 
    background-color: rgba(0, 0, 0, 0);
    border: 0.5px solid #ff4b4b;
        }}
    </style>
    """
 , unsafe_allow_html=True)


# DEFINIMOS LA IMAGEN DEL SIDEBAR
st.sidebar.title ('Inisde Airbnb')


# ------- ESTILO DE LA PAGINA ---------------------------------------------#