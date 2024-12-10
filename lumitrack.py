import streamlit as st
import pandas as pd
import time

# Configuración inicial
st.title("LumiTrack: Catastro de Luminarias")
st.write("Registra datos de luminarias, como potencia, tipo de poste y ubicación GPS.")

# Variable para almacenar la ubicación GPS actual
if "gps_location" not in st.session_state:
    st.session_state.gps_location = "Ubicación no disponible"

# Función para obtener las coordenadas GPS desde el navegador
def refresh_gps():
    gps_script = """
    <script>
    navigator.geolocation.getCurrentPosition(
        (position) => {
            const latitude = position.coords.latitude;
            const longitude = position.coords.longitude;
            const coords = `${latitude}, ${longitude}`;
            document.getElementById("gps-coords").value = coords;
            Streamlit.setComponentValue(coords);
        },
        (error) => {
            let errorMessage = "Permiso denegado o no disponible.";
            if (error.code === 1) {
                errorMessage = "Acceso a la ubicación denegado por el usuario.";
            } else if (error.code === 2) {
                errorMessage = "Ubicación no disponible.";
            } else if (error.code === 3) {
                errorMessage = "La solicitud de ubicación expiró.";
            }
            document.getElementById("gps-coords").value = errorMessage;
            Streamlit.setComponentValue(errorMessage);
        }
    );
    </script>
    """
    coords = st.components.v1.html(
        f"""
        {gps_script}
        <input type="text" id="gps-coords" style="width: 100%; padding: 8px;" readonly>
        """,
        height=50,
    )
    return coords

# Botón para refrescar la ubicación GPS
if st.button("Refrescar ubicación GPS"):
    st.session_state.gps_location = refresh_gps()

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
                "Fecha y Hora": time.strftime("%Y-%m-%d %H:%M:%S"),
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
