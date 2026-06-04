
import streamlit as st
import random
import pandas as pd

st.set_page_config(page_title="Benzin Calculator", page_icon="⛽", layout="centered")

st.title("⛽ Бензин & Километраж калькулятор")

start_km = st.number_input("📍 Бастапқы одометр", value=0)
end_km = st.number_input("🏁 Соңғы одометр", value=0)
days = st.number_input("📅 Күн саны", min_value=1, value=1, step=1)

consumption = st.number_input("⛽ 100 км шығын (литр)", value=9.2)

if st.button("Есептеу 🚀"):

    total_km = end_km - start_km

    if total_km <= 0:
        st.error("Соңғы км бастапқыдан үлкен болуы керек!")
    else:
        # --- BENZIN CALC ---
        total_liters = (total_km / 100) * consumption

        st.success(f"🚗 Жалпы жүріс: {round(total_km)} км")
        st.info(f"⛽ Жалпы бензин: {round(total_liters, 2)} L")

        # --- DAILY SPLIT ---
        base = total_km / days

        current = start_km
        used = 0

        data = []

        for i in range(int(days)):
            if i == int(days) - 1:
                km = round(total_km - used)
            else:
                km = round(random.uniform(base * 0.8, base * 1.2))
                used += km

            current += km

            data.append({
                "Күн": i + 1,
                "Жүріс (км)": km,
                "Одометр": current
            })

        df = pd.DataFrame(data)

        st.subheader("📊 Күндік жоспар")
        st.dataframe(df, use_container_width=True)

        st.subheader("📈 График")
        st.line_chart(df["Жүріс (км)"])
