import streamlit as st
import requests
#from streamlit_lottie import st_lottie
from PIL import Image

st.set_page_config(page_title= 'Documentación', page_icon= '📃')

def css_load(css_file):
  with open(css_file) as file:
    st.markdown(f"<style>{file.read()}</style>", unsafe_allow_html= True)

email_contact = "romanaichino2002@gmail.com"

css_load('Style/main.css')

#funcion para animaciones
def load_lottieurl(url):
  r = requests.get(url)
  if r.status_code != 200:
    return None
  return r.json()


#lottie_coding = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_0yfsb3a1.json")
Logo_principal = Image.open("Imagenes/Logo principal.jpg")
Alcance_proyecto = Image.open("Imagenes/Alcance del proyecto.jpg")
Gantt = Image.open("Imagenes/GANTT.jpeg")
Diagrama_er = Image.open("Imagenes/diagrama er.jpg")
Diagrama_googlemaps = Image.open("Imagenes/diagrama_googlemaps.jpg")
Diagrama_yelp = Image.open("Imagenes/diagrama_yelp.jpg")
Tabla1 = Image.open("Imagenes/tabla1.png")
Tabla2 = Image.open("Imagenes/tabla2.png")
Tabla3_1 = Image.open("Imagenes/tabla3.png")
Tabla3_2 = Image.open("Imagenes/tabla3_2.png")
Tabla4 = Image.open("Imagenes/tabla4.png")
Tabla5 = Image.open("Imagenes/tabla5.png")
ciclo_dato = Image.open("Imagenes/ciclo del dato.png")

caping1 = Image.open("Imagenes/cap_ing1.jpg")
caping2 = Image.open("Imagenes/cap_ing2.jpg")
caping3 = Image.open("Imagenes/cap_ing3.jpg")
caping4 = Image.open("Imagenes/cap_ing4.jpg")

dashboard1 = Image.open("Imagenes/Dashboard 1.jpg")
dashboard2 = Image.open("Imagenes/Dashboard 2.jpg")
dashboard3 = Image.open("Imagenes/Dashboard 3.jpg")


# Crea un archivo HTML con los estilos CSS
#with open("estilos.html", "w") as f:
#    f.write("""
#    <style>
#      body {
#          background-color: #3498db; /* Color de fondo sólido */
#      }
#  </style>
#  """)

# Carga el archivo HTML con los estilos CSS
st.markdown(open("estilos.html").read(), unsafe_allow_html=True)

with st.container():
  st.write("""
    <style>
        div.stApp {
            text-align: center;
        }
    </style>
  """, unsafe_allow_html=True)

  st.subheader("Bienvenidos!! somos DREM DATA INSIGTHS, y esta es la documentación del proyecto grupal de Reviews de Yelp y Google Maps. :wave: :wave: ")
  st.title("Documentación")

with st.container():
  st.image(Logo_principal, use_column_width=True, output_format="JPEG")
  st.write("(27/08/2023 al 15/09/1023)")

with st.container():
  st.write("---")
  st.subheader("Integrantes")
  st.markdown("<p style='text-align: left; font-size: 18px;'><strong>Roman Aichino: </strong>Data Engineer<br><strong>Max Jeffer:</strong> Data Engineer & Machine Learning<br><strong>Diego Campos:</strong> Data Engineer<br><strong>Eduardo Vivar:</strong> Data Analytics</p>", unsafe_allow_html=True)

with st.container():
  st.write("---")
  st.subheader("Introducción")
  st.markdown("<p style='text-align: justify; font-size: 18px;'>Este es un proyecto que fue realizado desde la disciplina Ciencia de Datos, que busca recolectar datos para procesarlos, analizarlos y poder tomar decisiones en base a ellos. El proyecto cuenta con un EDA, una automatización del ETL en la nube ‘Google Cloud Platform’, una carga incrementa a partir de los datos de una API, un dashboard con KPIs, y por último, un modelo de Machine Learning que devuelve cual es la mejor opción para una decisión empresarial.</p>", unsafe_allow_html=True)
  #st.lottie(lottie_coding, height= 300, key = "coding")

