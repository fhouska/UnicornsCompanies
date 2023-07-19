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

# Modelo
from pycaret.regression import load_model, predict_model


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
colors = ['#8ECCE6','#85BB89','#F6E691','#FDA7C0','#A977A8','#7B1C79']


# ------- Side Barr -----------------------------------------------------------------------------------------------------------------------------------------------#
with st.sidebar:
    selected = option_menu(
        menu_title= None,
        options= ['Introducción','Análisis Exploratorio','Probando Hipótesis','Machine Learning','Conclusión'],
        icons= ["house", "bar-chart", "clipboard2-check", "wrench","card-checklist"],
        )
    
st.sidebar.title (' ')


# ------- CONTENIDO -----------------------------------------------------------------------------------------------------------------------------------------------#
 
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


if selected == 'Análisis Exploratorio':
    st.markdown("<h2 style='text-ana: center; color: #7B1C79;'>Situación Actual</h2>", unsafe_allow_html=True)
    """
    Para analizar la composición de las empresas unicornio en el presente, se utilizaron dos enfoques: 
    * un mapa de distribución y 
    * un tablero de visualización. 
    """

    tab1, tab2, tab3, tab4 = st.tabs(["**Mapa Distribución**", "**Tablero de Datos**",'**Evolución**','**Industrias**'])

    with tab1:
        st.markdown("<h3 style='text-ana: center; color: #7B1C79;'>Distribución de empresas unicornios</h3>", unsafe_allow_html=True)

        # col1, col2 = st.columns(2)
        # with col1:
        st.write("""
                     
            A continuación, presentamos un mapa que muestra la distribución de empresas unicornio por países. 
            
            Podemos observar que Estados Unidos lidera en cantidad de 
            empresas unicornio, con un total de 656, seguido de China con 171 empresas. Esta información nos brinda una perspectiva clara de los países con mayor
            concentración de empresas unicornio en el mundo.
            """)
        # with col2:
        #     datos2023 = unicorns[unicorns['Year']==2023]
        #     count_continent = datos2023.groupby(['Continent'])['Company'].count().reset_index()
        #     fig = px.pie(count_continent, values='Company', names='Continent', 
        #         template="plotly_dark", 
        #         color_discrete_sequence = colors,
        #         height=400,
        #         title="Empresas Unicornio por Continente en 2023")
            
        #     fig.update_layout({'plot_bgcolor': 'rgba(255, 255, 255, 0.4)',
        #                 'paper_bgcolor': 'rgba(255, 255, 255, 0.4)'})
            
        #     st.plotly_chart(fig,use_container_width=True)


        # Ruta al archivo HTML
        archivo_html = "Data/mapa.html"
        
        # Leer el mapa HTML con la codificación UTF-8
        with open(archivo_html, 'r', encoding='utf-8') as f:
            contenido_html = f.read()

        st.components.v1.html(contenido_html, width=1300, height=800)


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
    with tab3:
        st.markdown("<h3 style='text-ana: center; color: #7B1C79;'>Evolución</h3>", unsafe_allow_html=True)
        """
        Las empresas unicornio han experimentado un crecimiento significativo a lo largo de los años. Se puede observar una gran diferencia en el año 2020, donde el 
        número de empresas unicornio pasó de 513 a 957 en el año 2021, lo que representa un incremento significativo en un solo año.
        
        Sin embargo, al analizar las empresas que se encuentran en el top 10 en cuanto a valuación, se puede notar que la mayoría de ellas ya existían antes del año 
        2020. Solo 3 de las empresas que forman parte del top 10 ingresaron después del año 2020. Esto sugiere que las empresas que han logrado alcanzar una alta 
        valuación han sido establecidas previamente y han logrado un crecimiento sostenido en el tiempo.

        """
        years = unicorns.groupby('Year')['Company'].count().reset_index()
        custom_font = dict(family="Arial, sans-serif", size=12, color="black")
        fig1 = px.area(years, x="Year", y="Company", 
                template= "plotly_dark", 
                color_discrete_sequence = [colors[5]]
                    )
        fig1.update_layout({'plot_bgcolor': 'rgba(255, 255, 255, 0.4)',
                        'paper_bgcolor': 'rgba(255, 255, 255, 0.4)'})
        fig1.update_layout(
                title='Evolución de Epresas Unicornios',
                xaxis=dict(title='Años',tickfont=custom_font),
                yaxis=dict(title='Cantidad',tickfont=custom_font),
                showlegend=False,
                )
        fig1.update_layout(height=300)
        st.plotly_chart(fig1,use_container_width=True)
     

        top_10_2023 = unicorns[unicorns['Year']==2023].head(10)
        top_10 = top_10_2023['Company'].unique()
        data_top_10 = unicorns[unicorns['Company'].isin(top_10)]
        fig2 = px.line(data_top_10, x="Year", y="Company", color='Company', 
                color_discrete_sequence = colors,
                    )
        fig2.update_layout({'plot_bgcolor': 'rgba(255, 255, 255, 0.4)',
                        'paper_bgcolor': 'rgba(255, 255, 255, 0.4)'})
        
        fig2.update_traces(line_shape='linear', line=dict(width=8))

        fig2.update_layout(
            title='Tiempo de Empresas top 10',
            xaxis=dict(title='Años',tickfont=custom_font),
            yaxis=dict(title='',tickfont=custom_font),
            showlegend=False,
            )
        fig2.update_layout(height=300)
        st.plotly_chart(fig2,use_container_width=True)

    with tab4:
        st.markdown("<h3 style='text-ana: center; color: #7B1C79;'>Industrias</h3>", unsafe_allow_html=True)
        
        # Variable a Graficar:
        Industry_type  = unicorns.groupby(['Industry_new','Year'])['Company'].count().reset_index()
        Industry_type = Industry_type.sort_values(by='Company', ascending=True)

        # fig3 = px.bar(Industry_type[Industry_type['Year']==2023], y='Industry_new', x='Company',
        # orientation='h', 
        # template= "plotly_dark",
        # color_discrete_sequence = [colors[3]],
        # height=400    
        # )
        # fig3.update_layout(
        # title='Distribución de Industrias',
        # xaxis=dict(title='Cantidades'),
        # yaxis=dict(title=' '),
        # showlegend=False
        # )
        # fig3.update_layout({'plot_bgcolor': 'rgba(255, 255, 255, 0.4)',
        #                 'paper_bgcolor': 'rgba(255, 255, 255, 0.4)'})
        # fig3.update_layout(height=300)
        # st.plotly_chart(fig3,use_container_width=True)



        fig4 = px.area(Industry_type, x="Year", y="Company", color="Industry_new", 
            title='Población por Continentes',
            color_discrete_sequence = colors,
            template="plotly_dark")
        fig4.update_layout(
        title='Evolución de Industrias a lo Largo de los Años',
        xaxis=dict(title='Cantidades'),
        yaxis=dict(title=' '),
        showlegend=True
        )
        fig4.update_layout({'plot_bgcolor': 'rgba(255, 255, 255, 0.4)',
                        'paper_bgcolor': 'rgba(255, 255, 255, 0.4)'})
        fig4.update_layout(height=350)
        st.plotly_chart(fig4,use_container_width=True)

        # Variable a Graficar:
        valuations = unicorns.groupby(['Industry:','Year'])['Valuation ($B)'].sum().reset_index()
        valuations = valuations.sort_values(by='Valuation ($B)',ascending = False)

        fig5 = px.box(valuations, x='Industry:', y='Valuation ($B)',
             template="plotly_dark",
             color_discrete_sequence = colors
             )
        fig5.update_layout(
        title='Distribución de Valuaciones de Empresas Unicornio por Industria',
        xaxis=dict(title='Valuación'),
        yaxis=dict(title=' '),
        showlegend=False
        )
        fig5.update_layout({'plot_bgcolor': 'rgba(255, 255, 255, 0.4)',
                        'paper_bgcolor': 'rgba(255, 255, 255, 0.4)'})
        fig5.update_layout(height=350)
        st.plotly_chart(fig5,use_container_width=True)

 
    
    



