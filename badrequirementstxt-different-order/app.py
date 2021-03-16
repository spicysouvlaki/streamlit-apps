import streamlit as st


st.write("this app has invalid characters at the top of the file")

msg = ""
with open("requirements.txt") as f:
    msg = f.readlines()

st.write("\trequirements.txt: ")
st.write(msg)
