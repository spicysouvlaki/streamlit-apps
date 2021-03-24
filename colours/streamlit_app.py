import streamlit as st
import coloredlogs, logging

coloredlogs.install()

st.title("this app prints in color! :rainbow:")

printInColor = st.checkbox("press to log colours")
justPrint = st.checkbox("just print")

if printInColor:
    logging.info("colorful")

if justPrint:
    print("just printing")

