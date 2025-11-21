import streamlit as st
import google.generativeai as genai
import string
# ... other imports

# Use Streamlit Secrets for the API key
if 'GEMINI_API_KEY' in st.secrets:
    # 1. Configure the Generative AI library with the secret key
    genai.configure(api_key=st.secrets['GEMINI_API_KEY'])
    # 2. Use a secure model name from the secrets (or a safe default)
    model_name = st.secrets.get('GEMINI_MODEL', 'models/gemini-2.5-flash')
    model = genai.GenerativeModel(model_name)
else:
    st.error("API Key not found in Streamlit Secrets. Please check your app settings.")
    model = None

# --- SIDEBAR: MODEL DEBUGGER ---
st.sidebar.header("System Check")
try:
    # Ask Google for available models
    available_models = []
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            available_models.append(m.name)
    
    # Display them in the sidebar so you can copy the right one
    st.sidebar.success("API Connection: Success!")
    st.sidebar.write("Available Models:")
    selected_model_name = st.sidebar.selectbox("Pick a model:", available_models)
    
    # Use the selected model dynamically
    model = genai.GenerativeModel(selected_model_name)

except Exception as e:
    st.sidebar.error(f"API Error: {e}")
    model = None

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
    if question and model:
        processed = preprocess_text(question)
        st.subheader("Processed Question:")
        st.code(processed)
        
        with st.spinner(f"Consulting {selected_model_name}..."):
            try:
                response = model.generate_content(processed)
                st.subheader("Answer:")
                st.write(response.text)
            except Exception as e:
                st.error(f"Error: {e}")
    elif not model:
        st.error("Model not loaded. Check the sidebar for API errors.")
    else:
        st.warning("Please enter a question.")




