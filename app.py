import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="CongestiQ",
    page_icon="🚦",
    layout="centered"
)

# ---------------- HEADER ----------------
st.markdown(
    "<h1 style='text-align:center;'>🚦 CongestiQ</h1>",
    unsafe_allow_html=True
)
st.markdown(
    "<p style='text-align:center;'>Traffic Congestion & Risk Intelligence System for Smart Cities</p>",
    unsafe_allow_html=True
)

st.info(
    "CongestiQ evaluates traffic congestion by combining traffic load, weather hazards, "
    "road conditions, safety compliance, and environmental stress into a single explainable score."
)

st.divider()

# ---------------- INPUTS ----------------
st.subheader("📥 Input Conditions")

tab1, tab2, tab3 = st.tabs(["🚗 Traffic", "🌦️ Weather", "🛑 Safety & Environment"])

# -------- TRAFFIC TAB --------
with tab1:
    col1, col2 = st.columns(2)

    with col1:
        traffic_density = st.slider("Traffic Density (%)", 0, 100, 50)
        avg_speed = st.slider("Average Speed (km/h)", 0, 120, 40)
        peak_hour = st.selectbox("Peak Hour", ["No", "Yes"])

    with col2:
        construction = st.selectbox("Road Construction", ["No", "Yes"])
        accident = st.selectbox("Recent Accident", ["No", "Yes"])
        lane_closure = st.selectbox("Lane Closure", ["No", "Yes"])

# -------- WEATHER TAB --------
with tab2:
    col3, col4 = st.columns(2)

    with col3:
        weather = st.selectbox(
            "Weather Condition",
            ["Clear", "Rain", "Fog", "Storm", "Extreme Heat", "Flooding"]
        )
        visibility = st.slider("Visibility (meters)", 50, 1000, 500)

    with col4:
        temperature = st.slider("Temperature (°C)", 0, 50, 30)
        humidity = st.slider("Humidity (%)", 0, 100, 60)

# -------- SAFETY TAB --------
with tab3:
    col5, col6 = st.columns(2)

    with col5:
        helmet_usage = st.slider("Helmet Usage (%)", 0, 100, 70)
        seatbelt_usage = st.slider("Seatbelt Usage (%)", 0, 100, 80)

    with col6:
        speeding = st.selectbox("Speeding Observed", ["No", "Yes"])
        time_of_day = st.selectbox("Time of Day", ["Day", "Night"])
        aqi = st.slider("Air Quality Index (AQI)", 0, 500, 120)

st.divider()

# ---------------- RISK ENGINE ----------------

traffic_risk = 0
weather_risk = 0
safety_risk = 0
environment_risk = 0

# ---- Traffic Risk ----
traffic_risk += traffic_density * 0.4
traffic_risk += max(0, 60 - avg_speed) * 0.35

if peak_hour == "Yes":
    traffic_risk += 10
if construction == "Yes":
    traffic_risk += 15
if accident == "Yes":
    traffic_risk += 20
if lane_closure == "Yes":
    traffic_risk += 10

# ---- Weather Risk ----
weather_scores = {
    "Clear": 0,
    "Rain": 12,
    "Fog": 18,
    "Storm": 25,
    "Extreme Heat": 10,
    "Flooding": 30
}
weather_risk += weather_scores[weather]

if visibility < 300:
    weather_risk += 12
if temperature > 40:
    weather_risk += 8
if humidity > 80:
    weather_risk += 6

# ---- Safety Risk ----
safety_risk += (100 - helmet_usage) * 0.25
safety_risk += (100 - seatbelt_usage) * 0.2

if speeding == "Yes":
    safety_risk += 15
if time_of_day == "Night":
    safety_risk += 8

# ---- Environmental Risk ----
if aqi > 200:
    environment_risk += 12

# ---- Total Risk ----
total_risk = traffic_risk + weather_risk + safety_risk + environment_risk

# Normalize to congestion %
congestion_percentage = min(100, int((total_risk / 160) * 100))

# ---------------- OUTPUT ----------------
st.subheader("📊 Congestion Assessment")

st.metric("Traffic Congestion Level", f"{congestion_percentage}%")
st.progress(congestion_percentage / 100)

if congestion_percentage < 35:
    st.success("🟢 Low Congestion")
    summary = "Traffic flow is stable with minimal disruption."
elif congestion_percentage < 65:
    st.warning("🟡 Moderate Congestion")
    summary = "Traffic buildup detected. Preventive measures recommended."
else:
    st.error("🔴 High Congestion")
    summary = "Severe congestion with high accident probability."

st.markdown(f"**System Insight:** {summary}")

# ---------------- BREAKDOWN ----------------
st.subheader("🔍 Risk Contribution Breakdown")

st.write(f"🚗 Traffic Factors: **{int(traffic_risk)}**")
st.write(f"🌦️ Weather Factors: **{int(weather_risk)}**")
st.write(f"🛑 Safety Factors: **{int(safety_risk)}**")
st.write(f"🌍 Environmental Factors: **{int(environment_risk)}**")

# ---------------- ACTIONS ----------------
st.subheader("🧠 Recommended Actions")

if congestion_percentage >= 65:
    st.write("• Activate traffic diversion plans")
    st.write("• Deploy traffic police & emergency teams")
    st.write("• Issue public travel advisories")
elif congestion_percentage >= 35:
    st.write("• Monitor congestion-prone zones")
    st.write("• Adjust signal timings")
    st.write("• Inform commuters in advance")
else:
    st.write("• Normal traffic operations")
    st.write("• Continue passive monitoring")

st.divider()
st.caption("CongestiQ | Explainable Traffic Intelligence for Smart Cities")
