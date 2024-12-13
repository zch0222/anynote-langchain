from langchain_ollama.chat_models import ChatOllama
from langchain_openai import ChatOpenAI

def get_ollama_model(model: str):
    return ChatOllama(model=model)

def get_openai_model(model: str):
    return

def get_model(model: str):
    split_model = model.split(':')
    if split_model[0] == "ollama":
        return get_ollama_model(split_model[1])
    elif split_model[0] == "openai":
        return get_openai_model(split_model[1])