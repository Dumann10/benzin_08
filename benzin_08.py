
import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="Benzin Pro Max", page_icon="⛽", layout="centered")

# ---------- STYLE ----------
st.markdown("""
<style>
.main {
    background-color: #0b1220;
}
h1 {
    color: #22c55e;
    text-align: center;
    font-weight: 800;
}
.stButton>button {
    background-color: #22c55e;
    color: white;
    border-radius: 12px;
    height: 3em;
    width: 100%;
    font-size: 16px;
}
div[data-testid="stMetric"] {
    background-color: #111827;
    padding: 15px;
    border-radius: 12px;
}
</style>
""", unsafe_allow_html=True)

st.title("⛽ Benzin Pro MAX")
st.write("🚗 Ақылды маршрут + бензин толық есеп")

# ---------- INPUT ----------
col1, col2 = st.columns(2)

with col1:
    start_km = st.number_input("📍 Бастапқы км", value=0)
    fuel = st.number_input("⛽ Бензин (литр)", value=0.0)

with col2:
    end_km = st.number_input("🏁 Соңғы км", value=0)
    days = st.number_input("📅 Күн саны", min_value=1, value=1)

consumption = st.number_input("📉 100 км шығын (L)", value=9.2)

# ---------- CALC ----------
if st.button("🚀 Есептеу"):

    total_km = end_km - start_km

    if total_km <= 0:
        st.error("❌ Соңғы км дұрыс емес!")
    else:
        st.success("✅ Есеп дайын!")

        # --- бензинге негізделген нақты қашықтық ---
        possible_km_by_fuel = (fuel / consumption) * 100

        # Екеуінің минимумы → бензин толық кетеді
        real_km = min(total_km, possible_km_by_fuel)

        st.subheader("📊 Негізгі нәтиже")

        c1, c2, c3 = st.columns(3)
        c1.metric("🚗 Жүріс", f"{round(real_km)} км")
        c2.metric("⛽ Бензин", f"{fuel} L")
        c3.metric("📉 100 км", f"{consumption} L")

        # ---------- DAILY SPLIT ----------
        base = real_km / days

        current = start_km
        used_km = 0

        data = []

        for i in range(int(days)):
            if i == int(days) - 1:
                km = round(real_km - used_km)
            else:
                km = round(random.uniform(base * 0.85, base * 1.15))
                used_km += km

            current += km

            data.append({
                "Күн": i + 1,
                "Жүріс (км)": km,
                "Одометр": current
            })

        df = pd.DataFrame(data)

        st.subheader("📍 Күндік жоспар")
        st.dataframe(df, use_container_width=True)

        st.success("🔥 Бензин толық пайдаланылды (баланс сақталған)")
