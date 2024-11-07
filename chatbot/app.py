from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()

## langsmith tracking  
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

##prompt template

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful AI assistant. You will be given a task. You must generate a detailed and long answer."),
        ("user", "Question: {question}"),
    ]
)

## streamlit framework

st.title("Langchain Chatbot")
input_text = st.text_area("Enter your question")

## openai LLM
llm = ChatOpenAI(model = "gpt-3.5-turbo")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if input_text:
    st.write(chain.invoke({'question' : input_text}))