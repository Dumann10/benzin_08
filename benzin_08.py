import streamlit as st
import random

st.title("⛽ Бензин калькулятор")

fuel = st.number_input("Бензин (литр)", min_value=0.0)
consumption = st.number_input("100 км-ге шығын (литр)", value=9.2)
days = st.number_input("Күн саны", min_value=1, step=1)
start_km = st.number_input("Бастапқы одометр (км)", value=0)

if st.button("Есептеу"):
    total_km = (fuel / consumption) * 100

    # Күндік базалық орташа
    base = total_km / days

    # Күндерге бөлу (дөңгелетілген)
    daily = []
    total = 0

    for i in range(int(days)):
        if i == int(days) - 1:
            value = round(total_km - total)  # соңғы күн түзету
        else:
            value = round(random.uniform(base * 0.8, base * 1.2))
            total += value
        daily.append(value)

    st.subheader("📊 Нәтиже")
    st.write(f"Жалпы жүріс: {round(total_km)} км")

    current_km = start_km

    st.write("📍 Күндік жоспар:")

    for i, km in enumerate(daily):
        current_km += km
        st.write(f"{i+1}-күн: +{km} км → {round(current_km)} км")
