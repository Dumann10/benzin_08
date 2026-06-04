
import streamlit as st
import random
import pandas as pd

st.set_page_config(page_title="Benzin Pro", page_icon="⛽", layout="centered")

# ---- STYLE ----
st.markdown("""
    <style>
    .main {
        background-color: #0f172a;
    }
    h1 {
        color: #22c55e;
        text-align: center;
    }
    .stButton>button {
        background-color: #22c55e;
        color: white;
        border-radius: 12px;
        height: 3em;
        width: 100%;
        font-size: 16px;
    }
    </style>
""", unsafe_allow_html=True)

st.title("⛽ Benzin PRO Calculator")
st.write("🚗 Километраж + бензин + күндік жоспар")

# ---- INPUTS ----
col1, col2 = st.columns(2)

with col1:
    start_km = st.number_input("📍 Бастапқы км", value=0)
    fuel_used = st.number_input("⛽ Жалпы бензин (L)", value=0.0)

with col2:
    end_km = st.number_input("🏁 Соңғы км", value=0)
    days = st.number_input("📅 Күн саны", min_value=1, value=1)

consumption = st.number_input("📉 100 км шығын (L)", value=9.2)

# ---- CALC ----
if st.button("Есептеу 🚀"):

    total_km = end_km - start_km

    if total_km <= 0:
        st.error("❌ Соңғы км бастапқыдан үлкен болуы керек!")
    else:
        st.success("✅ Есептеу дайын!")

        st.subheader("📊 Нәтиже")
        st.info(f"🚗 Жалпы жүріс: {round(total_km)} км")
        st.info(f"⛽ Сен енгізген бензин: {fuel_used} L")
        st.info(f"📉 100 км шығын: {consumption} L")

        total_liters_calc = (total_km / 100) * consumption

        st.success(f"📦 Есептелген бензин: {round(total_liters_calc, 2)} L")

        # ---- DAILY SPLIT ----
        base = total_km / days

        current = start_km
        used = 0

        data = []

        for i in range(int(days)):
            if i == int(days) - 1:
                km = round(total_km - used)
            else:
                km = round(random.uniform(base * 0.85, base * 1.15))
                used += km

            current += km

            data.append({
                "Күн": i + 1,
                "Жүріс (км)": km,
                "Одометр": current
            })

        df = pd.DataFrame(data)

        st.subheader("📍 Күндік жоспар")
        st.dataframe(df, use_container_width=True)

        st.success("🔥 Дайын!")