if selected == 'Probando Hipótesis':
    st.markdown("<h2 style='text-ana: center; color: #7B1C79;'>Probando Hipótesis</h2>", unsafe_allow_html=True)
    
    """
    Esta sección se enfoca en realizar pruebas estadísticas. Se plantearon dos preguntas que han surgido durante la exploración y 
    el análisis de los datos.

    **1.**	¿Existe algún peso significativo en la valuación si la empresa pertenece a Estados Unidos en comparación con China?

    **2.**	Teniendo en cuenta el año 2020 fue el año de la pandemia ¿Existe algún peso significativo en la valuación si la empresa entró a la lista en ese año?

    Para responder a estas preguntas, se utilizaron dos tipos de pruebas estadísticas: el test de Shapiro-Wilk y el test de Mann-Whitney-U.

    * **Mann-Whitney-U**: se utilizó para comparar las medias de dos grupos independientes, en este caso, las empresas unicornios en Estados Unidos y China, y 
    aquellas empresas que entraron a la lista en el año 2020 y las demás. 
    * **Shapiro-Wilk**: se empleó para determinar si las variables tienen una distribución normal o no. Esto es importante para poder utilizar el test *Mann-Whitney-U* 
    ya que es un tipo de test no paramétrico.
    Para ambos test se utilizó un nivel de **significancia** de **0.05**, lo que implica que si el p-valor obtenido es menor que 0.05, se rechaza la hipótesis nula.
    """
    st.markdown("<h3 style='text-ana: center; color: #7B1C79;'>Primer A/B Testing</h3>", unsafe_allow_html=True)
    """
    *Hipótesis nula:* = No existe diferencia significativa en la valuación de las empresas unicornios si pertenecen a Estados Unidos y China.
    * Shapiro-Wilk para la valuación de empresas unicornios en Estados Unidos: **p-valores = 0.00**.
    * Shapiro-Wilk para la valuación de empresas unicornios en China: **p-valores = 0.00**.
    * Mann-Whitney-U es de **5.457875322956404e-06**.
    """
    col1, col2 = st.columns(2)
    custom_font = dict(family="Arial, sans-serif", size=12, color="black")
    with col1:
        df_valuation = unicorns[unicorns['Country'].isin(['United States', 'China'])]
        # Estados Unidos
        fig4 = px.histogram(
            df_valuation[df_valuation['Country'] == 'United States'],
            x="Valuation ($B)",
            nbins=20,
            log_y=True,
            color_discrete_sequence = [colors[0]],
            template="plotly_dark"
            )
        fig4.update_layout(
                            title='Distribución de Valuación en Estados Unidos',
                            xaxis=dict(title='Valuación',tickfont=custom_font),
                            yaxis=dict(title=' '),
                            bargap=0.1,
                            showlegend=True 
                            )
        fig4.update_layout({'plot_bgcolor': 'rgba(255, 255, 255, 0.4)',
                        'paper_bgcolor': 'rgba(255, 255, 255, 0.4)'})
        
        fig4.update_layout(width=400, height=350)
        st.plotly_chart(fig4,use_container_width=True)
    with col2:
        # China
        fig5 = px.histogram(
            df_valuation[df_valuation['Country'] == 'China'],
            x="Valuation ($B)",
            nbins=20,
            log_y=True,
            color_discrete_sequence = [colors[1]],
            template="plotly_dark"
        )

        fig5.update_layout(
                            title='Distribución de Valuación en China',
                            xaxis=dict(title='Valuación',tickfont=custom_font),
                            yaxis=dict(title=' '),
                            bargap=0.1,
                            showlegend=True 
                            )
        fig5.update_layout({'plot_bgcolor': 'rgba(255, 255, 255, 0.4)',
                        'paper_bgcolor': 'rgba(255, 255, 255, 0.4)'})
        fig5.update_layout(width=400, height=350)
        st.plotly_chart(fig5,use_container_width=True)

    
    """
    **Conclusión**: 

    Según el test Shapiro-Wilk y las gráficas podemos ver que las valuaciones en ambos países no siguen una distribución normal.
    
    Dado que el p-valor de Mann-Whitney-U es menor que 0.05 **se rechaza la hipótesis nula** y se puede afirmar que hay una diferencia significativa en la valuación de 
    las empresas unicornios entre ambos países.     
    """
    st.markdown("<h3 style='text-ana: center; color: #7B1C79;'>Segundo A/B Testing</h3>", unsafe_allow_html=True)

    """
    *Hipótesis nula:* No existe diferencia significativa en la valuación de las empresas unicornios si pertenecen al 2020 o el resto de los años.
    * Shapiro-Wilk para la valuación de empresas unicornios en el año 2020: **p-valores = 1.634614658634899e-41**.
    * Shapiro-Wilk para la valuación de empresas unicornios en el resto de los años: **p-valores = 0.00**.
    * Mann-Whitney-U es de **0.44621711860946967**.
    """
    col1, col2 = st.columns(2)
    with col1:
        df_valuation = unicorns.copy()
    # Año 2020
        fig6 = px.histogram(
        df_valuation[df_valuation['Year'] == 2020],
        x="Valuation ($B)",
        nbins=20,
        log_y=True,
        color_discrete_sequence = [colors[0]],
        template="plotly_dark"
        )
        fig6.update_layout(
                        title='Distribución de Valuación en el año 2020',
                        xaxis=dict(title='Valuación',tickfont=custom_font),
                        yaxis=dict(title=''),
                        bargap=0.1,
                        showlegend=True,
                        )
        fig6.update_layout({'plot_bgcolor': 'rgba(255, 255, 255, 0.5)',
                        'paper_bgcolor': 'rgba(255, 255, 255, 0.5)'})
        fig6.update_layout(width=400, height=350)
        st.plotly_chart(fig6,use_container_width=True)

    with col2:
        # Resto de los años
        fig7 = px.histogram(
        df_valuation[df_valuation['Year'] != 2020],
        x="Valuation ($B)",
        nbins=20,
        log_y=True,
        color_discrete_sequence = [colors[1]],
        template="plotly_dark"
        )
        fig7.update_layout(
                        title='Distribución de Valuación en el año 2020',
                        xaxis=dict(title='Valuación',tickfont=custom_font),
                        yaxis=dict(title=''),
                        bargap=0.1,
                        showlegend=True 
                        )
        fig7.update_layout({'plot_bgcolor': 'rgba(255, 255, 255, 0.5)',
                        'paper_bgcolor': 'rgba(255, 255, 255, 0.5)'})
        fig7.update_layout(width=400, height=350)
        st.plotly_chart(fig7,use_container_width=True)


    """
    **Conclusión**:

    Según el test Shapiro-Wilk y las gráficas podemos ver que las valuaciones en ambas muestras no sigue una distribución normal.

    Dado que el p-valor de Mann-Whitney-U es mayor que 0.05 **no se puede rechazar la hipótesis nula** y no se puede afirmar que hay una diferencia significativa entre 
    la valuación de las empresas entre el año 2020 y el resto de los años.

    """


