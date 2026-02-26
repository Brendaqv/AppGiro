import streamlit as st
import pandas as pd
from datetime import datetime

# Configuración de estilo
st.set_page_config(page_title="Giro de Rigo 2026", page_icon="🚴‍♂️")

# Título y Fase Actual
st.title("🚀 Entrenador Élite: Giro de Rigo")

# --- BLOQUE DE FASE ACTUAL ---
col_fase, col_fecha = st.columns([2, 1])
with col_fase:
    st.info("**Fase Actual:** Construcción de Base Aeróbica (Mes 1)")
with col_fecha:
    st.write(f"📅 {datetime.now().strftime('%d/%m/%Y')}")

st.divider()

# --- PLAN DE ENTRENAMIENTO DINÁMICO ---
st.subheader("📅 Cronograma de la Semana")

# Ejemplo de cómo organizar los detalles
plan = {
    "Lunes": {"tipo": "Descanso", "detalle": "Recuperación total. Estiramientos suaves de 15 min."},
    "Martes": {"tipo": "Series de Potencia", "detalle": "4x8 min a 90% FTP con 4 min de recuperación entre series."},
    "Miércoles": {"tipo": "Z2 - Resistencia", "detalle": "90 min en Zona 2 constante. Cadencia 85-90 rpm."},
    "Jueves": {"tipo": "Subidas", "detalle": "Repeticiones en cuesta: 5x5 min en subida grado 6-8%."},
    "Viernes": {"tipo": "Recuperación", "detalle": "45 min rodaje muy suave (plato pequeño)."},
    "Sábado": {"tipo": "Fondo Largo", "detalle": "3h 30min acumulando desnivel. Enfoque en hidratación."},
    "Domingo": {"tipo": "Libre / Grupeto", "detalle": "Rodada social o descanso según sensaciones."}
}

for dia, info in plan.items():
    with st.expander(f"{dia} - {info['tipo']}"):
        st.write(f"**Detalle Técnico:** {info['detalle']}")
        if st.button(f"Registrar entreno del {dia}"):
            st.success(f"✅ ¡Entrenamiento de {dia} guardado en el historial!")

st.divider()

# --- CAMBIO DE MES / PLAN ---
with st.sidebar:
    st.header("⚙️ Configuración")
    mes_plan = st.selectbox("Seleccionar Mes de Entrenamiento", ["Febrero - Base", "Marzo - Fuerza", "Abril - Pico"])
    st.write(f"Estás viendo el plan de: **{mes_plan}**")
    
    st.button("Actualizar Plan desde la Nube")

# --- MÉTRICAS RÁPIDAS ---
st.subheader("📊 Resumen Semanal")
col1, col2, col3 = st.columns(3)
col1.metric("Horas Objetivo", "12h", "+2h")
col2.metric("TSS Previsto", "450", "Estable")
col3.metric("Kms Semanales", "180 km", "10%")