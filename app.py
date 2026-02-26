import streamlit as st
from datetime import date

# Configuración de la página para que se vea bien en celular
st.set_page_config(page_title="App El Giro de Rigo - Cali 2026", page_icon="🚴")

# Título de la App
st.title("🚴 Giro de Rigo: Cali 2026")
st.subheader("Tu camino de Lima a Colombia")

# Lógica de fechas
fecha_giro = date(2026, 11, 1)
hoy = date.today()
dias = (fecha_giro - hoy).days
semanas = dias // 7

# Mostrar métricas en tarjetas visuales
col1, col2 = st.columns(2)
col1.metric("Días Restantes", dias)
col2.metric("Semanas", semanas)

# Barra de progreso (estimando que empezamos hoy)
progreso = min(100, max(0, (1 - (dias / 248)) * 100)) # 248 es lo que falta hoy
st.write(f"Progreso hacia la competencia: {progreso:.1f}%")
st.progress(int(progreso))

# Mensaje motivador según la fase
st.divider()
if semanas > 24:
    st.info("📍 **Fase de Base**: Sal a rodar. Enfócate en tú resistencia aeróbica.")
else:
    st.warning("⚠️ ¡Es hora de empezar con las cuestas!")

# Botón interactivo (solo de prueba)
if st.button("¡Registrar entrenamiento de hoy!"):
    st.balloons()
    st.success("¡Entrenamiento guardado! (Próximamente conectaremos con Garmin)")