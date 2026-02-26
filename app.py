import streamlit as st
import pandas as pd

st.title("🚴‍♂️ Mi Reto: Giro de Rigo 2026")

# Sección del Plan de Entrenamiento
st.header("📅 Mi Plan de Entrenamiento")

# Creamos los datos del plan (puedes cambiar los textos por tus entrenamientos reales)
data = {
    "Día": ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"],
    "Actividad": ["Descanso Activo", "Series de Potencia", "Z2 - Resistencia", "Subidas (Cali)", "Rodada Suave", "Fondo Largo", "Recuperación"],
    "Duración": ["30 min", "1h 30min", "2h 00min", "1h 45min", "1h 00min", "4h+ (Reto)", "Libre"]
}

df = pd.DataFrame(data)

# Mostramos la tabla en la App
st.table(df)

# Un mensaje de motivación que cambie
st.info("💡 Tip del día: Hidrátate bien, hoy el calor en la ruta será fuerte.")