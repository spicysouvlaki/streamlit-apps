import streamlit as st

st.title("I throw errors!")

checked = st.checkbox('click for error')

if checked:
    print(1 / 0)

