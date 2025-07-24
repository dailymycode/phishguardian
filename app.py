import streamlit as st 
from google import genai  # +1 This needs to be included
from google.genai import types  # +1 
import pytesseract  # To extract text from images
from PIL import Image
import io
import os
from dotenv import load_dotenv  # To hide the API key

# API KEY save it in an .env file.
load_dotenv()
API = os.getenv("API_KEY")
client = genai.Client(api_key=API)

#  Analysis function
def analyze_email_with_gemini(email_text):
    prompt = f"""
Analyze the following email in detail and indicate the potential phishing risk as a percentage.
Explain risky expressions item by item. Provide clear advice to the user.

Email:
{email_text}

Response format:
1. Risk Assessment: %...
2. Reasons:
3. Dangerous Expressions:
4. Recommendations:
"""
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[prompt]
    )
    return response.text

#  Interface
st.set_page_config(page_title="PhishGuardian - AI Phishing Detection", layout="centered")
st.title("🛡️ PhishGuardian")
st.markdown("An AI-powered email phishing (scam) detection tool.")

#  Accept text or image input from user
option = st.radio("Select analysis type:", ["✉️ Email Text", "🖼️ Image (Extract Text via OCR)"])

email_text = ""

if option == "✉️ Email Text":
    email_text = st.text_area("📩 Paste the email text here:", height=200)

elif option == "🖼️ Image (Extract Text via OCR)":
    uploaded_image = st.file_uploader("Upload a screenshot of the email (.png/.jpg):", type=["png", "jpg", "jpeg"])
    if uploaded_image:
        img = Image.open(uploaded_image)
        st.image(img, caption="Uploaded Image", use_column_width=True)
        email_text = pytesseract.image_to_string(img)
        st.text_area("📝 Text extracted via OCR:", email_text, height=200)

#  Analyze button
if st.button("🔎 Analyze"):
    if email_text.strip() == "":
        st.warning("Please enter valid text or upload an image for analysis.")
    else:
        with st.spinner("AI is analyzing..."):
            result = analyze_email_with_gemini(email_text)
        st.markdown("### 📊 Analysis Result")
        st.markdown(result)