with st.container():
  st.write("---")
  st.subheader("Quiénes Somos y Quién es nuestro cliente?")
  st.markdown("<p style='text-align: justify; font-size: 18px;'>Nosotros somos Drem Data Insights, una empresa dedicada a la ciencia de los datos, y en este proyecto en particular nuestra tarea es crear un sistema que proporcione información sobre los restaurantes en Estados Unidos, en el estado de Florida, con el objetivo de que nuestro cliente, una empresa que quiere abrir un restaurante, pueda tomar buenas decisiones en cuanto a la ubicación y otros detalles del negocio. </p>", unsafe_allow_html=True)

with st.container():
  st.write("---")
  st.subheader("Objetivos")
  st.markdown("<p style='text-align: justify; font-size: 18px;'><strong>Generales:</strong></p>", unsafe_allow_html=True)
  st.markdown("<p style='text-align: justify; font-size: 18px;'>❖	Realizar un análisis de datos para identificar atributos estratégicos, desarrollar un análisis de sentimiento y clasificar ciudades en base a sus indicadores en el sector ‘restaurantes’ para un cliente con preferencias en ciudades con menor contaminación de aire.</p>", unsafe_allow_html=True)
  st.markdown("<p style='text-align: justify; font-size: 18px;'><strong>Especificos:</strong></p>", unsafe_allow_html=True)
  st.markdown("<p style='text-align: justify; font-size: 18px;'>❖	Automatización de pipelines con ETL.<br>❖	Análisis exploratorio de los datos para la creación de KPIs.<br>❖	Automat<br>❖Diseño de un dashboard interactivo en Power Bi para realizar el seguimiento y monitoreo de los KPIs.<br>❖	Implementar una carga incremental automatizada a partir de una API.<br>❖	Análisis de sentimiento mediante un modelo de ML.</p>", unsafe_allow_html=True)

with st.container():
  st.write("---")
  st.subheader("Alcance del Proyecto")
  st.image(Alcance_proyecto, use_column_width=True, output_format="JPEG")

with st.container():
  st.write("---")
  st.subheader("Planificación")
  st.markdown("<p style='text-align: center; font-size: 21px;'><strong>Metodología Scrum: Roles y Planificación</strong></p>", unsafe_allow_html=True)
  st.markdown("<p style='text-align: justify; font-size: 21px;'><strong>Roles en Scrum</strong></p>", unsafe_allow_html=True)
  st.markdown("<p style='text-align: justify; font-size: 18px;'><strong>❖	Product Owner:</strong><br>Responsable de definir y priorizar el Product Backlog.<br>          Asegura que el equipo trabaje en las tareas más valiosas para el cliente.<br>          Colabora con interesados y el equipo para mantener la visión clara del producto.<br>          Asegura que el equipo trabaje en las tareas más valiosas para el cliente.<br>          Colabora con interesados y el equipo para mantener la visión clara del producto.</p>", unsafe_allow_html=True)
  st.markdown("<p style='text-align: justify; font-size: 18px;'><strong>❖	Scrum Master:</strong><br>Facilitadora del proceso Scrum.<br>          Garantiza que el equipo siga las prácticas y principios de Scrum.<br>          Elimina obstáculos y fomenta un entorno de trabajo colaborativo.</p>", unsafe_allow_html=True)
  st.markdown("<p style='text-align: justify; font-size: 18px;'><strong>❖	Equipo de Desarrollo:</strong><br>Campos Diego<br>Aichino Roman<br>Jeffer Max<br>Vivar Eduardo</p>", unsafe_allow_html=True)
  st.markdown("<p style='text-align: justify; font-size: 18px;'>Transforman elementos del Product Backlog en incrementos de producto entregables.<br>Autónomos y autoorganizados, toman decisiones sobre cómo abordar tareas.<br>Colaboran para lograr los objetivos del Sprint.</p>", unsafe_allow_html=True)
  st.markdown("<p style='text-align: justify; font-size: 18px;'><strong>Planificación en Scrum</strong></p>", unsafe_allow_html=True)

