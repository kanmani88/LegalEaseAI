import streamlit as st
st.title("LegalEase - AI Legal Document Generator")
doc_type = st.selectbox("Document Type", ["Rental Agreement", "NDA", "Employment Contract"]
parties = st.text_input("parties Involved")
terms = st.text_area("Terms and conditions")
if st.button("Generate"):
    st.success(f"Generated {doc_type} for {parties}")  
