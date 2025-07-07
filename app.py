from dotenv import load_dotenv
import os
import streamlit as st
from ui.chat_url_interface import show_url_chat_ui
from ui.chat_interface import show_chat_ui
from ui.dashboard import show_dashboard
from azure.ai.inference import ChatCompletionsClient
from azure.core.credentials import AzureKeyCredential

# Load environment variables
load_dotenv()
token = os.getenv("GITHUB_TOKEN")
print("Token Loaded:", token is not None)  # Optional: for debugging

# Azure AI Inference Client setup
endpoint = "https://models.github.ai/inference"
model = "openai/gpt-4.1"
client = ChatCompletionsClient(endpoint=endpoint,
                               credential=AzureKeyCredential(token))

# Streamlit UI setup
st.set_page_config(layout="wide", page_title="SAP GenAI Copilot")

# Sidebar menu
menu = st.sidebar.selectbox("📌 Choose Module",
                            ["📞 Chat Copilot", "📊 KPI Dashboard",
                             "📎 Chat with URL"])


if menu == "📞 Chat Copilot":
    show_chat_ui(client, model)  # pass the model + client if needed
elif menu == "📊 KPI Dashboard":
    show_dashboard()
elif menu == "📎 Chat with URL":
    show_url_chat_ui(client, model)
