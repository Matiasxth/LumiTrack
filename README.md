# LumiTrack

**LumiTrack** es una aplicación interactiva desarrollada con Python y Streamlit para el catastro de luminarias. Esta herramienta permite registrar datos clave, como potencia de luminarias instaladas y retiradas, tipo de poste y ubicación GPS. Los datos recopilados pueden descargarse en formato CSV para un análisis posterior.

## Características

- **Registro de datos**:
  - Potencia instalada.
  - Potencia retirada.
  - Tipo de poste (madera, metal, hormigón, etc.).
  - Ubicación GPS (automática o manual).

- **Exportación de datos**:
  - Los datos registrados pueden descargarse en formato CSV con columnas correctamente separadas.

- **Diseño optimizado**:
  - Funciona en navegadores de escritorio y móviles.
  - Interfaz fácil de usar para técnicos en terreno.

## Requisitos

- **Python**: Versión 3.8 o superior.
- **Bibliotecas necesarias**:
  - `streamlit`
  - `pandas`

Para instalar las dependencias necesarias, ejecuta el siguiente comando en la terminal:
```bash
pip install -r requirements.txt


Uso
Clona este repositorio en tu máquina local:
git clone <URL-https://github.com/Matiasxth/LumiTrack.git)](https://github.com/Matiasxth/LumiTrack.git)>
cd lumitrack
Instala las dependencias necesarias:
pip install -r requirements.txt
Ejecuta la aplicación:
streamlit run lumitrack.py
