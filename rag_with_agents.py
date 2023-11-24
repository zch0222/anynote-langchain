import dotenv
import os
import bs4
from langchain import hub
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import WebBaseLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.schema import StrOutputParser
from langchain.schema.runnable import RunnablePassthrough
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.document_loaders import PyPDFLoader
from langchain.agents.agent_toolkits import create_retriever_tool
from langchain.agents.agent_toolkits import create_conversational_retrieval_agent
from langchain.chat_models import ChatOpenAI





dotenv.load_dotenv()
print(os.environ["OPENAI_API_KEY"])

# loader = PyPDFLoader("./data/2022.pdf")
# docs = loader.load_and_split()
#
# print(docs)
#
# text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
# splits = text_splitter.split_documents(docs)

embeddings = OpenAIEmbeddings()

vectorstore = Chroma(persist_directory="./data/Wen-Tiejun_Ten-Crises_Online-PDF_20210619_REVISED-1-150_pdf",  embedding_function=embeddings)
retriever = vectorstore.as_retriever()

tool = create_retriever_tool(
    retriever,
    "search_Wen-Tiejun_Ten-Crises_Online-PDF_20210619_REVISED-1-150_pdf",
    "Searches and returns documents regarding the Wen-Tiejun_Ten-Crises_Online-PDF_20210619_REVISED-1-150.pdf.",
)

tools = [tool]

llm = ChatOpenAI(model_name="gpt-4-1106-preview", temperature=0)

agent_executor = create_conversational_retrieval_agent(llm, tools, verbose=True)

while(True):
    ask = input("请输入问题：")
    result = agent_executor({"input": ask})
    print(result["output"])

