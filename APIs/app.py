from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langserve import add_routes
import uvicorn
import os
from langchain_ollama import OllamaLLM
from dotenv import load_dotenv

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
## langsmith tracking  
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

app = FastAPI(
    title="LLM-Based Question-Answering API",
    description="An API that uses LangChain to provide answers to questions using a variety of LLMs.",
    version="1.0.0",
)

add_routes(
    app, 
    ChatOpenAI(),
    path="/openai"
)

model = ChatOpenAI(model="gpt-3.5-turbo")
llm = OllamaLLM(model="llama2")

prompt1 = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant"),
        ("user", "Tell me an analysis about {topic}")
    ]
)
prompt2 = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant"),
        ("user", "Tell me a poem in 100 words about {topic}")
    ]
)

add_routes(
    app,
    prompt1|model,
    path="/essay"
)

add_routes(
    app,
    prompt2|llm,
    path="/poem"
)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)