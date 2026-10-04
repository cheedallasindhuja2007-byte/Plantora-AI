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

File Description
File	Purpose
app.py:	Main Streamlit application and user interaction flow
prompts.py:	System, welcome, summary, and email prompts
requirements.txt:	Python dependencies
.gitignore:	Prevents sensitive and unnecessary files from being committed
secrets.toml:	Stores API keys and email credentials locally


⚙️ Installation & Setup
1. Clone the Repository
git clone https://github.com/cheedallasindhuja2007-byte/Plantora-AI
cd Plantora

3. Create a Virtual Environment
python -m venv venv

For Windows:

venv\Scripts\activate
3. Install Dependencies
pip install -r requirements.txt
4. Configure Secrets

Create:

.streamlit/secrets.toml

Add:

GEMINI_API_KEY = "your_gemini_api_key"
GMAIL_ADDRESS = "your_gmail_address"
GMAIL_APP_PASSWORD = "your_gmail_app_password"

⚠️ Never commit secrets.toml to GitHub.

▶️ Run Locally

Start the Streamlit application:

streamlit run app.py

The application will open in your browser.

📧 Email Summary

Plantora uses Gmail SMTP to send the generated plant-care summary.

The user's email address is used as the destination address, while the configured Gmail account acts as the sender.

Plantora
   ↓
Generate Summary with Gemini
   ↓
Gmail SMTP
   ↓
User's Email
🔐 Security

Sensitive credentials are managed using Streamlit Secrets.

The following information should never be committed to the repository:

Gemini API key
Gmail App Password
Other private credentials

Example .gitignore:

.streamlit/secrets.toml
venv/
__pycache__/
*.pyc
🚀 Deployment

Plantora can be deployed using Streamlit Community Cloud.

Deployment steps:

Push the project to GitHub.
Connect the GitHub repository to Streamlit Community Cloud.
Select app.py as the main application file.
Add the required secrets in the Streamlit deployment settings.
Deploy the application.


🎯 Use Cases
Plant health monitoring
Beginner-friendly plant care
Identifying visible plant problems
Understanding common plant stress symptoms
Getting personalized plant-care guidance
Receiving a complete plant-care summary by email


🔮 Future Enhancements
🌱 Plant-care history and user profiles
📊 Long-term plant health tracking
🔔 Watering and care reminders
🗂️ Multiple plant profiles
📱 Mobile-friendly improvements
🌍 Support for more plant species and languages
