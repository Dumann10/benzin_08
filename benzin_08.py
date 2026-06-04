import streamlit as st
import random

st.set_page_config(page_title="Бензин калькулятор", page_icon="⛽", layout="centered")

st.markdown("""
    <style>
        .main {
            background-color: #0f172a;
            color: white;
        }
        .stButton>button {
            background-color: #22c55e;
            color: white;
            border-radius: 10px;
            height: 3em;
            width: 100%;
            font-size: 16px;
        }
    </style>
""", unsafe_allow_html=True)

st.title("⛽ Бензин калькулятор")
st.write("Күндік жүріс пен маршрут жоспарын автоматты есептеу")

col1, col2 = st.columns(2)

with col1:
    fuel = st.number_input("⛽ Бензин (литр)", min_value=0.0)

    consumption = st.number_input("📉 100 км шығын", value=9.2)

with col2:
    days = st.number_input("📅 Күн саны", min_value=1, step=1)

    start_km = st.number_input("🚗 Бастапқы км", value=0)

if st.button("Есептеу 🚀"):

    total_km = (fuel / consumption) * 100
    base = total_km / days

    daily = []
    total = 0

    for i in range(int(days)):
        if i == int(days) - 1:
            value = round(total_km - total)
        else:
            value = round(random.uniform(base * 0.85, base * 1.15))
            total += value
        daily.append(value)

    st.success(f"Жалпы жүріс: {round(total_km)} км")

    current = start_km

    st.subheader("📍 Күндік жоспар")

    for i, km in enumerate(daily):
        current += km
        st.write(f"**{i+1}-күн:** +{km} км → {round(current)} км")
