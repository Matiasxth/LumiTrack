# LumiTrack
sistema de catastro y seguimiento de luminarias.
# LumiTrack

**LumiTrack** es una aplicación interactiva desarrollada con Python y Streamlit para el catastro de luminarias. Permite registrar datos como potencia de luminarias instaladas y retiradas, tipo de poste, y ubicación GPS, almacenándolos en un archivo descargable. Este software está diseñado para garantizar la gestión eficiente de puntos de iluminación.

## Características

- **Registro de luminarias**:
  - Potencia de luminaria instalada y retirada.
  - Tipo de poste (madera, metal, hormigón, etc.).
  - Ubicación GPS (ingreso manual o automático).
  
- **Exportación de datos**:
  - Descarga los datos registrados en formato CSV o Excel.

- **Visualización interactiva**:
  - Tabla con todos los puntos registrados durante la sesión.
  - Mapa interactivo para mostrar las ubicaciones.

- **Privacidad**:
  - Los datos ingresados no se almacenan permanentemente en el servidor ni en el repositorio.

## Requisitos

- **Python 3.8 o superior**
- Bibliotecas requeridas:
  - `streamlit`
  - `pandas`
  - `openpyxl`
  - `folium`
  - `streamlit-folium` (opcional, para mapas)

Para instalarlas, ejecuta:
```bash
pip install streamlit pandas openpyxl folium streamlit-folium
git clone <URL-del-repositorio>
cd lumitrack
streamlit run app.py

