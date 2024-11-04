from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAIEmbeddings()

text_splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=200,
    chunk_overlap=0,
)

loader = TextLoader("facts.txt")
# 1. docs = loader.load()
docs = loader.load_and_split(
    text_splitter=text_splitter
)

# 1. print(docs)
for doc in docs:
    print(doc.page_content)
    print("\n")