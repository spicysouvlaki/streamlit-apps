import streamlit as st
import sys
import coloredlogs, logging

coloredlogs.install()

st.title("this app prints in color! :rainbow:")

st.write("stderr is a tty",sys.stderr.isatty() )
st.write("stdout is a tty",sys.stdout.isatty() )

logging.info("beep boop")
logging.error("boop beep")
logging.warning("ACK ACK!!")
logging.critical("I love streamlit")

user_input = st.text_input("test out logging here")
logging.info(user_input)
