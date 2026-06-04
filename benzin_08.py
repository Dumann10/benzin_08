import streamlit as st
import math
import random

st.title("🚗 Километраж & Одометр калькулятор")

start_km = st.number_input("📍 Бастапқы километраж", value=0)
end_km = st.number_input("🏁 Соңғы километраж", value=0)
days = st.number_input("📅 Күн саны", min_value=1, value=1, step=1)

if st.button("Есептеу 🚀"):

    total_km = end_km - start_km

    if total_km <= 0:
        st.error("Соңғы км бастапқыдан үлкен болуы керек!")
    else:
        st.success(f"Жалпы жүрген жол: {round(total_km)} км")

        base = total_km / days

        st.subheader("📊 Күндік есеп")

        current_odo = start_km
        used_total = 0

        for i in range(int(days)):
            if i == int(days) - 1:
                km = round(total_km - used_total)  # соңғы күн түзету
            else:
                km = round(random.uniform(base * 0.8, base * 1.2))
                used_total += km

            current_odo += km

            st.write(
                f"**{i+1}-күн:** "
                f"+{km} км | "
                f"Одометр: {current_odo} км"
            )
