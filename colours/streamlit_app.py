import streamlit as st
import sys
import coloredlogs, logging

coloredlogs.install()

st.title("this app prints in color! :rainbow:")

st.write("stderr is a tty",sys.stderr.isatty() )
st.write("stdout is a tty",sys.stdout.isatty() )
# print('\033[4;35m purple')
# logging.info('\033[4;35m purple')

logging.info("beep boop")
logging.error("boop beep")
logging.warning("ACK ACK!!")
printInColor = st.checkbox("press to log colours")
justPrint = st.checkbox("just print")

if printInColor:
    logging.info("colorful")

if justPrint:
    print("just printing")

