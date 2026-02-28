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
        "objetivo": "Construir resistencia y base aeróbica estable sobre la Tarmac.",
        "intensidad": "Zona 2 (79-108W / 55-75% FTP) con cadencia alta.",
        "entrenos": {
            "Lunes": "🚫 Descanso Total: Recuperación muscular completa.",
            "Martes": "⚙️ Rodillo Cadencia: 15' Calent. + 5x(30''/30'') Cadencia 110+ + 40' Z2 (85-95W) a 90 RPM.",
            "Miércoles": "🧘 Descanso Activo: Caminar 30 min o estiramientos suaves.",
            "Jueves": "🔥 Rodillo Resistencia: 15' Calent. (50-60W) + 50' Z2 estable (95-108W) a 90-95 RPM + 10' Cool down.",
            "Viernes": "🔧 Logística: Revisar presión de llantas y CALIBRAR potenciómetro (Zero Offset).",
            "Sábado": "🛣️ Fondo Calango: 2h 30m total. Mantener 79-108W (Z2) constante. Cadencia: 85-95 RPM (Plano) y >75 RPM (Subida).",
            "Domingo": "🚲 Recuperación Activa: 45' rodaje muy suave (<75W), plato pequeño, cadencia >90 RPM."
        }
    },
    "2. Construcción y Fuerza (Junio - Agosto)": {
        "objetivo": "Desarrollar potencia para los ascensos de 20km en Cali.",
        "intensidad": "Zona 3 (115-130W) y trabajos de fuerza-resistencia.",
        "entrenos": {
            "Lunes": "🚫 Descanso Total.",
            "Martes": "💪 Fuerza en Subida: 15' Calent. + 4x8' en Zona 3 (115-130W) a 65 RPM + 10' Recup.",
            "Miércoles": "⚙️ Rodillo Z2: 60 min constantes (90-105W) a 90 RPM.",
            "Jueves": "⚡ Intervalos FTP: 15' Calent. + 3x10' al 95-100% FTP (138-145W) a 90 RPM + 10' Recup.",
            "Viernes": "🧘 Descanso Activo: 40 min regenerativos (<70W).",
            "Sábado": "🏔️ Fondo con Desnivel: 3h 30m. En subida mantener Z3 (115-130W). En plano Z2 (80-105W).",
            "Domingo": "🚲 Recuperación Activa: 1h rodaje muy suave, cadencia libre."
        }
    },
    "3. Especialización (Septiembre - Octubre)": {
        "objetivo": "Simular las condiciones reales del Giro de Rigo.",
        "intensidad": "Simulación de carrera, ritmo alto y fondos de 140km+.",
        "entrenos": {
            "Lunes": "🚫 Descanso Total.",
            "Martes": "🏔️ Sweet Spot: 2x20' al 90% del FTP (130W) - Ritmo de subida larga en Cali.",
            "Miércoles": "⚙️ Rodillo Z2: 70 min con 5 sprints de 10'' (>200W) para ganar explosividad.",
            "Jueves": "📈 Picos de Potencia: 6x3' en Zona 4 (155-165W) para ataques en repechos cortos.",
            "Viernes": "🧘 Descanso Activo.",
            "Sábado": "🏁 Simulación Giro: 4h 30m de ruta. Entrenar nutrición (60g carbos/hora) y ritmo Z2-Z3.",
            "Domingo": "🚲 Recuperación Activa: 1h 15m muy suave, soltar piernas."
        }
    },
    "4. Tapering / Descarga (Últimas 2 Semanas)": {
        "objetivo": "Llegar a Cali con frescura total y máxima energía.",
        "intensidad": "Bajo volumen, toques cortos de intensidad para no perder ritmo.",
        "entrenos": {
            "Lunes": "🚫 Descanso Total.",
            "Martes": "🚀 Activación: 40' Z2 con 3 picos de 1' a 145W (ritmo carrera) para despertar el cuerpo.",
            "Miércoles": "🧘 Movilidad y relax profundo.",
            "Jueves": "🔧 Ajuste Final: 30' muy suaves (<70W). Comprobar maleta, Tarmac y sensores.",
            "Viernes": "✈️ Viaje a Cali / Carga de carbohidratos (Pasta/Arroz).",
            "Sábado": "🚲 Reconocimiento: 20' muy suaves en Cali. Calibrar potenciómetro con el calor de allá.",
            "Domingo": "🏆 EVENTO: GIRO DE RIGO CALI (150km). ¡A aplicar lo entrenado!"
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
                st.button("📥 Enviar a mi Garmin", key=f"gar_{dia}_{fase_seleccionada}")

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