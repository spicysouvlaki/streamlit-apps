import streamlit as st
import os

st.write(os.environ)
ok = st.checkbox("refresh")
    print("refresh")
    st.write(os.environ)
