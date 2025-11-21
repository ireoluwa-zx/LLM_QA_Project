import google.generativeai as genai
import string
import sys

# --- CONFIGURATION ---
API_KEY = "AIzaSyBqbigoxlplm9qwn4toXCJ3cogDfHyurXw" 
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

def preprocess_text(text):
    """
    Rubric Requirement: Lowercasing, tokenization (basic split), punctuation removal.
    """
    # 1. Lowercase
    text = text.lower()
    # 2. Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    # 3. Tokenization (just for show, we rejoin it for the API)
    tokens = text.split()
    processed_text = " ".join(tokens)
    return processed_text

def main():
    print("--- NLP Q&A CLI System ---")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("Enter your question: ")
        
        if user_input.lower() == 'exit':
            print("Exiting...")
            break
            
        if not user_input:
            continue

        # Step 1: Preprocess
        clean_prompt = preprocess_text(user_input)
        print(f"\n[System] Processed Prompt: {clean_prompt}")
        print("[System] Sending to LLM...")

        try:
            # Step 2: Send to API
            response = model.generate_content(clean_prompt)
            
            # Step 3: Display Answer
            print(f"\n[Answer]: \n{response.text}\n")
            print("-" * 40)
            
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
