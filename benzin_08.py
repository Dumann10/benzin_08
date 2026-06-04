import streamlit as st

st.title("⛽ Бензин калькулятор")

# Бастапқы деректер
fuel = st.number_input("Бензин (литр)", min_value=0.0)
consumption = st.number_input("100 км-ге шығын (литр)", value=9.2)
days = st.number_input("Күн саны", min_value=1, step=1)
start_km = st.number_input("Бастапқы одометр (км)", value=0)

if st.button("Есептеу"):
    total_km = (fuel / consumption) * 100

    km_per_day = total_km / days

    st.subheader("📊 Нәтиже")
    st.write(f"Жалпы жүріс: {total_km:.0f} км")

    st.write(f"Күніне орташа: {km_per_day:.0f} км")

    st.write("📍 Күндік жоспар:")

    current_km = start_km
    for i in range(int(days)):
        current_km += km_per_day
        st.write(f"{i+1}-күн: {current_km:.0f} км")
