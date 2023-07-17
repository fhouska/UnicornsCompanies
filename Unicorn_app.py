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




# ------- ESTILO DE LA PAGINA ----------------------------------------------------------------------------------------------------------------------------------#
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


# ------- DATA FRAME ---------------------------------------------------------------------------------------------------------------------------------------------#
unicorns = pd.read_csv('Data/unicorns_final.csv')
colors = ['#8ECCE6','#85BB89','#F6E691','#FDA7C0','#A977A8']


# ------- Side Barr -----------------------------------------------------------------------------------------------------------------------------------------------#
with st.sidebar:
    selected = option_menu(
        menu_title= None,
        options= ['Introducción','Situación Actual','Datos Históricos','Probando Hipótesis','Machine Learning','Conclusión'],
        icons= ["house", "bar-chart", "bar-chart-fill", "clipboard2-check", "wrench","card-checklist"],
        )
    
st.sidebar.title (' ')


# ------- CONTENIDO -----------------------------------------------------------------------------------------------------------------------------------------------#
################----INTRODUCCION---################ 
if selected == 'Introducción':
    st.markdown("<h2 style='text-ana: center; color: #7B1C79;'>Introducción</h2>", unsafe_allow_html=True)
    
    st.markdown("<h3 style='text-ana: center; color: #7B1C79;'>¿Por qué elegir analizar las empresas unicornios?</h3>", unsafe_allow_html=True)
    """
    Seleccioné este tema debido a mi curiosidad y la relevancia que tienen las empresas unicornio en el mundo empresarial y tecnológico actual. Las empresas unicornio 
    son reconocidas por su capacidad para innovar y liderar en el ámbito tecnológico. 

    A través de este análisis, mi objetivo es identificar y explorar estas empresas, comprender en qué áreas específicas operan y determinar qué países presentan una 
    mayor concentración de estas organizaciones.
    """

    st.markdown("<h3 style='text-ana: center; color: #7B1C79;'>¿Qué es una empresa unicornio?</h3>", unsafe_allow_html=True)
    """
    El término "unicornio" fue utilizado por primeva vez en un artículo publicado en *TechCrunch* por *Aileen Lee* para *Cowboy Ventures*."""
    link_text = "[Ver publicación aquí](https://techcrunch.com/2013/11/02/welcome-to-the-unicorn-club/)"
    st.markdown(link_text, unsafe_allow_html=True)

    """Se utiliza para describir a aquellas empresas startups que alcanzan una valuación de mercado de **1 mil millones de dólares** antes 
    de salir a bolsa o ser adquiridas por otra empresa en un período relativamente corto, por lo general menos de **10 años**.
    """

    st.markdown("<h3 style='text-ana: center; color: #7B1C79;'>¿Dónde se obtienen los datos?</h3>", unsafe_allow_html=True)
    """
    Para llevar a cabo este análisis, se recopilaron datos de una plataforma de análisis de negocios globales conocida como ***CB Insights***. Esta plataforma 
    proporciona información y cuenta con una base de datos global de empresas privadas. 

    Dado que CB Insights solo muestra datos de la situación actual y no ofrece datos históricos, se recopiló información adicional de diferentes fuentes. 
    
    Para los años **2015 a 2022**, los datos se obtuvieron de **Kaggle**, donde también se utilizó **CB Insights** como fuente primaria"""
    link_2015_2021 = "[2015-2021- Kaggle](https://www.kaggle.com/datasets/cheeann290/unicorn)"
    st.markdown(link_2015_2021, unsafe_allow_html=True)
    link_2022 = "[2022- Kaggle](https://www.kaggle.com/datasets/rajkumarpandey02/complete-list-of-unicorn-companies)"
    st.markdown(link_2022, unsafe_allow_html=True)
    """
    Para los datos del año **2023**, se accedió directamente al sitio web de **CB Insights** para obtener la información más actualizada.
    """
    link_2023 = "[2023 - Cb Insights](https://www.cbinsights.com/research-unicorn-companies)"
    st.markdown(link_2023, unsafe_allow_html=True)

    st.markdown("<h3 style='text-ana: center; color: #7B1C79;'>Dataset Final:</h3>", unsafe_allow_html=True)
    """
    Luego de procesar nuesto los datos obtenemos el siguiente dataset:

    (Primeras 10 filas)
    """
    st.write(unicorns.head(10),width=0.7)


