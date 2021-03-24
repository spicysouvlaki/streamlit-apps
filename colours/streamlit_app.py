import streamlit as st
import os
import coloredlogs, logging

coloredlogs.install()

st.title("this app prints in color! :rainbow:")

st.write("stderr is a tty",sys.stderr.isatty() )
st.write("stdout is a tty",sys.stdout.isatty() )
print('\033[4;35m purple')
logging.info('\033[4;35m purple')

printInColor = st.checkbox("press to log colours")
justPrint = st.checkbox("just print")

if printInColor:
    logging.info("colorful")

if justPrint:
    print("just printing")

