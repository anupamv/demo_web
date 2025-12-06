import streamlit as st

st.title("Welcome to AVSTech")
st.header("Python")
st.subheader("Java")
st.markdown("I love python")

name = st.text_input("Enter your name: ")
fname = st.text_input("Enter your father name: ")
addr = st.text_area("Enter your address: ")
classdata = st.selectbox("Enter your class: ",(1,2,3,4,5,6))
button = st.button("Done")
if button :
    st.markdown(f"""
    Name: {name}
    Father's Name: {fname}
    Address: {addr}
    Class: {classdata}""")
