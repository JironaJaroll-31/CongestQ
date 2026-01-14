import streamlit as st

st.set_page_config(page_title="CongestiQ", layout="centered")

st.title("🚦 CongestiQ – Intelligent Traffic Risk Analyzer")
st.write("Predicts congestion & accident risk using real-world conditions")

# ------------------ INPUTS ------------------

st.header("🚗 Traffic Conditions")
traffic_density = st.slider("Traffic Density (%)", 0, 100, 50)
avg_speed = st.slider("Average Speed (km/h)", 0, 120, 40)
construction = st.selectbox("Road Construction Ongoing?", ["No", "Yes"])
accident_reported = st.selectbox("Recent Accident Reported?", ["No", "Yes"])
peak_hour = st.selectbox("Peak Hour?", ["No", "Yes"])

st.header("🌦️ Weather & Climate")
weather = st.selectbox(
    "Weather Condition",
    ["Clear", "Rain", "Fog", "Storm", "Extreme Heat", "Flooding"]
)
visibility = st.slider("Visibility (meters)", 50, 1000, 500)

st.header("🛑 Safety Factors")
helmet_usage = st.slider("Helmet Usage (%)", 0, 100, 70)
seatbelt_usage = st.slider("Seatbelt Usage (%)", 0, 100, 80)
speeding = st.selectbox("Frequent Speeding Observed?", ["No", "Yes"])

st.header("🌍 Environmental Conditions")
temperature = st.slider("Temperature (°C)", 0, 50, 30)
humidity = st.slider("Humidity (%)", 0, 100, 60)
aqi = st.slider("Air Quality Index (AQI)", 0, 500, 120)
day_night = st.selectbox("Time of Day", ["Day", "Night"])

# ------------------ RISK CALCULATION ------------------

risk_score = 0

# Traffic Risk
risk_score += traffic_density * 0.3
risk_score += (60 - avg_speed) * 0.4 if avg_speed < 60 else 0
if construction == "Yes":
    risk_score += 15
if accident_reported == "Yes":
    risk_score += 20
if peak_hour == "Yes":
    risk_score += 10

# Weather Risk
weather_risk = {
    "Clear": 0,
    "Rain": 10,
    "Fog": 15,
    "Storm": 20,
    "Extreme Heat": 8,
    "Flooding": 25
}
risk_score += weather_risk[weather]

if visibility < 300:
    risk_score += 10

# Safety Risk
risk_score += (100 - helmet_usage) * 0.2
risk_score += (100 - seatbelt_usage) * 0.15
if speeding == "Yes":
    risk_score += 15

# Environmental Risk
if temperature > 40:
    risk_score += 10
if humidity > 80:
    risk_score += 5
if aqi > 200:
    risk_score += 10
if day_night == "Night":
    risk_score += 8

# ------------------ OUTPUT ------------------

st.header("📊 Risk Analysis Result")

if risk_score < 30:
    st.success(f"🟢 Low Risk Zone\n\nRisk Score: {int(risk_score)}")
elif risk_score < 60:
    st.warning(f"🟡 Moderate Risk Zone\n\nRisk Score: {int(risk_score)}")
else:
    st.error(f"🔴 High Risk Zone\n\nRisk Score: {int(risk_score)}")

st.markdown("### 🧠 Suggested Actions")
if risk_score >= 60:
    st.write("- Deploy traffic police")
    st.write("- Issue public safety alerts")
    st.write("- Reroute vehicles")
elif risk_score >= 30:
    st.write("- Monitor traffic closely")
    st.write("- Reduce speed limits")
else:
    st.write("- Traffic flow is normal")

st.markdown("---")
st.caption("CongestiQ | Smart Cities & Road Safety Initiative")

