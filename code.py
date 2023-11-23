from langchain.document_loaders.generic import GenericLoader
from langchain.document_loaders.parsers import LanguageParser
from langchain.text_splitter import Language
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationSummaryMemory
import dotenv
import os

dotenv.load_dotenv()
print(os.environ["OPENAI_API_KEY"])

repo_path = "/Volumes/aigo/code/vue/gpt-web"

loader = GenericLoader.from_filesystem(
    repo_path,
    glob="**/*",
    suffixes=[".js"],
    parser=LanguageParser(language=Language.JS, parser_threshold=500),
)
documents = loader.load()

print(len(documents))

python_splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.JS, chunk_size=2000, chunk_overlap=200
)
texts = python_splitter.split_documents(documents)
print(len(texts))

db = Chroma.from_documents(texts, OpenAIEmbeddings(disallowed_special=()))

retriever = db.as_retriever(
    search_type="mmr",  # Also test "similarity"
    search_kwargs={"k": 8},
)

llm = ChatOpenAI(model_name="gpt-3.5-turbo")
memory = ConversationSummaryMemory(
    llm=llm, memory_key="chat_history", return_messages=True
)
qa = ConversationalRetrievalChain.from_llm(llm, retriever=retriever, memory=memory)

question = input("请输入问题：")

result = qa(question)
print(result["answer"])
