import streamlit as st
import pandas as pd

NOMBRE_DE_LA_APP="EcoGeoConcrete"
EMISONES_DE_CARBONO_MATERIALES_POR_M3={
    "hormigonConvencional":300,
    "hormigonGeopolimerico":135
}

def CalcularEmisiones(metros, tipo):
    return metros*EMISONES_DE_CARBONO_MATERIALES_POR_M3[tipo]
def CalcularCO2(CO2Convecional, CO2Polimerico):
    return CO2Convecional-CO2Polimerico

st.set_page_config(
    page_title=NOMBRE_DE_LA_APP,
    layout="wide"
)
st.title("Calculadora de CO2 - ECOGEO")
st.write("Compara cuanto contamina el hormigon convencional y el geopolimerico")

metros = st.number_input("Ingrese los m3 de hormigon", min_value=0.0, value=100.0)

CO2Convencional = CalcularEmisiones(metros, "Convencional")
CO2Polimerico = CalcularEmisiones(metros, "Geopolimerico")
diferenciaHormigon = CalcularCO2(co2_convencional, co2_geopolimerico)

st.write("Hormigon convencional:", CO2Convencional, "kg de CO2")
st.write("Hormigon geopolimerico:", CO2Polimerico, "kg de CO2")

st.bar_chart({"kg de CO2": {"Convencional": CO2Convencional, "Geopolimerico": CO2Polimerico}})

st.success("Con hormigon geopolimerico se dejan de emitir " + str(diferenciaHormigon) + " kg de CO2")