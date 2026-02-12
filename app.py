import streamlit as st

st.title("💧 Water Jug Game")

# Input section
capA = st.number_input("Capacity of Jug A", min_value=1, value=4)
capB = st.number_input("Capacity of Jug B", min_value=1, value=3)
target = st.number_input("Target", min_value=1, value=2)

if "a" not in st.session_state:
    st.session_state.a = 0
    st.session_state.b = 0
    st.session_state.moves = 0

def update_state(new_a, new_b):
    st.session_state.a = new_a
    st.session_state.b = new_b
    st.session_state.moves += 1

st.write(f"### Jug A: {st.session_state.a}/{capA}")
st.write(f"### Jug B: {st.session_state.b}/{capB}")
st.write(f"### Moves: {st.session_state.moves}")

col1, col2 = st.columns(2)

with col1:
    if st.button("Fill A"):
        update_state(capA, st.session_state.b)

    if st.button("Empty A"):
        update_state(0, st.session_state.b)

    if st.button("Pour A → B"):
        transfer = min(st.session_state.a, capB - st.session_state.b)
        update_state(st.session_state.a - transfer,
                     st.session_state.b + transfer)

with col2:
    if st.button("Fill B"):
        update_state(st.session_state.a, capB)

    if st.button("Empty B"):
        update_state(st.session_state.a, 0)

    if st.button("Pour B → A"):
        transfer = min(st.session_state.b, capA - st.session_state.a)
        update_state(st.session_state.a + transfer,
                     st.session_state.b - transfer)

if st.session_state.a == target or st.session_state.b == target:
    st.success("🎉 You Win!")

if st.button("Reset Game"):
    st.session_state.a = 0
    st.session_state.b = 0
    st.session_state.moves = 0
