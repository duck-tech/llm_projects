from langchain.chat_models import ChatOpenAI
from langchain.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
)
from langchain.schema import SystemMessage
from langchain.agents import OpenAIFunctionsAgent, AgentExecutor
from dotenv import load_dotenv

from tools.sql import run_query_tool, list_tables, describe_tables_tool
load_dotenv()

chat = ChatOpenAI()

tables = list_tables()
prompt = ChatPromptTemplate(
    messages=[
        SystemMessage(content=(
            ### 優化1: system message使得每次都會呼叫describe_tables, 得到的答案更穩定
            "You are an AI that has acess to a SQLite database.\n"
            f"The database has tables of: {tables}\n"
            "Do not make any assumptions about what tables exist "
            "or what columns exist.Instead, use the 'describe_tables' function"
            )),
        HumanMessagePromptTemplate.from_template("{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad") # 像是memory 
    ]
)
tools = [run_query_tool, describe_tables_tool]

agent = OpenAIFunctionsAgent(
    llm=chat, 
    prompt=prompt,
    tools = tools
)

agent_executor = AgentExecutor(
    agent=agent,
    verbose=True,
    tools= tools
)

# agent_executor("How many users are in the database?") # 2000 users
agent_executor("How many users have provided a shipping address?")