with st.container():
  st.write("---")
  st.subheader("Diagrama de Gantt")
  st.image(Gantt, use_column_width=True, output_format="JPEG")

with st.container():
  st.write("---")
  st.subheader("Stack Tecnológico")
  st.markdown("<p style='text-align: justify; font-size: 21px;'><strong>Parte técnica:</strong></p>", unsafe_allow_html=True)
  st.markdown("<p style='text-align: justify; font-size: 18px;'>Nube: Google Cloud Platform</p>", unsafe_allow_html=True)
  st.markdown("<p style='text-align: justify; font-size: 18px;'>Google Cloud Storage: para nuestro Datalake.</p>", unsafe_allow_html=True)
  st.markdown("<p style='text-align: justify; font-size: 18px;'>BigQuery: para nuestro Datawarehouse.</p>", unsafe_allow_html=True)
  st.markdown("<p style='text-align: justify; font-size: 18px;'>Google Colab: para la creación de archivos jupyter que automáticamente hagan la carga incremental, el ETL y la subida al Datawarehouse de todos nuestros datasets. Además, también lo utilizamos para los EDAs que quedarán subidos en el repositorio.</p>", unsafe_allow_html=True)
  st.markdown("<p style='text-align: justify; font-size: 18px;'>Cloud Functions: para la automatización de los archivos jupyter creados en Google Colab.</p>", unsafe_allow_html=True)
  st.markdown("<p style='text-align: justify; font-size: 18px;'>Pub/Sub y Cloud Scheduler: para el trigger de las funciones creadas en Cloud Functions.</p>", unsafe_allow_html=True)
  st.markdown("<p style='text-align: justify; font-size: 18px;'>Lenguaje de programación: Python, ya que es el que nuestra empresa utiliza habitualmente para procesar y analizar datos.</p>", unsafe_allow_html=True)
  st.markdown("<p style='text-align: justify; font-size: 18px;'>Librerías: </p>", unsafe_allow_html=True)
  st.markdown("<p style='text-align: justify; font-size: 16px;'>          ❖	Pandas: la mejor para procesar datasets en forma de dataframes. <br>          ❖	Mathplotlib: para la creación de gráficos que nos permitan mirar los datos desde otra perspectiva más analizable. <br>          ❖	Numpy: para ecuaciones matemáticas. <br>          ❖	Sk-learn: para nuestro modelo predictivo.</p>", unsafe_allow_html=True)
  st.markdown("<p style='text-align: justify; font-size: 21px;'><br><strong>Parte analítica:</strong></p>", unsafe_allow_html=True)
  st.markdown("<p style='text-align: justify; font-size: 18px;'>Power BI: para la creación del Dashboard interactivo.</p>", unsafe_allow_html=True)
  st.markdown("<p style='text-align: justify; font-size: 18px;'>Google Colab: para el análisis de los datos.</p>", unsafe_allow_html=True)

