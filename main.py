from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores.chroma import Chroma 
from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAIEmbeddings()

text_splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=200,
    chunk_overlap=0,
)

loader = TextLoader("facts.txt")

docs = loader.load_and_split(
    text_splitter=text_splitter
)

db=Chroma.from_documents(
    docs, # 計算embbedings
    embedding=embeddings,
    persist_directory="emb"
)

# k 是輸出多少個相近結果  default=4
results = db.similarity_search_with_score("What is an interesting fact about the English language?",
                                          k=3 )

for result in results:
    print("\n")
    print(result[1])
    print(result[0].page_content)





