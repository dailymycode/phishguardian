# 🛡️ PhishGuardian - AI-Powered Phishing Email Analyzer

**PhishGuardian** is an AI-based tool that analyzes email content and detects potential **phishing** risks as a percentage.  
It uses **Google's Gemini model** for natural language understanding and **OCR (Tesseract)** for extracting text from screenshots.

---

## 🚀 Features

- 📩 Analyze plain email text
- 🖼️ Extract text from screenshots using OCR (optional)
- 📊 Shows phishing risk as a percentage
- ⚠️ Highlights suspicious expressions
- ✅ Gives personalized safety recommendations

---

## ⚙️ Installation

### 1. Install the required Python packages:

```bash
pip install streamlit

## 🔐 Add Your API Key 

To use the Gemini model, you'll need an API key.

1. Get a free API key from [Google AI Studio](https://makersuite.google.com/app).
2. In your project root directory, create a `.env` file and add the following line:

## ▶️ Run the App

After installing the dependencies and setting up your API key, you can start the application with the following command:


streamlit run app.py