with st.container():
  st.write("---")
  st.subheader("Modelo de datos")
  st.markdown("<p style='text-align: justify; font-size: 18px;'>Se dispone como fuente de información los archivos de las dos plataformas, compuestos por archivos de tipo json, parquet, pkl. Durante los procesos de ETL y EDA a dichos archivos, y tomando como referencia los diccionarios de las fuentes. El modelo de datos que contiene el datawarehouse del proyecto contiene tablas de ambas plataformas.</p>", unsafe_allow_html=True)
  st.markdown("<p style='text-align: justify; font-size: 21px;'><strong>Tablas de la Plataforma Google Maps:</strong></p>", unsafe_allow_html=True)
  st.markdown("<p style='text-align: justify; font-size: 18px;'><strong>1. dim_gm_business: </strong>Esta tabla almacena información detallada sobre los negocios en Google Maps, incluyendo detalles de ubicación, categorías, horarios de operación entre otros.</p>", unsafe_allow_html=True)
  st.markdown("<p style='text-align: justify; font-size: 18px;'><strong>2. fact_gm_review: </strong>Aquí se almacenan las reseñas y calificaciones de los usuarios en relación con los negocios registrados en Google Maps, lo que nos da la posibilidad de analizar la interacción entre negocios y usuarios.</p>", unsafe_allow_html=True)
  st.markdown("<p style='text-align: justify; font-size: 22px;'><strong>Tablas de la Plataforma Yelp:</strong></p>", unsafe_allow_html=True)
  st.markdown("<p style='text-align: justify; font-size: 18px;'><strong>1. dim_yelp_business: </strong>En esta tabla, mantenemos información esencial sobre los negocios en Yelp, como categorías, atributos y valoraciones.</p>", unsafe_allow_html=True)
  st.markdown("<p style='text-align: justify; font-size: 18px;'><strong>2. dim_yelp_user: </strong>En esta tabla se encuentran registrados los usuarios de Yelp, a diferencia de googlemaps podemos tener mayor información sobre el perfil del usuario, como sus contactos y sus valoraciones.</p>", unsafe_allow_html=True)
  st.markdown("<p style='text-align: justify; font-size: 18px;'><strong>3. fact_yelp_review: </strong>Al igual que en el caso de Google Maps, esta tabla contiene revisiones y calificaciones de usuarios relacionadas con los negocios en Yelp, lo que nos permite evaluar la satisfacción del cliente y realizar análisis de sentimiento.</p>", unsafe_allow_html=True)
  st.markdown("<p style='text-align: justify; font-size: 18px;'><strong>4. fact_yelp_checkin: </strong>Esta tabla contiene información sobre las visitas realizadas por los usuarios de Yelp en los negocios, lo que puede proporcionar indicios sobre la actividad y la popularidad de los lugares reflejada en la plataforma.</p>", unsafe_allow_html=True)
  st.markdown("<p style='text-align: justify; font-size: 21px;'><br> <strong>A.	DIAGRAMA DE ENTIDAD RELACION</strong><br>Las estructuras de datos para el datawarehouse del proyecto en la plataforma BIGQUERY, se han asignado a dos datasets:</p>", unsafe_allow_html=True)
  st.markdown("<p style='text-align: justify; font-size: 18px;'>googlemaps</p>", unsafe_allow_html=True)

  st.image(Diagrama_googlemaps, output_format="JPEG")
  st.markdown("<p style='text-align: justify; font-size: 18px;'>yelp</p>", unsafe_allow_html=True)
  st.image(Diagrama_yelp, output_format="JPEG")
  st.markdown("<p style='text-align: justify; font-size: 18px;'>A continuación, tenemos el <strong>DER</strong> (Diagrama Entidad Relación)</p>", unsafe_allow_html=True)

  width = 845
  height = 590
  Diagrama_er = Diagrama_er.resize((width, height))
  st.image(Diagrama_er, use_column_width=True, output_format="JPEG")
  st.markdown("<p style='text-align: justify; font-size: 21px;'><strong>B.	DICCIONARIO DE DATOS</strong></p>", unsafe_allow_html=True)
  st.markdown("<p style='text-align: justify; font-size: 16px;'>Usamos la nomenclatura dim_% para tablas de dimensiones, y fact_% para tablas de hechos</p>", unsafe_allow_html=True)

  st.image(Tabla1, use_column_width=True, output_format="png")
  st.image(Tabla2, use_column_width=True, output_format="png")
  st.image(Tabla3_1, use_column_width=True, output_format="png")
  st.image(Tabla3_2, use_column_width=True, output_format="png")
  st.image(Tabla4, use_column_width=True, output_format="png")
  st.image(Tabla5, use_column_width=True, output_format="png")

