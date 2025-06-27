from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI()


def suggest_optimization(prompt: str) -> str:
    """
    Suggests SAP process optimizations using the LLM.
    """
    full_prompt = (
        "You are an SAP operations expert. "
        "Based on this input, suggest optimizations:\n\n"
        f"{prompt}"
    )
    return llm.predict(full_prompt)
