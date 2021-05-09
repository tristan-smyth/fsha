import streamlit

streamlit.write("Addition")

firstVar = streamlit.text_input(
    label="First Varible",
    value=0)

secondVar = streamlit.text_input(
    label="Second Varible",
    value=0)

if streamlit.button(label="submit"):
    streamlit.write("Output")
    streamlit.write(int(firstVar) + int(secondVar))