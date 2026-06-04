import streamlit as st
import random
import pandas as pd

st.set_page_config(page_title="Думанның алғашқы программасы", page_icon="⛽", layout="centered")

# ---------- IPHONE STYLE ----------
st.markdown("""
<style>
body {
    background-color: #f2f2f7;
}

.main {
    background-color: #f2f2f7;
}

h1 {
    text-align: center;
    color: #111;
    font-weight: 800;
    font-size: 28px;
}

.card {
    background: white;
    padding: 15px;
    border-radius: 16px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    margin-bottom: 15px;
}

.stButton>button {
    background-color: #007aff;
    color: white;
    border-radius: 14px;
    height: 3em;
    width: 100%;
    font-size: 16px;
    font-weight: 600;
}
</style>
""", unsafe_allow_html=True)

st.title("⛽ Думанның алғашқы программасы")

# ---------- INPUTS ----------
st.markdown('<div class="card">', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    start_km = st.number_input("📍 Бастапқы км", value=0)
    fuel = st.number_input("⛽ Бензин (литр)", value=0.0)

with col2:
    consumption = st.number_input("📉 100 км шығын", value=9.2)
    days = st.number_input("📅 Күн саны", min_value=1, value=1)

st.markdown('</div>', unsafe_allow_html=True)

# ---------- CALC ----------
if st.button("Есептеу 🚀"):

    possible_km = (fuel / consumption) * 100

    st.success("✅ Есеп дайын!")

    # ---------- RESULT CARDS ----------
    st.markdown('<div class="card">', unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    c1.metric("⛽ Бензин", f"{fuel} L")
    c2.metric("🚗 Жол", f"{round(possible_km)} км")
    c3.metric("📉 100 км", f"{consumption} L")

    st.markdown('</div>', unsafe_allow_html=True)

    # ---------- DAILY SPLIT ----------
    base = possible_km / days

    current = start_km
    used = 0

    data = []

    for i in range(int(days)):
        if i == int(days) - 1:
            km = round(possible_km - used)
        else:
            km = round(random.uniform(base * 0.85, base * 1.15))
            used += km

        current += km

        data.append({
            "Күн": i + 1,
            "Күніне км": km,
            "Одометр": current
        })

    df = pd.DataFrame(data)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("📍 Күндік жоспар")
    st.dataframe(df, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.success("🔥 Дайын iPhone-style программа")
