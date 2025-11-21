import streamlit as st
import google.generativeai as genai
import string

# --- CONFIGURATION ---
API_KEY = "YAIzaSyBqbigoxlplm9qwn4toXCJ3cogDfHyurXw" 
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# --- PREPROCESSING FUNCTION ---
def preprocess_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    tokens = text.split()
    return " ".join(tokens)

# --- STREAMLIT UI ---
st.title("NLP Q&A System")
st.write("Project 2: LLM API Integration")

# Input
question = st.text_input("Enter your question here:")

if st.button("Get Answer"):
    if question:
        processed = preprocess_text(question)
        st.subheader("Processed Question:")
        st.code(processed)

        with st.spinner("Thinking..."):
            try:
                response = model.generate_content(processed)
                st.subheader("Answer:")
                st.write(response.text)
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please enter a question.")
