import streamlit as st
import pandas as pd  # <--- ESTA ES LA QUE FALTA
from datetime import datetime

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Vamos Cali - Giro de Rigo", page_icon="🚴‍♀️", layout="wide")

# --- ESTILO CSS PERSONALIZADO ---
st.markdown("""
    <style>
    .block-container { padding-top: 1.5rem; }
    .stSelectbox { margin-bottom: 20px; }
    .fase-info { background-color: #f0f4f8; padding: 15px; border-radius: 12px; border-left: 5px solid #1e88e5; margin-bottom: 20px; }
    .stButton>button { width: 100%; border-radius: 10px; height: 3em; }
    </style>
    """, unsafe_allow_html=True)

# --- BASE DE DATOS DE ENTRENAMIENTO ---
datos_plan = {
    "1. Base Aeróbica (Marzo - Mayo)": {
        "objetivo": "Construir resistencia y fortalecer ligamentos sobre la Tarmac.",
        "intensidad": "Zona 2 (vatios bajos, cadencia alta).",
        "entrenos": {
            "Lunes": "Descanso Activo: Movilidad 20 min.",
            "Martes": "Rodaje Z2: 90 min cadencia 90-95 rpm.",
            "Miércoles": "Z2 progresiva: 2h con últimos 15 min en Z3.",
            "Jueves": "Cadencia técnica: 60 min con intervalos de cadencia alta.",
            "Viernes": "Rodaje suave: 45 min recuperación.",
            "Sábado": "Fondo Largo: 3h 30m en terreno plano/ondulado.",
            "Domingo": "Libre o caminata."
        }
    },
    "2. Construcción y Fuerza (Junio - Agosto)": {
        "objetivo": "Desarrollar potencia para ascensos de 20 km.",
        "intensidad": "Intervalos y fortalecimiento en gimnasio (Fuerza-Resistencia).",
        "entrenos": {
            "Lunes": "Gimnasio: Tren inferior (Sentadillas/Prensa).",
            "Martes": "Intervalos de Fuerza: 4x10 min a 60 rpm en subida.",
            "Miércoles": "Z2 Resistencia: 2h fondo.",
            "Jueves": "Sprints de potencia: 8x30 seg al máximo.",
            "Viernes": "Gimnasio: Core y tren superior.",
            "Sábado": "Fondo con puertos: 4h incluyendo 2 subidas largas.",
            "Domingo": "Descanso total."
        }
    },
    "3. Especialización (Septiembre - Octubre)": {
        "objetivo": "Simular condiciones reales y el 'serrucho' final.",
        "intensidad": "Rodajes de larga distancia (140-160 km) y nutrición.",
        "entrenos": {
            "Lunes": "Descanso activo.",
            "Martes": "Simulacro de puerto: 2x30 min a ritmo de carrera.",
            "Miércoles": "Rodaje tempo: 90 min en Z3.",
            "Jueves": "Intervalos mixtos: Simulación de repechos (serrucho).",
            "Viernes": "Rodaje suave: 60 min.",
            "Sábado": "El Gran Fondo: 5h-6h (150 km) probando geles y sales.",
            "Domingo": "Rodada social 90 min."
        }
    },
    "4. Tapering / Descarga (Últimas 2 semanas Oct)": {
        "objetivo": "Recuperación total y asimilación del entrenamiento.",
        "intensidad": "Bajo volumen, toques de intensidad cortos.",
        "entrenos": {
            "Lunes": "Descanso total.",
            "Martes": "Activación: 60 min con 3 piques de 1 min.",
            "Miércoles": "Rodaje muy suave: 45 min.",
            "Jueves": "Activación corta: 45 min cadencia alta.",
            "Viernes": "Descanso total.",
            "Sábado": "Rodada previa: 60 min planos.",
            "Domingo": "🏁 DÍA DEL GIRO DE RIGO 🚴‍♂️"
        }
    }
}

# --- BARRA LATERAL (SIDEBAR) ---
with st.sidebar:
    st.title("⚙️ Panel de Control")
    vista = st.radio("Ver planificación:", ["Plan Semanal", "Plan Mensual"])
    st.divider()
    st.info("🎯 Meta: Giro de Rigo 2026")
    if st.button("🔄 Sincronizar Datos"):
        st.toast("Buscando actualizaciones...")

# --- ENCABEZADO PRINCIPAL ---
fecha_hoy = datetime.now().strftime('%d de %B, %Y')
st.write(f"📅 {fecha_hoy}")
st.title("🚀 Vamos Cali")