with st.container():
  st.write("---")
  st.subheader("Ingeniería de Datos")
  st.markdown("<p style='text-align: justify; font-size: 18px;'>Ya habiendo nombrado anteriormente nuestro stack tecnológico, lo que queda es explicar cómo usamos cada herramienta, y el ciclo de vida del dato.</p>", unsafe_allow_html=True)
  st.image(ciclo_dato, output_format="png")
  st.markdown("<p style='text-align: justify; font-size: 18px;'>Nuestros datos principales son extraídos desde un Google Drive que nos aportó el cliente, a partir de ellos lo primero que hicimos fue realizarles el ETL con Google Colab.<br>Imagen que demuestra la creación de varios colabs en una carpeta e Google Drive:</p>", unsafe_allow_html=True)
  st.image(caping1, use_column_width=True, output_format="JPEG")
  st.markdown("<p style='text-align: justify; font-size: 18px;'>Luego de realizar tanto los ETLs como los EDAs en Google Colab, subimos los datasets a Google Cloud Storage para poder implementar los ETLs que realizamos en Google Colab, pero de una manera más automatizada a través de Google Cloud Functions.<br>Imagen que demuestra los datos en varios buckets de GCS:</p>", unsafe_allow_html=True)
  st.image(caping2, use_column_width=True, output_format="JPEG")
  st.markdown("<p style='text-align: justify; font-size: 18px;'>Imagen que demuestra la creación de funciones para los ETLs, la API y la carga incremental: </p>", unsafe_allow_html=True)
  st.image(caping3, use_column_width=True, output_format="JPEG")

  st.markdown("<p style='text-align: justify; font-size: 18px;'>Explicación de lo que hace cada función de la imagen:</p>", unsafe_allow_html=True)
  st.markdown("<p style='text-align: justify; font-size: 18px;'>          ❖	Apiloader: Esta función es la encargada de llamar a la API, extraer los datos y almacenarlos en GSC. Además, se ejecuta cada una hora ya que la API tiene ese tiempo de actualización.</p>", unsafe_allow_html=True)
  st.markdown("<p style='text-align: justify; font-size: 18px;'>          ❖	carga_incremental_intento_1: Esta función cumple varios roles, primero en principal es la encargada de llevar un registro en cuanto a los archivos que ya fueron cargados en BigQuery (nuestro datawarehouse) con el objetivo de que, si la API llegase a fallar, no se almacenen datos repetidos; y, en segundo lugar, la función también es la encargada de llevar los datos a una tabla de BigQuery en donde se van almacenando debajo de los datos ya existentes.</p>", unsafe_allow_html=True)
  st.markdown("<p style='text-align: justify; font-size: 18px;'>          ❖	ETL: Aquí están los ETLs, que como previamente mencioné, fueron creados en Google Colab de forma provisoria. Los objetivos de este pipeline, son el de juntar todos los datasets del mismo tipo para crear uno que pueda ser procesado y enviado a tablas de BigQuery. </p>", unsafe_allow_html=True)
  st.markdown("<p style='text-align: justify; font-size: 18px;'>La diferencia entre esta función y la de carga incremental, es que los datos de Google Drive jamás serán actualizados, por lo que esta función quedaría automatizada y lista para recibir actualizaciones, pero no ocurrirá a menos que sea manualmente mediante un dataset creado por nosotros.</p>", unsafe_allow_html=True)
  st.markdown("<p style='text-align: justify; font-size: 18px;'><br>(Tanto ETL_GoogleMaps_Review_Florida como gco_to_bigquery son funciones que implementamos en un principio pero que luego descartamos ante la creación de otras mejores)<br>Imagen que demuestra la presencia de las tablas con los datos en BigQuery:</p>", unsafe_allow_html=True)
  st.image(caping4, use_column_width=True, output_format="JPEG")
  st.markdown("<p style='text-align: justify; font-size: 18px;'>Como vemos a la izquierda, tenemos 3 conjuntos de datos llamados ‘googlemaps’, ‘inremental_load’ y ‘yelp’, y cada uno tiene dentro las tablas que le corresponden.</p>", unsafe_allow_html=True)

