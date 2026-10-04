from google import genai
from google.genai import types
import streamlit as st
from prompts import SYSTEM_PROMPT, WELCOME_MESSAGE_TEMPLATE, SUMMARY_REQUEST_PROMPT, EMAIL_SUBJECT, EMAIL_BODY_TEMPLATE

GEMINI_API_KEY=st.secrets["GEMINI_API_KEY"]

@st.cache_resource
def get_gemini_client():
    return genai.Client(api_key=GEMINI_API_KEY)

gemini_client=get_gemini_client()
MODEL_NAME="gemini-3.5-flash-lite"

import smtplib
from email.mime.text import MIMEText
GMAIL_ADDRESS = st.secrets["GMAIL_ADDRESS"]
GMAIL_APP_PASSWORD = st.secrets["GMAIL_APP_PASSWORD"]
def send_email(to_address, subject, body):

    try:
        message = MIMEText(body)
        message["Subject"] = subject
        message["From"] = GMAIL_ADDRESS
        message["To"] = to_address

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(GMAIL_ADDRESS, GMAIL_APP_PASSWORD)
            server.send_message(message)

        return True, "Email sent successfully"

    except Exception as e:
        return False, str(e)


def render_msg(message):
    with st.chat_message(message["Role"]):
        if message["Kind"]=="text":
            st.write(message["Content"])
        elif message["Kind"]=="image":
            st.image(message["Content"])

def add_msg(role,kind,content):
    st.session_state.messages.append({
        "Role":role,"Kind":kind,"Content":content
    })
    render_msg(st.session_state.messages[-1])
def ask_gemini(parts):
    try:
        return st.session_state.chat.send_message(parts).text
    except Exception as error:
        return f"Sorry, Something went wrong: {error}"
if "onboarded" not in st.session_state:
    st.session_state.onboarded = False

if "messages" not in st.session_state:
    st.session_state.messages = []

if not st.session_state.onboarded:
    st.title("Plantora AI 🌱")
    st.caption("See. Understand. Care. Grow. 🌿")
    with st.form("onboarding_form"):
        name=st.text_input("Enter your name")
        email_id=st.text_input(
                   "Enter your email address",
                   help="This Email Id will help Plantora AI to text you"  
        )
        submitted=st.form_submit_button("Let's Go")
    if submitted:
        if not name.strip() or not email_id.strip():
            st.warning("Please enter your details")
        else:
            st.session_state.name = name.strip()
            st.session_state.email_id = email_id.strip() 
            st.session_state.chat=gemini_client.chats.create(
                model=MODEL_NAME,
                config=types.GenerateContentConfig(system_instruction=SYSTEM_PROMPT)
            )
            st.session_state.messages=[]      
            st.session_state.onboarded=True
            st.rerun()
    st.stop()  

header_col,button_col=st.columns([5,2],vertical_alignment="center")
with header_col:
    st.title("Plantora AI 🌱")
with button_col:
    send_disabled=len(st.session_state.messages)<=1
    if st.button("Send Summary to Email",disabled=send_disabled, use_container_width=True):
        with st.spinner("Generating Summary..."):
            summary=ask_gemini([SUMMARY_REQUEST_PROMPT])
        success,info=send_email(st.session_state.email_id,EMAIL_SUBJECT,EMAIL_BODY_TEMPLATE.format(name=st.session_state.name, summary=summary))
        if success:
            st.success("Summary sent to your email successfully!")
        else:
            st.error(f"failed to send: {info}")
   
st.caption(f"Logged in as {st.session_state.name} and updates go to {st.session_state.email_id}")                 
if not  st.session_state.messages:
    add_msg("assistant","text",WELCOME_MESSAGE_TEMPLATE.format(name=st.session_state.name))
else:
    for message in st.session_state.messages:
        render_msg(message)

user_input=st.chat_input(
                "Upload a photo or type your message here...",
                accept_file=True,
                file_type=["png","jpg","jpeg"]
        )
if user_input:
    photo=user_input.files[0] if user_input.files else None
    text=user_input.text
    parts=[]
    if photo is not None:
        photo_bytes=photo.getvalue()
        add_msg("user","image",photo_bytes)
        parts.append(types.Part.from_bytes(data=photo_bytes,mime_type=photo.type))
    if text:
        add_msg("user","text",text)
        parts.append(text)
    elif photo is not None:
        parts.append("Please analyze the uploaded photo and provide insights about the plant's condition.")
    with st.spinner("Analyzing..."):
        answer=ask_gemini(parts)
    add_msg("assistant","text",answer)


