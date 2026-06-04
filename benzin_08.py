import streamlit as st
import random
import pandas as pd

st.set_page_config(page_title="Benzin Pro", page_icon="⛽", layout="centered")

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

st.title("⛽ Benzin Pro Calculator")

# ---------- INPUT ----------
col1, col2 = st.columns(2)

with col1:
    start_km = st.number_input("📍 Бастапқы км", value=0)
    fuel = st.number_input("⛽ Бензин (литр)", value=0.0)

with col2:
    days = st.number_input("📅 Күн саны", min_value=1, value=1)

consumption = st.number_input("📉 100 км шығын (L)", value=9.2)

# ---------- CALC ----------
if st.button("🚀 Есептеу"):

    # бензинмен мүмкін жол
    possible_km = (fuel / consumption) * 100

    st.success("✅ Есеп дайын!")

    st.subheader("📊 Нәтиже")

    c1, c2, c3 = st.columns(3)
    c1.metric("⛽ Бензин", f"{fuel} L")
    c2.metric("🚗 Жол", f"{round(possible_km)} км")
    c3.metric("📉 100 км", f"{consumption} L")

    # ---------- DAILY SPLIT ----------
    base = possible_km / days

    current_km = start_km
    used = 0

    data = []

    for i in range(int(days)):
        if i == int(days) - 1:
            km = round(possible_km - used)  # БЕНЗИН ТОЛЫҚ ТАУСЫЛАДЫ
        else:
            km = round(random.uniform(base * 0.85, base * 1.15))
            used += km

        current_km += km

        data.append({
            "Күн": i + 1,
            "Күніне км": km,
            "Жалпы одометр": current_km
        })

    df = pd.DataFrame(data)

    st.subheader("📍 Күндік жүріс (жинақталып отырады)")
    st.dataframe(df, use_container_width=True)

    st.success("🔥 Бензин толық жұмсалды + күндерге бөлінді")