with st.container():
  st.write("---")
  st.subheader("Modelo de Machine Learning")
  st.markdown("<p style='text-align: justify; font-size: 18px;'>Aunque quizá la palabra correcta sea Modelos, ya que hay varios. Estos cumplen 2 funciones, el primero, busca tokenizar las opiniones de la gente para obtener una puntuación a partir de lo que escribe y así, poder filtrar por restaurantes y ciudad en la plataforma GoogleMaps; el segundo modelo, busca comparar las reseñas de ambas plataformas, con el objetivo de saber de cuales conviene fiarse mas.<br><br>Para entender todas las desiciones tomadas, adentrese en los archivos de ML en la carpeta '5_ ML' del repositorio.<br></p>", unsafe_allow_html=True)
  st.markdown("<p style='text-align: justify; font-size: 21px;'>Conclusiones del modelo:</p>", unsafe_allow_html=True)
  st.markdown("<p style='text-align: justify; font-size: 18px;'>La mayoria de opiniones acerca de restaurants son expresadas con 500 palabras o menos y la mayoria de opiniones son positivas en 3 de 5 categorias de rating por compound score(ver histograma 1, 2 y 4).</p>", unsafe_allow_html=True)
  st.markdown("<p style='text-align: justify; font-size: 18px;'>Una vez realizada la etiquetacion de los resultados de compound de VADER, se puede notar el desbalance de casos positivos (1) y casos negativos (0), lo que sesga la capacidad de prediccion de un modelo de clasificacion (ver histograma 3).</p>", unsafe_allow_html=True)
  st.markdown("<p style='text-align: justify; font-size: 18px;'>Se comprueba la relacion directa que existe (de uno a uno) entre el score compound de Vader, la relacion directa entre el score positivo, la relacion inversa entre score negativo y el rating del restaurant respectivamente (ver histograma 4 y 5).Por ejemplo, si el restaurant tiene un rating de 1 es mas probable que tenga una mala percepcion o resultado negativo en el analisis de sentimiento.</p>", unsafe_allow_html=True)
  st.markdown("<p style='text-align: justify; font-size: 18px;'>Los comentarios u opiniones(positivas o negativas) en googlemaps son mas diferenciados que en yelp, por ejemplo, en el histograma 4 la diferencia entre comentarios de 1 y 2 ratings son mucho mas diferenciados a los comentarios de 3,4 y 5 rating.</p>", unsafe_allow_html=True)
  st.markdown("<p style='text-align: justify; font-size: 18px;'>De los modelos de clasificacion usados sin realizar validacion cruzada el score de accuracy es de un 94% en promedio y el AUC promedio de 96%. Despues de realizar la validacion cruzada en promedio(teniendo en cuenta los dos modelos) se obtiene un accuracy de 93% y un AUC de 95%. Lo anterior permite concluir que si pusieramos en produccion el modelo de machine learning para predecir comentarios positivos y negativos de acuerdo a Vader, este ultimo va a producir(asignar scores positivos) un 93% de outputs correctos (opiniones que realmente son positivas) y tendra un 7% de error en asignar scores(positivos) a los comentarios.</p>", unsafe_allow_html=True)
  st.markdown("<p style='text-align: justify; font-size: 18px;'>Comparando los resultados de yelp con los de google en terminos de accuracy, google presenta un mejor grado de prediccion de opiniones positivas en lo que respecta al valor al que un empresario/ cliente de restaurant podria acceder haciendo uso de los servicios de un restaurant. Los histogramas de ambos en cuanto al rating/stars por score compound muestran que en googlemaps se puede tener un mayor acceso a opiniones negativas tanto como positivas, lo que permite contrastar mejor que tipo de restaurants podrian ofrecer un mayor valor a los clientes y esto mismo podria ser usado para determinar mejoras en el servicio con otros datos complementarios.</p>", unsafe_allow_html=True)