# Selector de Fases
fase_seleccionada = st.selectbox(
    "📍 Selecciona la Fase Actual:",
    options=list(datos_plan.keys())
)

fase = datos_plan[fase_seleccionada]

# --- VISTA CONDICIONAL ---
if vista == "Plan Semanal":
    st.markdown(f"""
    <div class="fase-info">
        <strong>🎯 Objetivo:</strong> {fase['objetivo']}<br>
        <strong>🔥 Intensidad:</strong> {fase['intensidad']}
    </div>
    """, unsafe_allow_html=True)

    st.subheader("📅 Entrenamientos de la Semana")
    
    for dia, detalle in fase['entrenos'].items():
        with st.expander(f"**{dia}**"):
            st.write(f"📝 {detalle}")
            c1, c2 = st.columns(2)
            with c1:
                if st.button(f"✅ Registrar {dia}", key=f"reg_{dia}_{fase_seleccionada}"):
                    st.success(f"¡Entreno de {dia} registrado!")
                    st.balloons()
            with c2:
                st.button("📥 Garmin", key=f"gar_{dia}_{fase_seleccionada}")

    # --- PANEL DE RESUMEN DE ESFUERZO (DISEÑO PREMIUM CON EXPLICACIONES) ---
    st.divider()
    st.subheader("📊 Nivel de Esfuerzo")

    # Estilo para las tarjetas (CSS mejorado)
    st.markdown("""
        <style>
        .card-container { display: flex; justify-content: space-between; gap: 10px; margin-bottom: 10px; }
        .metric-card { background-color: white; padding: 15px; border-radius: 15px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); text-align: center; flex: 1; border-bottom: 5px solid #1e88e5; }
        .metric-value { font-size: 22px; font-weight: bold; color: #1e88e5; margin: 5px 0; }
        .metric-label { font-size: 12px; color: #666; text-transform: uppercase; font-weight: bold; }
        .explainer { font-size: 0.85rem; color: #555; background-color: #f8f9fa; padding: 10px; border-radius: 10px; margin-top: 5px; line-height: 1.4; }
        </style>
        """, unsafe_allow_html=True)

    # Tarjetas HTML
    st.markdown(f"""
    <div class="card-container">
        <div class="metric-card">
            <div class="metric-label">📍 Distancia</div>
            <div class="metric-value">145.8 km</div>
        </div>
        <div class="metric-card" style="border-bottom-color: #f4b400;">
            <div class="metric-label">⏱️ Tiempo</div>
            <div class="metric-value">08:42 hs</div>
        </div>
        <div class="metric-card" style="border-bottom-color: #d32f2f;">
            <div class="metric-label">⚡ Esfuerzo (TSS)</div>
            <div class="metric-value">320</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # --- SECCIÓN DE LECTURA ÁGIL (EXPLICACIONES) ---
    with st.expander("🤔 Te lo explico"):
        col_a, col_b = st.columns(2)
        with col_a:
            st.markdown("""
            **📍 Distancia y Tiempo:** Son tu 'volumen'. Nos dicen cuánto terreno has conquistado. En la fase de **Base**, el tiempo es más importante que la velocidad: buscamos acostumbrar al cuerpo a estar horas sobre el sillín.
            """)
        with col_b:
            st.markdown("""
            **⚡ El TSS y tu recuperación:**
            
            Ayuda a saber cuánto descanso necesitas después de una salida:
            * **Menos de 150:** Carga baja. Te recuperas para el día siguiente.
            * **150 a 300:** Carga media. Sentirás fatiga, pero es manejable.
            * **300 a 450:** Carga alta. Necesitas 2 días de descanso o rodaje muy suave.
            * **Más de 450:** Carga extrema. Te dejará agotado por varios días.
            """)

    # Gráfico de carga
    st.write("📈 **Tu 'Batería' de Esfuerzo Diaria**")
    datos_carga = {
        "Día": ["Lun", "Mar", "Mie", "Jue", "Vie", "Sab", "Dom"],
        "TSS (Estrés)": [10, 85, 60, 90, 40, 100, 20]
    }
    df_carga = pd.DataFrame(datos_carga)
    st.bar_chart(df_carga.set_index("Día"), color="#1e88e5")

# --- ESTA ES LA PARTE QUE CORRIGE EL ERROR ---
else:
    st.subheader("📅 Calendario Mensual")
    st.warning("Esta vista está en construcción. Aquí verás el calendario completo de 4 semanas.")
    st.info("💡 Tip: Usa la vista semanal para registrar tus entrenos diarios.")