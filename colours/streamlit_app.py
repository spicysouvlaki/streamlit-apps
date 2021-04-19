import streamlit as st
import sys
import coloredlogs, logging

coloredlogs.install()

st.title("this app prints in color! :rainbow:")

st.write("If true, python will think we're talking to a terminal and color output by itself!")
st.write("stderr is a tty?", sys.stderr.isatty())

logging.info("beep boop")
logging.error("boop beep")
logging.warning("ACK ACK!!")
logging.critical("I love Streamlit")



st.write("these codes are manually configured and just exist for samples")
from colorama import Fore, Back, Style
palette = [
    Fore.RED + "red color: #ff4b4b",
    Back.RED + "red background-color: #ff4b4b",
    Fore.BLUE+"blue color: #1c83e1",
    Back.BLUE+"blue background-color: #1c83e1",
    Fore.CYAN+"cyan color: #00c0f2",
    Back.CYAN+"cyan background-color: #00c0f2",
    Fore.WHITE+"white color: #000",
    Back.White+Fore.BLACK+"black on white background-color: #000",
    Back.BLACK+Fore.WHITE+"white on black background-color: #fff",
    Fore.GREEN+"green color: #21c454",
    Back.GREEN+"green background-color: #21c454",
    Fore.YELLOW+"yellow color: #ffe312",
    Back.YELLOW+"yellow background-color: #ffe312",
    Fore.MAGENTA+"magenta color: #f63366",
    Back.MAGENTA+"magenta background-color: #f63366",
]

user_input = st.text_input("test out logging here", value='🎈 welcome to my demo 🎈')
logging.info(user_input)
