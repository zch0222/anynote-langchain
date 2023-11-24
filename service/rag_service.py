from fastapi import Depends
from core import get_redis, INDEX_PATH
import redis
import time
import json
import os
from model import ResData, PdfVO
from langchain.embeddings import OpenAIEmbeddings
from langchain.schema import StrOutputParser
from langchain.schema.runnable import RunnablePassthrough
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.document_loaders import PyPDFLoader
from langchain import hub
from langchain.chat_models import ChatOpenAI

from model import PDFRequestDTO
from utils.docs_util import format_docs


class RagService:

    def __init__(self, redis_client: redis.Redis = Depends(get_redis)):
        self.redis_client = redis_client
        self.vectorstore = None

    def pdf(self, pdf_request_dto: PDFRequestDTO):
        self.vectorstore = None
        loader = PyPDFLoader(pdf_request_dto.url)
        docs = loader.load_and_split()
        print(docs)
        index_path = f"{INDEX_PATH}/{pdf_request_dto.file_key}"
        embeddings = OpenAIEmbeddings()
        if os.path.exists(index_path) and os.path.isdir(index_path):
            print("use persist")
            self.vectorstore = Chroma.from_documents(persist_directory=index_path, embedding_function=embeddings)
        else:
            print("indexing............")
            text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
            splits = text_splitter.split_documents(docs)
            self.vectorstore = Chroma.from_documents(documents=splits, embedding=embeddings)
            self.vectorstore.persist(persist_directory=index_path)

        retriever = self.vectorstore.as_retriever()
        prompt = hub.pull("rlm/rag-prompt")
        llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
        rag_chain = (
                {"context": retriever | format_docs, "question": RunnablePassthrough()}
                | prompt
                | llm
                | StrOutputParser()
        )
        message = ""
        for chunk in rag_chain.stream(pdf_request_dto.question):
            message = message + chunk
            yield 'id: "{}"\nevent: "message"\ndata: {}\n\n'.format(int(time.time()),
                                                                    json.dumps(ResData.success(
                                                                        PdfVO(message=message).to_dic()
                                                                    )))
