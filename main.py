import streamlit as st
import pandas as pd

st.title("Helloooo universeeeeeee")
st.write("pat251463635456ter")

st.markdown("# My age")
run_btn = st.button("Run")
if run_btn:
    st.markdown("Button has already been clicked")

# Create columns
cols = st.columns(2)  # Fixed: Changed st.column to st.columns
with cols[0]:  # Access the first column
    age_input = st.number_input("Input your age")
    st.markdown(f"Your age is {age_input}")

with cols[1]:  # Access the second column
    st.markdown("# NLP Task")
    text_inp = st.text_input("Input your text")
    st.markdown(f"Your input is: {text_inp}")
