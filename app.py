import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="CongestiQ",
    page_icon="🚦",
    layout="centered"
)

st.markdown("<h1 style='text-align:center;'>🚦 CongestiQ</h1>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align:center;'>Smart Traffic Congestion & Risk Analysis System</p>",
    unsafe_allow_html=True
)

st.divider()

# ---------------- INPUT SECTIONS ----------------

st.subheader("🚗 Traffic Conditions")
col1, col2 = st.columns(2)

with col1:
    traffic_density = st.slider("Traffic Density (%)", 0, 100, 50)
    avg_speed = st.slider("Average Speed (km/h)", 0, 120, 40)
    peak_hour = st.selectbox("Peak Hour", ["No", "Yes"])

with col2:
    construction = st.selectbox("Road Construction", ["No", "Yes"])
    accident = st.selectbox("Recent Accident", ["No", "Yes"])
    lane_closure = st.selectbox("Lane Closure", ["No", "Yes"])

st.subheader("🌦️ Weather & Climate Factors")
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

st.subheader("🛑 Safety & Human Factors")
col5, col6 = st.columns(2)

with col5:
    helmet_usage = st.slider("Helmet Usage (%)", 0, 100, 70)
    seatbelt_usage = st.slider("Seatbelt Usage (%)", 0, 100, 80)

with col6:
    speeding = st.selectbox("Speeding Observed", ["No", "Yes"])
    night_time = st.selectbox("Time of Day", ["Day", "Night"])

st.subheader("🌍 Environmental Stress")
aqi = st.slider("Air Quality Index (AQI)", 0, 500, 120)

st.divider()

# ---------------- LOGIC ENGINE ----------------

risk_score = 0

# Traffic influence
risk_score += traffic_density * 0.35
risk_score += max(0, (60 - avg_speed)) * 0.4

if peak_hour == "Yes":
    risk_score += 10
if construction == "Yes":
    risk_score += 15
if accident == "Yes":
    risk_score += 20
if lane_closure == "Yes":
    risk_score += 10

# Weather influence
weather_risk = {
    "Clear": 0,
    "Rain": 12,
    "Fog": 18,
    "Storm": 25,
    "Extreme Heat": 10,
    "Flooding": 30
}
risk_score += weather_risk[weather]

if visibility < 300:
    risk_score += 12

# Safety influence
risk_score += (100 - helmet_usage) * 0.2
risk_score += (100 - seatbelt_usage) * 0.15

if speeding == "Yes":
    risk_score += 15
if night_time == "Night":
    risk_score += 8

# Environmental stress
if temperature > 40:
    risk_score += 10
if humidity > 80:
    risk_score += 6
if aqi > 200:
    risk_score += 10

# ---------------- FINAL CONGESTION CALCULATION ----------------

# Normalize to 0–100%
congestion_percentage = min(100, int((risk_score / 150) * 100))

# ---------------- OUTPUT ----------------

st.subheader("📊 Final Analysis")

st.metric(
    label="Traffic Congestion Level",
    value=f"{congestion_percentage} %"
)

st.progress(congestion_percentage / 100)

if congestion_percentage < 35:
    st.success("🟢 Low Congestion & Risk")
    status = "Traffic is flowing smoothly with minimal risk."
elif congestion_percentage < 65:
    st.warning("🟡 Moderate Congestion & Risk")
    status = "Traffic buildup detected. Caution advised."
else:
    st.error("🔴 High Congestion & Risk")
    status = "Severe congestion and high accident probability."

st.markdown(f"**System Insight:** {status}")

st.subheader("🧠 Recommended Actions")

if congestion_percentage >= 65:
    st.write("• Reroute traffic immediately")
    st.write("• Deploy traffic police")
    st.write("• Issue public safety alerts")
elif congestion_percentage >= 35:
    st.write("• Monitor traffic closely")
    st.write("• Reduce speed limits")
    st.write("• Alert commuters")
else:
    st.write("• Normal traffic operations")
    st.write("• No immediate intervention needed")

st.divider()
st.caption("CongestiQ | Smart Cities • Road Safety • Real-Time Inspired MVP")


