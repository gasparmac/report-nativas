
import streamlit as st
import openai

st.set_page_config(page_title="🌍 Informe Ambiental del Campo", layout="centered")
st.title("🌱 Informe Ambiental del Campo con ChatGPT")

# Obtener la API Key desde secrets (configurado en Streamlit Cloud)
if "OPENAI_API_KEY" not in st.secrets:
    st.error("No se encontró la API Key. Configurala en Settings > Secrets en Streamlit Cloud.")
else:
    openai.api_key = st.secrets["OPENAI_API_KEY"]

    st.subheader("📍 Seleccioná la ubicación del campo")
    direccion = st.text_input("Ingresá una dirección, localidad o nombre del campo:")

    if st.button("Generar informe ambiental con IA"):
        if direccion:
            prompt = f"""
Actuá como un experto en ecología, clima y biodiversidad. Quiero que me des un informe ambiental simple y claro para un campo ubicado en: {direccion}.

Indicame brevemente:
- Bioregión o ecoregión
- Promedio de precipitaciones
- Temperatura media anual
- Altitud aproximada
- Tipo de vegetación predominante
- Nivel de biodiversidad
- Riesgo climático (bajo / medio / alto)

El informe debe ser corto, informativo y claro. Redactalo en español, como para un productor o empresa.
"""

            with st.spinner("Consultando a ChatGPT..."):
                try:
                    response = openai.ChatCompletion.create(
                        model="gpt-4",
                        messages=[
                            {"role": "system", "content": "Sos un asistente experto en agroecología y clima."},
                            {"role": "user", "content": prompt}
                        ],
                        temperature=0.7,
                        max_tokens=600
                    )
                    result = response.choices[0].message.content
                    st.markdown("---")
                    st.subheader("🧾 Informe generado")
                    st.markdown(result)
                except Exception as e:
                    st.error(f"Error al consultar ChatGPT: {str(e)}")
        else:
            st.warning("Ingresá una dirección o localidad para continuar.")
