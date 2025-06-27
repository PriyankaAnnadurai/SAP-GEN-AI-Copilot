
import fitz
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI


def load_policy_docs(path="data/policies/procurement_policy.pdf"):
    doc = fitz.open(path)
    text = " ".join([page.get_text() for page in doc])
    splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    return splitter.split_text(text)


def setup_rag():
    texts = load_policy_docs()
    embeddings = OpenAIEmbeddings()
    vectordb = FAISS.from_texts(texts, embedding=embeddings)
    retriever = vectordb.as_retriever()
    return RetrievalQA.from_chain_type(
        llm=ChatOpenAI(), retriever=retriever
    )


rag_chain = setup_rag()


def ask_policy_question(q):
    return rag_chain.run(q)
