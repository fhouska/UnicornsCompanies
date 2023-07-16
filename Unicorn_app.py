import streamlit as st
from streamlit_option_menu import option_menu
import numpy as np
import pandas as pd
from PIL import Image

#to make graphs
import matplotlib.pyplot as plt
import seaborn as sns

#to make the plotly graphs
import plotly.graph_objs as go
import plotly.express as px

#to make maps
import geopandas as gpd

# warnings
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=RuntimeWarning)


# ------- CONFIGURACION DE LA PAGINA---------------------------------------#
st.set_page_config(page_title="Empresas unicornios",page_icon="🦄",layout= 'wide')
# """(para que no nos muestre (los waring) lo que cabia de streamlist y nos muestre solo lo que hagamos)"""
st.set_option('deprecation.showPyplotGlobalUse', False)

image = Image.open('picture/Titulo.png')
st.sidebar.image(image, caption='',width=300)




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


# ------- DATA FRAME -----------------------------------------------------------------------------------------------------------------------------------#
unicorns = pd.read_csv('Data/unicorns_final.csv')
colors = ['#8ECCE6','#85BB89','#F6E691','#FDA7C0','#A977A8']


# ------- Side Barr -------------------------------------------------------------------------------------------------------------------------------------#
with st.sidebar:
    selected = option_menu(
        menu_title= None,
        options= ['Introducción','Situación Actual','Datos Históricos','Probando Hipótesis','Machine Learning','Conclusión'],
        icons= ["house", "bar-chart", "bar-chart-fill", "clipboard2-check", "wrench","card-checklist"],
        )
    
st.sidebar.title (' ')


# ------- CONTENIDO --------------------------------------------------------------------------------------------------------------------------------------#
if selected == 'Introducción':
    st.markdown("<h2 style='text-ana: center; color: #7B1C79;'>Introducción</h2>", unsafe_allow_html=True)
    "aca va algo"

if selected == 'Situación Actual':
    st.markdown("<h2 style='text-ana: center; color: #7B1C79;'>Situación Actual</h2>", unsafe_allow_html=True)

    "aca va algo"

    # # Ruta al archivo HTML
    # archivo_html = "Data/mapa.html"

    # # Leer el archivo HTML con la codificación UTF-8
    # with open(archivo_html, 'r', encoding='utf-8') as f:
    #     contenido_html = f.read()

    # # Generar el código HTML con CSS para centrar el mapa
    # html_centrado = f"""
    # <style>
    # .container {{
    #     display: flex;
    #     justify-content: center;
    #     align-items: center;
    #     height: 100vh;
    # }}
    # </style>

    # <div class="container">
    #     {contenido_html}
    # </div>
    # """

    # # Mostrar el mapa centrado en Streamlit
    # st.components.v1.html(html_centrado, width=1000, height=750)


    # ------- ESTILO DE LA PAGINA ---------------------------------------------#
    datos2023 = unicorns[unicorns['Year']==2023]
    empresas_count = datos2023[['Year','Country']].value_counts().sort_values(ascending=True)

    df_empresas_count = pd.DataFrame(empresas_count)
    df_empresas_count = df_empresas_count.reset_index()
    adam = gpd.read_file("Data/countries.geojson")
    fig3 = px.choropleth_mapbox(df_empresas_count, geojson=adam, featureidkey='properties.ADMIN', locations="Country", color='count',
                                color_continuous_scale=colors,title = " ", zoom=1, hover_data=['Country', 'count'],
                                mapbox_style="carto-positron", width=900, height=500, center = {"lat": 32.0242, "lon": 6.8227})
    fig3.update(layout_coloraxis_showscale=True)
    fig3.update_layout(paper_bgcolor="#7B1C79", font_color="#fff", title_font_size=40, title_x=0.5)
    fig3.update_layout(legend=dict(title=""))
    fig3.update_layout(margin=dict(l=10, r=8, t=8, b=8))
    st.plotly_chart(fig3)


# TABLERO POWER BI
    link = '<iframe title="Unicorn_Companies" width="100%" height="641.5" src="https://app.powerbi.com/view?r=eyJrIjoiYjI3YjU2NmMtY2QwYi00ZmI3LTgwNmEtOGQ2ZGJmYWZlMzhhIiwidCI6IjhhZWJkZGI2LTM0MTgtNDNhMS1hMjU1LWI5NjQxODZlY2M2NCIsImMiOjl9" frameborder="0" allowFullScreen="true"></iframe>'
    st.markdown(link, unsafe_allow_html=True)


if selected == 'Datos Históricos':
    st.markdown("<h2 style='text-ana: center; color: #7B1C79;'>Datos Históricos</h2>", unsafe_allow_html=True)
    
    "aca va algo"


if selected == 'Probando Hipótesis':
    st.markdown("<h2 style='text-ana: center; color: #7B1C79;'>Probando Hipótesis</h2>", unsafe_allow_html=True)
    
    "aca va algo"

if selected == 'Machine Learning':
    st.markdown("<h2 style='text-ana: center; color: #7B1C79;'>Machine Learning</h2>", unsafe_allow_html=True)
    
    "aca va algo"

if selected == 'Conclusión':
    st.markdown("<h2 style='text-ana: center; color: #7B1C79;'>Conclusión</h2>", unsafe_allow_html=True)
    
    "aca va algo"








