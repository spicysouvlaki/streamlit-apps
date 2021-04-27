import streamlit as st
import os

st.write(os.environ)
ok = st.checkbox("refresh")
if ok:
    print("refresh")
    st.write(os.environ)
