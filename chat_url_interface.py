import streamlit as st
import requests
from bs4 import BeautifulSoup
from azure.ai.inference.models import SystemMessage, UserMessage


def extract_text_from_url(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        return ' '.join([p.text for p in soup.find_all('p')])
    except Exception as e:
        return f"Failed to extract content: {e}"


def show_url_chat_ui(client, model):
    st.title("📎 Chat with URL")

    # Input for URL
    url = st.text_input("Enter a URL:", key="url_input")

    # Fetch button
    if st.button("Fetch"):
        with st.spinner("Extracting content..."):
            context = extract_text_from_url(url)
            st.session_state["webpage_context"] = context
        st.success("Content fetched! Now ask a question.")

    # Show input box and button only if content is available
    if "webpage_context" in st.session_state:
        st.text_area("📄 Webpage Context (read-only)",
                     st.session_state["webpage_context"], height=150,
                     disabled=True)
        question = st.text_input("Ask a question about the webpage:",
                                 key="query_input")

    if st.button("Submit Question"):
        with st.spinner("Thinking..."):
            system_prompt = (
                f"You are a helpful assistant. "
                f"Use:\n\n{st.session_state['webpage_context']}"
            )
            response = client.complete(
                messages=[
                    SystemMessage(system_prompt),
                    UserMessage(question)
                ],
                model=model
            )
            st.markdown("**Answer:**")
            st.success(response.choices[0].message.content)
