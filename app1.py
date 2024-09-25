import streamlit as st

text_input = st.text_input("Enter some text")

if st.button("submit"):
    st.write("You've inputted:", text_input)