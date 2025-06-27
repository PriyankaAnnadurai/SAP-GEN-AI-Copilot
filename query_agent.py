from langchain_community.agent_toolkits.sql.base import create_sql_agent
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.sql_database import SQLDatabase
from langchain.chat_models import ChatOpenAI
import os

os.environ["OPENAI_API_KEY"] = "your-api-key"

db = SQLDatabase.from_uri("sqlite:///data/sap_transactions.db")
llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")

agent_executor = create_sql_agent(
    llm=llm,
    toolkit=SQLDatabaseToolkit(db=db, llm=llm),
    verbose=True
)


def query_sap_nl(question):
    return agent_executor.run(question)
