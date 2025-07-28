import streamlit as st

st.title("IR50 Calculator")

bpt = st.number_input("Enter IR50:", value=0.0)

intr_values = []
for i in range(10):
    intr = st.number_input(f"Enter for Member {i+1}:", key=i)
    intr_values.append(intr)

if st.button("Calculate"):
    st.subheader("Results:")
    for i, intr in enumerate(intr_values):
        result = bpt * intr / 25
        st.write(f"Member {i+1}: {round(result, 2)}")
