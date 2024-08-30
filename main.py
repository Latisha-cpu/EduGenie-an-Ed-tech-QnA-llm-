import streamlit as st
from langchain import get_qa_chain, create_vector_db

st.title("EduGenie🤖")


question = st.text_input("How can i assist you? ")

if question:
    chain = get_qa_chain()
    response = chain(question)

    st.header("Answer")
    st.write(response["result"])






