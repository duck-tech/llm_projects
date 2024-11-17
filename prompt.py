from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores.chroma import Chroma 
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

chat= ChatOpenAI()
embeddings = OpenAIEmbeddings()


db=Chroma(
    embedding_function=embeddings,
    persist_directory="emb"

)

retriever = db.as_retriever()

chain = RetrievalQA.from_chain_type(
    llm=chat,
    retriever=retriever,
    chain_type="stuff"
)

result = chain.run("What is an interesting fact about the English language?")

print(result)





