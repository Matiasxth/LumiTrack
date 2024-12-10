# LumiTrack
sistema de catastro y seguimiento de luminarias.
# LumiTrack

**LumiTrack** es una aplicación interactiva desarrollada con Python y Streamlit para el catastro de luminarias. Permite registrar datos como potencia de luminarias instaladas y retiradas, tipo de poste, y ubicación GPS, almacenándolos en un archivo descargable. Este software está diseñado para garantizar la gestión eficiente de puntos de iluminación.

## Características

- Registro de datos de luminarias:
  - Potencia instalada.
  - Potencia retirada.
  - Tipo de poste (madera, metal, hormigón, etc.).
  - Ubicación GPS (automática o manual).
- Exportación de datos en formato CSV.
- Manejo de datos de forma temporal durante la sesión.
- Diseño optimizado para su uso en navegadores móviles.
  
- **Exportación de datos**:
  - Descarga los datos registrados en formato CSV o Excel.

- **Visualización interactiva**:
  - Tabla con todos los puntos registrados durante la sesión.
  - Mapa interactivo para mostrar las ubicaciones.

- **Privacidad**:
  - Los datos ingresados no se almacenan permanentemente en el servidor ni en el repositorio.

## Requisitos

- Python 3.8 o superior.
- Dependencias requeridas:
  - `streamlit`
  - `pandas`

Para instalarlas, ejecuta:
```bash
pip install streamlit pandas openpyxl folium streamlit-folium
git clone <URL-del-repositorio>
cd lumitrack
streamlit run app.py


### Cambios realizados:
1. Agregada la sección **Consideraciones Importantes** para incluir el requisito de activar el GPS.
2. Notas sobre navegadores compatibles para garantizar un mejor funcionamiento.



