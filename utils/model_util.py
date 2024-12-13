from langchain_ollama.chat_models import ChatOllama
from langchain_openai import ChatOpenAI
from langchain_huggingface import HuggingFaceEmbeddings

def get_ollama_model(model: str):
    return ChatOllama(model=model)

def get_openai_model(model: str):
    return ChatOpenAI(model=model)

def get_huggingface_embeddings(model: str):
    return HuggingFaceEmbeddings(model_name=model)


def get_model(model: str):
    split_model = model.split('_')
    print(split_model)
    if split_model[0] == "ollama":
        return get_ollama_model(split_model[1])
    elif split_model[0] == "openai":
        return get_openai_model(split_model[1])

def get_embedding_model(model: str):
    split_model = model.split('_')
    print(split_model)
    if split_model[0] == "ollama":
        return get_ollama_model(split_model[1])
    elif split_model[0] == "huggingface":
        return get_huggingface_embeddings(split_model[1])