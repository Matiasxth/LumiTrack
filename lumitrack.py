import streamlit as st
import pandas as pd
from streamlit_javascript import st_javascript

# Configuración inicial
st.title("LumiTrack: Catastro de Luminarias")
st.write("Registra datos de luminarias, como potencia, tipo de poste y ubicación GPS.")

# Variable para almacenar la ubicación GPS actual
if "gps_location" not in st.session_state:
    st.session_state.gps_location = "Ubicación no disponible"

# Botón para refrescar la ubicación GPS
if st.button("Refrescar ubicación GPS"):
    coords = st_javascript(
        code="""
        navigator.geolocation.getCurrentPosition(
            (position) => {
                const latitude = position.coords.latitude;
                const longitude = position.coords.longitude;
                const coords = `${latitude}, ${longitude}`;
                document.dispatchEvent(new CustomEvent("streamlit:setComponentValue", {detail: coords}));
            },
            (error) => {
                const errorMessage = "Permiso denegado o no disponible.";
                document.dispatchEvent(new CustomEvent("streamlit:setComponentValue", {detail: errorMessage}));
            }
        );
        """
    )
    st.session_state.gps_location = coords

# Mostrar la ubicación GPS actual
st.write("### Ubicación GPS Actual:")
st.write(st.session_state.gps_location)

# Almacenamiento temporal en la sesión de Streamlit
if "data" not in st.session_state:
    st.session_state.data = []

# Formulario para ingreso de datos
with st.form("catastro_form"):
    potencia_instalada = st.number_input("Potencia Luminaria Instalada (W)", min_value=0, step=1)
    potencia_retirada = st.number_input("Potencia Luminaria Retirada (W)", min_value=0, step=1)
    tipo_poste = st.selectbox("Tipo de Poste", ["Madera", "Metal", "Hormigón", "Otro"])
    ubicacion_gps = st.text_input("Ubicación GPS (automática o manual)", st.session_state.gps_location)
    submit_button = st.form_submit_button("Agregar")

    if submit_button:
        if "Permiso denegado" not in ubicacion_gps and ubicacion_gps:
            st.session_state.data.append({
                "Fecha y Hora": pd.Timestamp.now().strftime("%Y-%m-%d %H:%M:%S"),
                "Potencia Instalada (W)": potencia_instalada,
                "Potencia Retirada (W)": potencia_retirada,
                "Tipo de Poste": tipo_poste,
                "Ubicación GPS": ubicacion_gps,
            })
            st.success("Dato agregado correctamente.")
        else:
            st.error("Por favor, otorgue permisos de ubicación o ingrese la ubicación manualmente.")

# Mostrar los datos ingresados
if st.session_state.data:
    st.write("### Datos ingresados:")
    df = pd.DataFrame(st.session_state.data)
    st.dataframe(df)

    # Exportar los datos a CSV
    csv_data = df.to_csv(index=False, sep=';', encoding='utf-8').encode('utf-8')
    st.download_button(
        label="Descargar archivo CSV",
        data=csv_data,
        file_name="catastro_luminarias.csv",
        mime="text/csv",
    )
else:
    st.info("No hay datos ingresados para exportar.")
