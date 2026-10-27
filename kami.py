import streamlit as st
import datetime

# Título que se ve arriba en la pestaña del navegador
st.set_page_config(page_title="Para ti mi niña hermosa", page_icon="❤️")

# Inicializamos la variable para recordar la opción elegida (Sí o No)
if "respuesta" not in st.session_state:
    st.session_state.respuesta = None

# Título principal en letras grandes
st.title("¡Hola, mi noviecita hermosa! ❤️")

# Contador de días
fecha_inicio = datetime.date(2025, 1, 18) 
hoy = datetime.date.today()
dias_juntos = (hoy - fecha_inicio).days

st.metric(label="Días amándote", value=f"{dias_juntos} días")

# Tus palabras sinceras
st.subheader("Esta pagina lo hice pensando en ti mi niña")
st.subheader("")
st.subheader("Leelo porfavor es lo q digo de mi corazón")
st.subheader("Mi amorcito")
st.write(
    "Te escribo estas palabras desde lo más profundo de mi corazón porque sé que hoy estamos distanciados por mi culpa. "
    "Sé perfectamente por qué estás enojada, dolida y decepcionada de mí. "
    "Quiero empezar pidiéndote perdón, no solo por haber salido con alguien, "
    "sino por lo que realmente te lastimó: habértelo ocultado durante más de un año. "
    "Entiendo por qué piensas que te engañé o que te menti. Mirando las cosas desde tu lugar, "
    "sé que la mentira hace que dudes de todo lo bonito que hemos vivido. "
    "Me equivoqué gravemente al no tener la madurez de contártelo en su momento por miedo a tu reacción, "
    "y al callarlo solo empeoré las cosas. Quiero que sepas, mirándote a los ojos a través de estas letras, "
    "que nunca te fui infiel, que para mí solo fue una amistad y que mi corazón siempre ha sido tuyo. "
    "Pero sé que mis palabras no bastan; debí demostrártelo con honestidad. "
    "Estos días que hemos salido he intentado demostrarte que te amo y que estoy cambiando. "
    "No quiero perderte, pero entiendo que recuperar tu confianza tomará tiempo. "
    "Estoy dispuesto a hacer las cosas bien, de manera transparente, "
    "porque eres la persona con la que quiero estar."
)

# Tus dos imágenes en columnas
col1, col2 = st.columns(2)

with col1:
    st.image("kami2.jpeg", caption="Un momento hermoso ❤️", use_container_width=True)

with col2:
    st.image("kamiii.jpeg", caption="Mira la primera vez q estuvimos solos 🥰", use_container_width=True)

# -------------------------------------------------------------
# NUEVA SECCIÓN: Propuesta Interactiva de Sí o No
# -------------------------------------------------------------
st.write("---") # Una línea divisoria bonita
st.subheader("Sé que las cosas han sido difíciles, pero quiero preguntarte...")
st.write("### ¿Me darías la oportunidad de seguir demostrándotelo y reconstruir lo nuestro? 🥺")

# Creamos las columnas para poner los botones uno al lado del otro
col_btn1, col_btn2 = st.columns(2)

with col_btn1:
    if st.button("Sí, quiero intentarlo 😍", use_container_width=True):
        st.session_state.respuesta = "si"

with col_btn2:
    if st.button("No... 💔", use_container_width=True):
        st.session_state.respuesta = "no"

# Control de las respuestas en pantalla
if st.session_state.respuesta == "si":
    st.balloons() # Lluvia de globos de celebración
    st.success("¡Gracias por darme esta oportunidad! Te prometo que cuidaré tu corazón con total honestidad. Te amo muchísimo. 💖👩‍❤️‍👨")

elif st.session_state.respuesta == "no":
    st.error("Entiendo perfectamente tu dolor... No me rendiré y te seguiré demostrando con hechos que valgo la pena. Aquí estaré para ti. 🥺🌹")
