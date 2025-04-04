
import streamlit as st
import random

st.set_page_config(page_title="🌍 Informe Ambiental del Campo", layout="centered")
st.title("🌱 Informe Ambiental del Campo")

# Simulador de datos ambientales según lat/lon o dirección (en el futuro se conecta a APIs reales)
def get_environmental_info(lat, lon):
    # Simulación con resultados randomizados
    return {
        "Bioregión": "Pastizales templados sudamericanos",
        "Precipitación": f"{random.randint(900, 1300)} mm/año",
        "Temperatura media": f"{random.uniform(15, 20):.1f} °C",
        "Altitud": f"{random.randint(50, 200)} m",
        "Vegetación": "Pastizal natural con cultivos en rotación",
        "Biodiversidad": "Alta (aves, polinizadores, pastizales)",
        "Riesgo climático": random.choice([
            "Bajo (buen balance hídrico y baja variabilidad)",
            "Medio (estrés hídrico ocasional, eventos extremos)",
            "Alto (frecuencia creciente de sequías o lluvias intensas)"
        ])
    }

# Entrada de dirección o selector de punto
st.subheader("📍 Seleccioná la ubicación del campo")

direccion = st.text_input("Ingresá una dirección o localidad:")
coordenadas = st.map()
lat, lon = None, None

# Simular lat/lon por dirección o usar punto fijo para demo
if direccion:
    lat, lon = -34.5, -60.8  # Ejemplo para Vedia

# Botón para generar informe
if st.button("Generar informe ambiental"):
    if lat is None or lon is None:
        st.warning("Por ahora simulamos con coordenadas fijas (Vedia, Bs.As.)")
        lat, lon = -34.5, -60.8

    info = get_environmental_info(lat, lon)
    st.markdown("---")
    st.subheader("🧾 Informe Ambiental del Campo")
    st.write(f"**Ubicación estimada:** {direccion or 'Lat: -34.5 / Lon: -60.8'}")

    for key, value in info.items():
        st.write(f"**{key}:** {value}")
