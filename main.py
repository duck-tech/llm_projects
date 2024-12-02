from langchain.chat_models import ChatOpenAI
from langchain.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
)
from langchain.schema import SystemMessage
from langchain.agents import OpenAIFunctionsAgent, AgentExecutor
from langchain.memory import ConversationBufferMemory
from handlers.chat_model_start_handler import ChatModelStartHandler
from dotenv import load_dotenv

from tools.sql import run_query_tool, list_tables, describe_tables_tool
from tools.report import write_report_tool
load_dotenv()

handler = ChatModelStartHandler()
chat = ChatOpenAI(
    callbacks = [handler]
)

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
        MessagesPlaceholder(variable_name="chat_history"),
        HumanMessagePromptTemplate.from_template("{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad") # 像是memory 是存在intermediate_steps, 下一個talk就會被刪除
    ]
)
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
tools = [run_query_tool, describe_tables_tool, write_report_tool]

agent = OpenAIFunctionsAgent(
    llm=chat, 
    prompt=prompt,
    tools = tools
)

agent_executor = AgentExecutor(
    agent=agent,
    # verbose=True,
    tools= tools,
    memory=memory
)

# agent_executor("How many users are in the database?") # 2000 users
# agent_executor("How many users have provided a shipping address?")
# agent_executor("Summarize the top 5 most popular product. Write the result to a report file.")
agent_executor("How many orders are there? Write the result to an html report")
agent_executor("Repeat the exact same process for users")