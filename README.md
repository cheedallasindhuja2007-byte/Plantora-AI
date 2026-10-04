🌱 Plantora – AI Plant Care Assistant

Plantora is a Gemini-powered plant care assistant that helps users understand and monitor plant health through image analysis and conversational guidance. Users can upload a plant image, discuss visible issues with Plantora, receive practical care recommendations, and get a complete plant-care summary delivered to their email.

 ✨ Features

- 🌿 Plant image analysis using Google Gemini
- 🔍 Plant identification when possible
- 🩺 Detection and explanation of visible plant health issues
- 💬 Conversational follow-up questions
- 💧 Personalized guidance for watering, sunlight, soil, pruning, and general care
- 📋 Automatic conversation summary generation
- 📧 Email delivery of the personalized plant-care summary
- 🔐 Secure API key and email credential management using Streamlit Secrets

 🔄 How It Works

1.  User Onboarding
   - User enters their name and email address.

2.   Plant Analysis
   - User uploads a plant or leaf image.
   - Gemini analyzes the image and identifies visible plant conditions and symptoms.

3.  Conversational Assistance
   - Plantora explains possible causes and provides practical care recommendations.
   - Users can ask follow-up questions about their plant.

4.  Summary Generation
   - When the user finishes, Plantora reviews the conversation and generates a concise plant-care summary.

5.  Email Delivery
   - The generated summary is sent to the user's registered email address through Gmail SMTP.

🛠️ Tech Stack

- **Language:** Python
- **Frontend / Framework:** Streamlit
- **AI Model:** Google Gemini
- **AI SDK:** Google GenAI SDK
- **Email Service:** Gmail SMTP
- **Configuration:** Streamlit Secrets
- **Version Control:** Git & GitHub

 🏗️ Project Structure
PlantoraAI/
│
├── app.py
├── prompts.py
├── requirements.txt
├── README.md
├── .gitignore
│
└── .streamlit/
    └── secrets.toml