if selected == 'Situación Actual':
    st.markdown("<h2 style='text-ana: center; color: #7B1C79;'>Situación Actual</h2>", unsafe_allow_html=True)
    """
    Para analizar la composición de las empresas unicornio en el presente, se utilizaron dos enfoques: 
    * un mapa de distribución y 
    * un tablero de visualización. 
    """

    tab1, tab2 = st.tabs(["**Distribución de empresas unicornios**", "**Tablero de datos**"])

    with tab1:
        st.markdown("<h3 style='text-ana: center; color: #7B1C79;'>Distribución de empresas unicornios</h3>", unsafe_allow_html=True)
        """
        A continuación, presentamos un mapa que muestra la distribución de empresas unicornio por países. 
        
        Podemos observar que Estados Unidos lidera en cantidad de 
        empresas unicornio, con un total de 656, seguido de China con 171 empresas. Esta información nos brinda una perspectiva clara de los países con mayor
        concentración de empresas unicornio en el mundo.
        """
        
        # Ruta al archivo HTML
        archivo_html = "Data/mapa.html"
        
        # Leer el mapa HTML con la codificación UTF-8
        with open(archivo_html, 'r', encoding='utf-8') as f:
            contenido_html = f.read()

        st.components.v1.html(contenido_html, width=1000, height=700)

    with tab2:

        # TABLERO POWER BI
        st.markdown("<h3 style='text-ana: center; color: #7B1C79;'>Tablero de datos</h3>", unsafe_allow_html=True)
        """
        Este tablero interactivo es creado con Power BI para visualizar y comprender la composición de las empresas unicornio en la actualidad.

        Se puede observar los diferentes gráficos y visualizaciones que brindan información sobre las empresas unicornio en términos de su país de origen, sector 
        de actividad, valoración financiera y otros aspectos relevantes.
        """

        link = '<iframe title="Unicorn_Companies" width="100%" height="641.5" src="https://app.powerbi.com/view?r=eyJrIjoiYjI3YjU2NmMtY2QwYi00ZmI3LTgwNmEtOGQ2ZGJmYWZlMzhhIiwidCI6IjhhZWJkZGI2LTM0MTgtNDNhMS1hMjU1LWI5NjQxODZlY2M2NCIsImMiOjl9" frameborder="0" allowFullScreen="true"></iframe>'
        st.markdown(link, unsafe_allow_html=True)

        """
        **Empresas**

        A Mayo 2023 se identifican **1.215** empresas que entran en la categoría de empresas unicornios, entre todas totalizan una exorbitante valuación 
        de **$ 3.865mil millones**.

        Dentro del tablero se puede identificar un listado con las 10 empresas con valoración mas alta. De estas se destacan 3 empresa empresas que sobrepasan 
        los $100 mil millones esas son: 
        * **Bytedance (TikTok)** con un capital de $225 mil millones se ha convertido en una aplicación popular a nivel mundial.
        * **SpaceX** con un capital de $137mil millones ha revolucionado la industria aeroespacial y ahora con su enfoque de colonizar Marte y los viajes turísticos 
        aeroespaciales han generado gran interés en el mundo.
        * **Shein** con un capital de $100 mil millones se ha destacado en el mercado de la moda con su modelo de negocio basado en la venta directa al consumidor y 
        una amplia variedad de productos accesibles y de tendencia.

        Por último para destacar la última empresa en ingresar a esta categoría de unicornio es la empresa **Avenue One**. Esta empresa proporciona una plataforma 
        tecnológica para servicios de administración de propiedades.""" 
        link_Avenue_One = "[web_Avenue_On]( https://www.avenue.one/#platform)"
        st.markdown(link_Avenue_One, unsafe_allow_html=True)

        """
        **Industrias**

        Se observa que la **industria tecnológica** tiene una presencia significativa en el mundo de las empresas unicornio. Al considerar el conteo de empresas en 
        función de su categoría, se identificaron dos categorías principales que representan una parte considerable del total: 
        Primero **"Internet Software & Services"**  representa aproximadamente el 30%  y en segundo lugar a **"Finance Technology"** que representa alrededor del 
        18% del total de empresas unicornio. Estas dos categorías en conjunto representan casi la mitad de todas las empresas unicornio.

        """


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