with st.container():
  st.write("---")
  st.subheader("KPIs (Indicadores Clave de Desempeño)")
  #st.markdown("<p style='text-align: justify; font-size: 18px;'>TASA DE CRECIMIENTO DE CANTIDAD DE RESTAURANTES POR CIUDAD (Ciudad): Negocios afiliados mes / Negocios afiliados mes anterior.(este indicador nos sirve para monitorear si el sector esta en auge o en declive en cada ciudad)</p>", unsafe_allow_html=True)
  st.markdown("<p style='text-align: justify; font-size: 18px;'>TASA DE RELACION VALORACIONES POSITIVAS (Ciudad): Reseña positivas del mes / Reseñas registradas del mes. (reseña positiva = valoración >= 4).</p>", unsafe_allow_html=True)
  st.markdown("<p style='text-align: justify; font-size: 18px;'>KPI DE DISPONIBILIDAD DE ATRIBUTOS DE RESTAURANTE(Restaurantes): Disponibilidad de atributos de un restaurante/Cantidad de atributos ofrecidos en los restaurantes.</p>", unsafe_allow_html=True)
  st.markdown("<p style='text-align: justify; font-size: 18px;'>KPI DE ANALISIS DE SENTIMIENTO POR RESTAURANTE(Restaurante): Puntaje de restaurante (cerca de -1  = malo, cerca de 1 = bueno)</p>", unsafe_allow_html=True)
  st.markdown("<p style='text-align: justify; font-size: 18px;'>TASA DE CONTAMINACIÓN POR HORA(Ciudad): Contaminación del mes.</p>", unsafe_allow_html=True)
  #st.markdown("<p style='text-align: justify; font-size: 18px;'>aaa</p>", unsafe_allow_html=True)

with st.container():
  st.write("---")
  st.subheader("Dashboard")
  st.markdown("<p style='text-align: justify; font-size: 18px;'>Estas son las 3 pagínas del Dashboard en orden, en las dos primeras estamos viendo información relacioanda a las ciudades, y en la tercera, información relacionada a los atributos de los restaurantes.</p>", unsafe_allow_html=True)
  st.image(dashboard1, use_column_width=True, output_format="JPEG")
  st.image(dashboard2, use_column_width=True, output_format="JPEG")
  st.image(dashboard3, use_column_width=True, output_format="JPEG")

with st.container():
  st.write("---")
  st.subheader("Conclusiones")
  st.markdown("<p style='text-align: justify; font-size: 18px;'>Tras los gráficos del dashboard y lo hablado en la presentación final, podemos concluir 3 cosas:</p>", unsafe_allow_html=True)
  st.markdown("<p style='text-align: justify; font-size: 18px;'>1: Que tras basarnos en las 5 ciudades con más restaurantes, concluimos que las 3 mejores opciones son Miame, Orlando y Tampa, tras comprobar que sus restaurantes son los que cuentan con mayor índice de valoraciones positivas y satisfacción.</p>", unsafe_allow_html=True)
  st.markdown("<p style='text-align: justify; font-size: 18px;'>2: Que las tres ciudades recién mencionadas, podemos verificar también su ingreso poblacional, el costo de vida y la calidad del aire, lo que nos dejaría como mejor opción a la ciudad de Tampa.</p>", unsafe_allow_html=True)
  st.markdown("<p style='text-align: justify; font-size: 18px;'>3: Una vez obtenida la mejor ciudad en la que poder poner un restaurante con las exigencias del cliente, debemos tener en cuenta que el promedio de atributos por restaurante de Tampa es de 14, por lo que a la hora de poner un restaurante competitivo minimamente deberá tener 14 atributos, entre los cuales se encuentran delivery, dinner, etc.</p>", unsafe_allow_html=True)

with st.container():
  st.write("---")
  st.subheader("Referencias")
  st.write("[Página donde se encuentra la API utilizada en el proyecto >>](https://www.iqair.com/)")
##enctype="multipart/form-data"
with st.container():
  st.write("---")
  st.subheader("Si tienes alguna consulta, no dudes en escribirnos! 📩")
  contact_form = f'''
  <form action="https://formsubmit.co/{email_contact}" method="POST">
  <input type="hidden" name="_captcha" value="false">  
    <input type="text" name="Nombre y Apellido" placeholder='Nombre y apellido:' required>
    <input type="email" name="Mail" placeholder= 'Mail:'>
    <textarea type="message" name="message" placeholder="Detalles de su duda:" required></textarea>
    <button type="submit">Enviar</button>
  </form>
'''
  st.markdown(contact_form, unsafe_allow_html=True)
