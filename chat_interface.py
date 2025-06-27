import streamlit as st


def show_chat_ui(client, model):
    from azure.ai.inference.models import SystemMessage, UserMessage
    st.title("📞 SAP GenAI Chat Copilot")

    query = st.text_input("Ask a question:")
    if st.button("Send") and query:
        response = client.complete(
            messages=[
                SystemMessage("You are an SAP expert."),
                UserMessage(query)
            ],
            model=model
        )
        st.markdown("**Answer:**")
        st.success(response.choices[0].message.content)