if selected == 'Machine Learning':
    st.markdown("<h2 style='text-ana: center; color: #7B1C79;'>Machine Learning</h2>", unsafe_allow_html=True)
    
    model = load_model('Data/ml_unicornios')

    st.title('Predicción de Valuación en Inversiones')


    Funding = st.slider('Inversión', min_value=1, max_value=300, value=10)

    Country = st.selectbox('País', options=['China', 'United States', 'Sweden', 'Australia', 'United Kingdom',
       'Bahamas', 'India', 'Indonesia', 'Turkey', 'Estonia', 'Germany',
       'Hong Kong', 'South Korea', 'Mexico', 'Canada', 'Netherlands',
       'France', 'Finland', 'Israel', 'Lithuania', 'Denmark', 'Belgium',
       'Colombia', 'Brazil', 'Singapore', 'Austria', 'Ireland',
       'United Arab Emirates', 'Switzerland', 'Vietnam', 'South Africa',
       'Thailand', 'Norway', 'Chile', 'Argentina', 'Bermuda', 'Japan',
       'Spain', 'Malaysia', 'Senegal', 'Philippines', 'Luxembourg',
       'Nigeria', 'Czech Republic', 'Croatia', 'Italy'])

    Industry = st.selectbox('Industria', options=['Artificial intelligence', 'Other',
       'E-commerce & direct-to-consumer', 'Fintech',
       'Internet software & services',
       'Supply chain, logistics, & delivery', 'Consumer & retail',
       'Data management & analytics', 'Edtech', 'Health', 'Hardware',
       'Auto & transportation', 'Travel', 'Cybersecurity',
       'Mobile & telecommunications', 'Artificial Intelligence'])

    Year_Founded = st.slider('Año', min_value=2002, max_value=2023, value=1)

    Years_Since_Founded = 2023 - Year_Founded
    Industry_Country = Industry  + Country
    Funding_Age_Ratio = Funding / Years_Since_Founded
    Industry_Funding = Industry + str(Funding)

    input_data = pd.DataFrame([[
        
        Funding, Industry, Country, Year_Founded, Years_Since_Founded, Industry_Country, Funding_Age_Ratio,Industry_Funding,
        
    ]], columns=['Industry', 'Country', 'Year_Founded', 'Funding','Years_Since_Founded', 'Industry_Country', 'Funding_Age_Ratio','Industry_Funding'])

    if st.button('¡Descubre el precio!'):

        prediction = predict_model(model, data=input_data)
        prediction_value = prediction["Valuation"].values[0].round(2)

        st.write(str(prediction_value) + ' euros')
        ROI = prediction['Valuation'].values[0] - Funding
        st.write('ROI: ' + str(ROI))











if selected == 'Conclusión':
    st.markdown("<h2 style='text-ana: center; color: #7B1C79;'>Conclusión</h2>", unsafe_allow_html=True)
    
    "aca va algo"








