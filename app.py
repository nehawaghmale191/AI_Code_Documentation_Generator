import streamlit as st
from parser import extract_code_info
from generator import create_documentation
import os
print(create_documentation)
st.title("AI Code Documentation Generator")

uploaded_file = st.file_uploader(
    "Upload Python File",
    type=["py"]
)

if uploaded_file:

    filepath = os.path.join(
        "uploads",
        uploaded_file.name
    )

    with open(filepath, "wb") as f:
        f.write(uploaded_file.getbuffer())

    functions, classes = extract_code_info(filepath)
    st.write("Functions Extracted:")
    st.write(functions)
    st.write("Classes Extracted:")
    st.write(classes)
    docs = create_documentation(functions, classes)

    st.subheader("Generated Documentation")

    st.text(docs)